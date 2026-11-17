#!/usr/bin/env python3
"""
Evaluate AWS CLI commands against EC2 Emulator.
Runs each command against a running emulator instance.
"""

import json
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime


def parse_bash_script(script_file):
    """
    Parse bash script and extract commands line by line.
    Returns list of (label_or_none, cmd). If the line immediately before a command
    is '# label: ec2' or '# label: non-ec2' or '# label: augmented-ec2', that value is used; else None.
    """
    commands = []
    prev_line = ""
    
    with open(script_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_stripped = line.strip()
            
            if not line_stripped:
                continue
            if line_stripped.startswith('#'):
                prev_line = line_stripped
                continue
            
            label = None
            if prev_line.startswith("# label:"):
                label = prev_line.split(":", 1)[-1].strip()
            commands.append((label, line_stripped))
            prev_line = ""
    
    return commands


def _emulator_env():
    """Build env with aws-ec2 .venv/bin on PATH so 'awscli' is found."""
    env = dict(os.environ)
    # eval_emulator.py lives in emulators/aws-ec2/tests/; awscli is in emulators/aws-ec2/.venv/bin
    script_dir = Path(__file__).resolve().parent
    venv_bin = script_dir.parent / ".venv" / "bin"
    if venv_bin.is_dir():
        env["PATH"] = str(venv_bin) + os.pathsep + env.get("PATH", "")
    return env


# ---------------------------------------------------------------------------
# Lifecycle describe-after-mutate verification
# ---------------------------------------------------------------------------

# For create actions: maps ec2 subcommand → (response JSON path to ID, describe subcommand, describe ID flag)
# After a successful create, we extract the resource ID from stdout and run describe to verify it exists.
_CREATE_DESCRIBE_MAP = {
    "create-vpc":                   (["Vpc", "VpcId"],                       "describe-vpcs",                     "--vpc-ids"),
    "create-subnet":                (["Subnet", "SubnetId"],                 "describe-subnets",                  "--subnet-ids"),
    "create-security-group":        (["GroupId"],                            "describe-security-groups",           "--group-ids"),
    "create-key-pair":              (["KeyName"],                            "describe-key-pairs",                 "--key-names"),
    "create-volume":                (["VolumeId"],                           "describe-volumes",                   "--volume-ids"),
    "create-snapshot":              (["SnapshotId"],                         "describe-snapshots",                 "--snapshot-ids"),
    "create-internet-gateway":      (["InternetGateway", "InternetGatewayId"], "describe-internet-gateways",      "--internet-gateway-ids"),
    "create-route-table":           (["RouteTable", "RouteTableId"],         "describe-route-tables",             "--route-table-ids"),
    "create-network-acl":           (["NetworkAcl", "NetworkAclId"],         "describe-network-acls",             "--network-acl-ids"),
    "create-network-interface":     (["NetworkInterface", "NetworkInterfaceId"], "describe-network-interfaces",   "--network-interface-ids"),
    "create-placement-group":       (["PlacementGroup", "GroupName"],        "describe-placement-groups",         "--group-names"),
    "create-managed-prefix-list":   (["PrefixList", "PrefixListId"],         "describe-managed-prefix-lists",     "--prefix-list-ids"),
    "create-nat-gateway":           (["NatGateway", "NatGatewayId"],         "describe-nat-gateways",             "--nat-gateway-ids"),
    "create-transit-gateway":       (["TransitGateway", "TransitGatewayId"], "describe-transit-gateways",         "--transit-gateway-ids"),
    "create-vpn-gateway":           (["VpnGateway", "VpnGatewayId"],        "describe-vpn-gateways",             "--vpn-gateway-ids"),
    "create-customer-gateway":      (["CustomerGateway", "CustomerGatewayId"], "describe-customer-gateways",     "--customer-gateway-ids"),
    "create-vpc-endpoint":          (["VpcEndpoint", "VpcEndpointId"],       "describe-vpc-endpoints",            "--vpc-endpoint-ids"),
    "create-vpc-peering-connection":(["VpcPeeringConnection", "VpcPeeringConnectionId"], "describe-vpc-peering-connections", "--vpc-peering-connection-ids"),
    "create-dhcp-options":          (["DhcpOptions", "DhcpOptionsId"],       "describe-dhcp-options",             "--dhcp-options-ids"),
    "create-capacity-reservation":  (["CapacityReservation", "CapacityReservationId"], "describe-capacity-reservations", "--capacity-reservation-ids"),
    "create-traffic-mirror-filter": (["TrafficMirrorFilter", "TrafficMirrorFilterId"], "describe-traffic-mirror-filters", "--traffic-mirror-filter-ids"),
    "create-traffic-mirror-target": (["TrafficMirrorTarget", "TrafficMirrorTargetId"], "describe-traffic-mirror-targets", "--traffic-mirror-target-ids"),
    "create-traffic-mirror-session":(["TrafficMirrorSession", "TrafficMirrorSessionId"], "describe-traffic-mirror-sessions", "--traffic-mirror-session-ids"),
    "allocate-address":             (["AllocationId"],                       "describe-addresses",                "--allocation-ids"),
    "run-instances":                (["Instances", 0, "InstanceId"],         "describe-instances",                "--instance-ids"),
    "create-flow-logs":             (["FlowLogIds", 0],                      "describe-flow-logs",                "--flow-log-ids"),
    "create-carrier-gateway":       (["CarrierGateway", "CarrierGatewayId"], "describe-carrier-gateways",         "--carrier-gateway-ids"),
    "create-egress-only-internet-gateway": (["EgressOnlyInternetGateway", "EgressOnlyInternetGatewayId"], "describe-egress-only-internet-gateways", "--egress-only-internet-gateway-ids"),
    "create-launch-template":       (["LaunchTemplate", "LaunchTemplateId"], "describe-launch-templates",         "--launch-template-ids"),
    "create-fleet":                 (["FleetId"],                            "describe-fleets",                   "--fleet-ids"),
    "allocate-hosts":               (["HostIds", 0],                         "describe-hosts",                    "--host-ids"),
    "create-image":                 (["ImageId"],                            "describe-images",                   "--image-ids"),
    "create-transit-gateway-vpc-attachment": (["TransitGatewayVpcAttachment", "TransitGatewayAttachmentId"], "describe-transit-gateway-vpc-attachments", "--transit-gateway-attachment-ids"),
    "create-transit-gateway-route-table": (["TransitGatewayRouteTable", "TransitGatewayRouteTableId"], "describe-transit-gateway-route-tables", "--transit-gateway-route-table-ids"),
    "create-transit-gateway-connect": (["TransitGatewayConnect", "TransitGatewayAttachmentId"], "describe-transit-gateway-connects", "--transit-gateway-attachment-ids"),
    "create-transit-gateway-peering-attachment": (["TransitGatewayPeeringAttachment", "TransitGatewayAttachmentId"], "describe-transit-gateway-peering-attachments", "--transit-gateway-attachment-ids"),
    "create-transit-gateway-multicast-domain": (["TransitGatewayMulticastDomain", "TransitGatewayMulticastDomainId"], "describe-transit-gateway-multicast-domains", "--transit-gateway-multicast-domain-ids"),
    "create-transit-gateway-policy-table": (["TransitGatewayPolicyTable", "TransitGatewayPolicyTableId"], "describe-transit-gateway-policy-tables", "--transit-gateway-policy-table-ids"),
    "create-verified-access-instance": (["VerifiedAccessInstance", "VerifiedAccessInstanceId"], "describe-verified-access-instances", "--verified-access-instance-ids"),
    "create-verified-access-group": (["VerifiedAccessGroup", "VerifiedAccessGroupId"], "describe-verified-access-groups", "--verified-access-group-ids"),
    "create-verified-access-endpoint": (["VerifiedAccessEndpoint", "VerifiedAccessEndpointId"], "describe-verified-access-endpoints", "--verified-access-endpoint-ids"),
    "create-verified-access-trust-provider": (["VerifiedAccessTrustProvider", "VerifiedAccessTrustProviderId"], "describe-verified-access-trust-providers", "--verified-access-trust-provider-ids"),
    "create-vpc-endpoint-service-configuration": (["ServiceConfiguration", "ServiceId"], "describe-vpc-endpoint-service-configurations", "--service-ids"),
    "create-vpc-endpoint-connection-notification": (["ConnectionNotification", "ConnectionNotificationId"], "describe-vpc-endpoint-connection-notifications", "--connection-notification-ids"),
    "create-network-insights-path": (["NetworkInsightsPath", "NetworkInsightsPathId"], "describe-network-insights-paths", "--network-insights-path-ids"),
    "create-network-insights-access-scope": (["NetworkInsightsAccessScope", "NetworkInsightsAccessScopeId"], "describe-network-insights-access-scopes", "--network-insights-access-scope-ids"),
    "create-instance-event-window": (["InstanceEventWindow", "InstanceEventWindowId"], "describe-instance-event-windows", "--instance-event-window-ids"),
    "create-instance-connect-endpoint": (["InstanceConnectEndpoint", "InstanceConnectEndpointId"], "describe-instance-connect-endpoints", "--instance-connect-endpoint-ids"),
    "register-image":               (["ImageId"],                            "describe-images",                   "--image-ids"),
}

# For delete actions: maps ec2 subcommand → (command-line flag containing the ID, describe subcommand, describe ID flag)
# After a successful delete, we parse the ID from the command args and run describe to verify it's gone.
_DELETE_DESCRIBE_MAP = {
    "delete-vpc":                   ("--vpc-id",            "describe-vpcs",                    "--vpc-ids"),
    "delete-subnet":                ("--subnet-id",         "describe-subnets",                 "--subnet-ids"),
    "delete-security-group":        ("--group-id",          "describe-security-groups",          "--group-ids"),
    "delete-key-pair":              ("--key-name",          "describe-key-pairs",                "--key-names"),
    "delete-volume":                ("--volume-id",         "describe-volumes",                  "--volume-ids"),
    "delete-snapshot":              ("--snapshot-id",       "describe-snapshots",                "--snapshot-ids"),
    "delete-internet-gateway":      ("--internet-gateway-id", "describe-internet-gateways",     "--internet-gateway-ids"),
    "delete-route-table":           ("--route-table-id",    "describe-route-tables",             "--route-table-ids"),
    "delete-network-acl":           ("--network-acl-id",    "describe-network-acls",             "--network-acl-ids"),
    "delete-network-interface":     ("--network-interface-id", "describe-network-interfaces",    "--network-interface-ids"),
    "delete-placement-group":       ("--group-name",        "describe-placement-groups",          "--group-names"),
    "delete-managed-prefix-list":   ("--prefix-list-id",    "describe-managed-prefix-lists",     "--prefix-list-ids"),
    "delete-nat-gateway":           ("--nat-gateway-id",    "describe-nat-gateways",             "--nat-gateway-ids"),
    "delete-transit-gateway":       ("--transit-gateway-id", "describe-transit-gateways",        "--transit-gateway-ids"),
    "delete-vpn-gateway":           ("--vpn-gateway-id",    "describe-vpn-gateways",             "--vpn-gateway-ids"),
    "delete-customer-gateway":      ("--customer-gateway-id", "describe-customer-gateways",     "--customer-gateway-ids"),
    "delete-vpc-endpoints":         ("--vpc-endpoint-ids",  "describe-vpc-endpoints",            "--vpc-endpoint-ids"),
    "delete-vpc-peering-connection":("--vpc-peering-connection-id", "describe-vpc-peering-connections", "--vpc-peering-connection-ids"),
    "delete-dhcp-options":          ("--dhcp-options-id",   "describe-dhcp-options",              "--dhcp-options-ids"),
    "cancel-capacity-reservation":  ("--capacity-reservation-id", "describe-capacity-reservations", "--capacity-reservation-ids"),
    "delete-traffic-mirror-filter": ("--traffic-mirror-filter-id", "describe-traffic-mirror-filters", "--traffic-mirror-filter-ids"),
    "delete-traffic-mirror-target": ("--traffic-mirror-target-id", "describe-traffic-mirror-targets", "--traffic-mirror-target-ids"),
    "delete-traffic-mirror-session":("--traffic-mirror-session-id", "describe-traffic-mirror-sessions", "--traffic-mirror-session-ids"),
    "release-address":              ("--allocation-id",     "describe-addresses",                "--allocation-ids"),
    "terminate-instances":          ("--instance-ids",      "describe-instances",                "--instance-ids"),
    "delete-flow-logs":             ("--flow-log-ids",      "describe-flow-logs",                "--flow-log-ids"),
    "delete-carrier-gateway":       ("--carrier-gateway-id", "describe-carrier-gateways",        "--carrier-gateway-ids"),
    "delete-egress-only-internet-gateway": ("--egress-only-internet-gateway-id", "describe-egress-only-internet-gateways", "--egress-only-internet-gateway-ids"),
    "delete-launch-template":       ("--launch-template-id", "describe-launch-templates",        "--launch-template-ids"),
    "delete-fleets":                ("--fleet-ids",          "describe-fleets",                   "--fleet-ids"),
    "release-hosts":                ("--host-ids",           "describe-hosts",                    "--host-ids"),
    "deregister-image":             ("--image-id",           "describe-images",                   "--image-ids"),
    "delete-transit-gateway-vpc-attachment": ("--transit-gateway-attachment-id", "describe-transit-gateway-vpc-attachments", "--transit-gateway-attachment-ids"),
    "delete-transit-gateway-route-table": ("--transit-gateway-route-table-id", "describe-transit-gateway-route-tables", "--transit-gateway-route-table-ids"),
    "delete-transit-gateway-connect": ("--transit-gateway-attachment-id", "describe-transit-gateway-connects", "--transit-gateway-attachment-ids"),
    "delete-transit-gateway-peering-attachment": ("--transit-gateway-attachment-id", "describe-transit-gateway-peering-attachments", "--transit-gateway-attachment-ids"),
    "delete-transit-gateway-multicast-domain": ("--transit-gateway-multicast-domain-id", "describe-transit-gateway-multicast-domains", "--transit-gateway-multicast-domain-ids"),
    "delete-transit-gateway-policy-table": ("--transit-gateway-policy-table-id", "describe-transit-gateway-policy-tables", "--transit-gateway-policy-table-ids"),
    "delete-verified-access-instance": ("--verified-access-instance-id", "describe-verified-access-instances", "--verified-access-instance-ids"),
    "delete-verified-access-group": ("--verified-access-group-id", "describe-verified-access-groups", "--verified-access-group-ids"),
    "delete-verified-access-endpoint": ("--verified-access-endpoint-id", "describe-verified-access-endpoints", "--verified-access-endpoint-ids"),
    "delete-verified-access-trust-provider": ("--verified-access-trust-provider-id", "describe-verified-access-trust-providers", "--verified-access-trust-provider-ids"),
    "delete-vpc-endpoint-service-configurations": ("--service-ids", "describe-vpc-endpoint-service-configurations", "--service-ids"),
    "delete-vpc-endpoint-connection-notifications": ("--connection-notification-ids", "describe-vpc-endpoint-connection-notifications", "--connection-notification-ids"),
    "delete-network-insights-path": ("--network-insights-path-id", "describe-network-insights-paths", "--network-insights-path-ids"),
    "delete-network-insights-access-scope": ("--network-insights-access-scope-id", "describe-network-insights-access-scopes", "--network-insights-access-scope-ids"),
    "delete-instance-event-window": ("--instance-event-window-id", "describe-instance-event-windows", "--instance-event-window-ids"),
    "delete-instance-connect-endpoint": ("--instance-connect-endpoint-id", "describe-instance-connect-endpoints", "--instance-connect-endpoint-ids"),
}

# For modify/attach/associate actions: maps ec2 subcommand → (command-line flag containing the ID, describe subcommand, describe ID flag)
# After a successful modify, we parse the ID from the command args and run describe to verify the resource still exists.
_MODIFY_DESCRIBE_MAP = {
    # modify-* commands
    "modify-vpc-attribute":              ("--vpc-id",              "describe-vpcs",                    "--vpc-ids"),
    "modify-subnet-attribute":           ("--subnet-id",           "describe-subnets",                 "--subnet-ids"),
    "modify-instance-attribute":         ("--instance-id",         "describe-instances",               "--instance-ids"),
    "modify-instance-maintenance-options": ("--instance-id",       "describe-instances",               "--instance-ids"),
    "modify-instance-metadata-options":  ("--instance-id",         "describe-instances",               "--instance-ids"),
    "modify-instance-placement":         ("--instance-id",         "describe-instances",               "--instance-ids"),
    "modify-instance-capacity-reservation-attributes": ("--instance-id", "describe-instances",         "--instance-ids"),
    "modify-volume":                     ("--volume-id",           "describe-volumes",                 "--volume-ids"),
    "modify-volume-attribute":           ("--volume-id",           "describe-volumes",                 "--volume-ids"),
    "modify-snapshot-attribute":         ("--snapshot-id",         "describe-snapshots",               "--snapshot-ids"),
    "modify-network-interface-attribute": ("--network-interface-id", "describe-network-interfaces",    "--network-interface-ids"),
    "modify-security-group-rules":       ("--group-id",            "describe-security-groups",         "--group-ids"),
    "modify-managed-prefix-list":        ("--prefix-list-id",      "describe-managed-prefix-lists",    "--prefix-list-ids"),
    "modify-capacity-reservation":       ("--capacity-reservation-id", "describe-capacity-reservations", "--capacity-reservation-ids"),
    "modify-capacity-reservation-fleet": ("--capacity-reservation-fleet-id", "describe-capacity-reservation-fleets", "--capacity-reservation-fleet-ids"),
    "modify-fleet":                      ("--fleet-id",            "describe-fleets",                  "--fleet-ids"),
    "modify-hosts":                      ("--host-ids",            "describe-hosts",                   "--host-ids"),
    "modify-image-attribute":            ("--image-id",            "describe-images",                  "--image-ids"),
    "modify-fpga-image-attribute":       ("--fpga-image-id",       "describe-fpga-images",             "--fpga-image-ids"),
    "modify-launch-template":            ("--launch-template-id",  "describe-launch-templates",        "--launch-template-ids"),
    "modify-transit-gateway":            ("--transit-gateway-id",  "describe-transit-gateways",        "--transit-gateway-ids"),
    "modify-transit-gateway-vpc-attachment": ("--transit-gateway-attachment-id", "describe-transit-gateway-vpc-attachments", "--transit-gateway-attachment-ids"),
    "modify-transit-gateway-prefix-list-reference": ("--transit-gateway-route-table-id", "describe-transit-gateway-route-tables", "--transit-gateway-route-table-ids"),
    "modify-traffic-mirror-session":     ("--traffic-mirror-session-id", "describe-traffic-mirror-sessions", "--traffic-mirror-session-ids"),
    "modify-traffic-mirror-filter-network-services": ("--traffic-mirror-filter-id", "describe-traffic-mirror-filters", "--traffic-mirror-filter-ids"),
    "modify-verified-access-endpoint":   ("--verified-access-endpoint-id", "describe-verified-access-endpoints", "--verified-access-endpoint-ids"),
    "modify-verified-access-group":      ("--verified-access-group-id", "describe-verified-access-groups", "--verified-access-group-ids"),
    "modify-verified-access-instance":   ("--verified-access-instance-id", "describe-verified-access-instances", "--verified-access-instance-ids"),
    "modify-verified-access-trust-provider": ("--verified-access-trust-provider-id", "describe-verified-access-trust-providers", "--verified-access-trust-provider-ids"),
    "modify-vpc-endpoint":               ("--vpc-endpoint-id",    "describe-vpc-endpoints",           "--vpc-endpoint-ids"),
    "modify-vpc-endpoint-connection-notification": ("--connection-notification-id", "describe-vpc-endpoint-connection-notifications", "--connection-notification-ids"),
    "modify-vpc-endpoint-service-configuration": ("--service-id",  "describe-vpc-endpoint-service-configurations", "--service-ids"),
    "modify-vpc-peering-connection-options": ("--vpc-peering-connection-id", "describe-vpc-peering-connections", "--vpc-peering-connection-ids"),
    "modify-vpn-connection":             ("--vpn-connection-id",   "describe-vpn-connections",         "--vpn-connection-ids"),
    "modify-vpn-connection-options":     ("--vpn-connection-id",   "describe-vpn-connections",         "--vpn-connection-ids"),
    "modify-vpn-tunnel-options":         ("--vpn-connection-id",   "describe-vpn-connections",         "--vpn-connection-ids"),
    "modify-vpn-tunnel-certificate":     ("--vpn-connection-id",   "describe-vpn-connections",         "--vpn-connection-ids"),
    "modify-client-vpn-endpoint":        ("--client-vpn-endpoint-id", "describe-client-vpn-endpoints", "--client-vpn-endpoint-ids"),
    "modify-instance-event-window":      ("--instance-event-window-id", "describe-instance-event-windows", "--instance-event-window-ids"),
    # attach/associate commands (modify-like: change resource state)
    "attach-internet-gateway":           ("--internet-gateway-id", "describe-internet-gateways",       "--internet-gateway-ids"),
    "attach-volume":                     ("--volume-id",           "describe-volumes",                 "--volume-ids"),
    "attach-network-interface":          ("--network-interface-id", "describe-network-interfaces",     "--network-interface-ids"),
    "attach-vpn-gateway":                ("--vpn-gateway-id",      "describe-vpn-gateways",            "--vpn-gateway-ids"),
    "attach-verified-access-trust-provider": ("--verified-access-instance-id", "describe-verified-access-instances", "--verified-access-instance-ids"),
    "associate-address":                 ("--allocation-id",       "describe-addresses",               "--allocation-ids"),
    "associate-dhcp-options":            ("--dhcp-options-id",     "describe-dhcp-options",            "--dhcp-options-ids"),
    "associate-route-table":             ("--route-table-id",      "describe-route-tables",            "--route-table-ids"),
    "associate-transit-gateway-route-table": ("--transit-gateway-route-table-id", "describe-transit-gateway-route-tables", "--transit-gateway-route-table-ids"),
    "associate-transit-gateway-multicast-domain": ("--transit-gateway-multicast-domain-id", "describe-transit-gateway-multicast-domains", "--transit-gateway-multicast-domain-ids"),
    "associate-instance-event-window":   ("--instance-event-window-id", "describe-instance-event-windows", "--instance-event-window-ids"),
    "authorize-security-group-ingress":  ("--group-id",            "describe-security-groups",         "--group-ids"),
    "authorize-security-group-egress":   ("--group-id",            "describe-security-groups",         "--group-ids"),
    "replace-transit-gateway-route":     ("--transit-gateway-route-table-id", "describe-transit-gateway-route-tables", "--transit-gateway-route-table-ids"),
    "replace-network-acl-entry":         ("--network-acl-id",      "describe-network-acls",            "--network-acl-ids"),
    "accept-transit-gateway-peering-attachment": ("--transit-gateway-attachment-id", "describe-transit-gateway-peering-attachments", "--transit-gateway-attachment-ids"),
    "associate-nat-gateway-address":     ("--nat-gateway-id",      "describe-nat-gateways",            "--nat-gateway-ids"),
    "enable-image":                      ("--image-id",            "describe-images",                  "--image-ids"),
    "disable-image":                     ("--image-id",            "describe-images",                  "--image-ids"),
}

# Top-level list keys returned by each describe command (to check count)
_DESCRIBE_LIST_KEY = {
    "describe-vpcs": "Vpcs",
    "describe-subnets": "Subnets",
    "describe-security-groups": "SecurityGroups",
    "describe-key-pairs": "KeyPairs",
    "describe-volumes": "Volumes",
    "describe-snapshots": "Snapshots",
    "describe-internet-gateways": "InternetGateways",
    "describe-route-tables": "RouteTables",
    "describe-network-acls": "NetworkAcls",
    "describe-network-interfaces": "NetworkInterfaces",
    "describe-placement-groups": "PlacementGroups",
    "describe-managed-prefix-lists": "PrefixLists",
    "describe-nat-gateways": "NatGateways",
    "describe-transit-gateways": "TransitGateways",
    "describe-vpn-gateways": "VpnGateways",
    "describe-customer-gateways": "CustomerGateways",
    "describe-vpc-endpoints": "VpcEndpoints",
    "describe-vpc-peering-connections": "VpcPeeringConnections",
    "describe-dhcp-options": "DhcpOptions",
    "describe-capacity-reservations": "CapacityReservations",
    "describe-traffic-mirror-filters": "TrafficMirrorFilters",
    "describe-traffic-mirror-targets": "TrafficMirrorTargets",
    "describe-traffic-mirror-sessions": "TrafficMirrorSessions",
    "describe-addresses": "Addresses",
    "describe-instances": "Reservations",
    "describe-flow-logs": "FlowLogs",
    "describe-carrier-gateways": "CarrierGateways",
    "describe-egress-only-internet-gateways": "EgressOnlyInternetGateways",
    "describe-launch-templates": "LaunchTemplates",
    "describe-fleets": "Fleets",
    "describe-hosts": "Hosts",
    "describe-images": "Images",
    "describe-transit-gateway-vpc-attachments": "TransitGatewayVpcAttachments",
    "describe-transit-gateway-route-tables": "TransitGatewayRouteTables",
    "describe-transit-gateway-connects": "TransitGatewayConnects",
    "describe-transit-gateway-peering-attachments": "TransitGatewayPeeringAttachments",
    "describe-transit-gateway-multicast-domains": "TransitGatewayMulticastDomains",
    "describe-transit-gateway-policy-tables": "TransitGatewayPolicyTables",
    "describe-verified-access-instances": "VerifiedAccessInstances",
    "describe-verified-access-groups": "VerifiedAccessGroups",
    "describe-verified-access-endpoints": "VerifiedAccessEndpoints",
    "describe-verified-access-trust-providers": "VerifiedAccessTrustProviders",
    "describe-vpc-endpoint-service-configurations": "ServiceConfigurations",
    "describe-vpc-endpoint-connection-notifications": "ConnectionNotificationSet",
    "describe-network-insights-paths": "NetworkInsightsPaths",
    "describe-network-insights-access-scopes": "NetworkInsightsAccessScopes",
    "describe-instance-event-windows": "InstanceEventWindows",
    "describe-instance-connect-endpoints": "InstanceConnectEndpoints",
}


# ---------------------------------------------------------------------------
# Field-level accuracy verification
# After create/modify, verify that the specific fields we set/changed are
# correctly reflected in the describe response.
# ---------------------------------------------------------------------------

_TERMINAL_STATES = frozenset({
    "deleted", "deleting", "terminated", "shutting-down",
    "cancelled", "deregistered", "expired", "released",
})

_DESCRIBE_ITEM_PATH = {
    "describe-instances": ["Instances", 0],
}

_ID_FLAGS = frozenset({
    "--vpc-id", "--subnet-id", "--instance-id", "--volume-id", "--snapshot-id",
    "--group-id", "--key-name", "--image-id", "--allocation-id",
    "--internet-gateway-id", "--route-table-id", "--network-acl-id",
    "--network-interface-id", "--prefix-list-id", "--nat-gateway-id",
    "--transit-gateway-id", "--vpn-gateway-id", "--customer-gateway-id",
    "--vpc-endpoint-id", "--vpc-peering-connection-id", "--dhcp-options-id",
    "--capacity-reservation-id", "--traffic-mirror-filter-id",
    "--traffic-mirror-target-id", "--traffic-mirror-session-id",
    "--flow-log-ids", "--carrier-gateway-id",
    "--egress-only-internet-gateway-id", "--launch-template-id",
    "--fleet-id", "--host-ids", "--instance-ids",
    "--transit-gateway-attachment-id", "--transit-gateway-route-table-id",
    "--transit-gateway-multicast-domain-id", "--transit-gateway-policy-table-id",
    "--verified-access-instance-id", "--verified-access-group-id",
    "--verified-access-endpoint-id", "--verified-access-trust-provider-id",
    "--service-id", "--connection-notification-id",
    "--network-insights-path-id", "--network-insights-access-scope-id",
    "--instance-event-window-id", "--instance-connect-endpoint-id",
    "--ipam-id", "--ipam-scope-id", "--ipam-pool-id",
    "--ipam-resource-discovery-id", "--resource-ids",
    "--peer-vpc-id", "--vpc-endpoint-ids",
})

_META_FLAGS = frozenset({
    "--output", "--region", "--endpoint-url", "--query", "--no-paginate",
    "--current-version", "--dry-run", "--no-dry-run",
    "--tag-specifications", "--tags",
    "--block-device-mappings", "--root-device-name",
    "--session-number", "--no-reboot",
    "--quantity", "--count",
    "--device", "--device-name",
    "--end-date",
    "--instance-type",
    "--disable-api-termination", "--no-disable-api-termination",
    "--disable-api-stop", "--no-disable-api-stop",
    "--auto-enable-io", "--no-auto-enable-io",
})

_COMPLEX_FLAGS = frozenset({
    "--options", "--add-operating-regions", "--remove-operating-regions",
    "--add-entries", "--remove-entries", "--time-range",
    "--add-route-table-ids", "--remove-route-table-ids",
    "--add-subnet-ids", "--remove-subnet-ids",
    "--add-security-group-ids", "--remove-security-group-ids",
    "--enable-dns-hostnames", "--enable-dns-support",
    "--no-enable-dns-hostnames", "--no-enable-dns-support",
    "--operating-regions",
    "--network-load-balancer-arns", "--gateway-load-balancer-endpoint-ids",
    "--entries",
    "--launch-permission", "--ip-permissions",
    "--protocol", "--port", "--cidr",
})

_FLAG_FIELD_OVERRIDES = {
    "--instance-count": "TotalInstanceCount",
    "--public-ip": "IpAddress",
    "--prefix-list-name": "PrefixListName",
    "--group-name": "GroupName",
    "--key-type": "KeyType",
    "--connectivity-type": "ConnectivityType",
    "--address-family": "AddressFamily",
    "--max-entries": "MaxEntries",
    "--auto-placement": "AutoPlacement",
    "--cron-expression": "CronExpression",
    "--private-dns-name": "PrivateDnsName",
    "--instance-platform": "InstancePlatform",
    "--traffic-type": "TrafficType",
    "--resource-type": "ResourceType",
    "--log-destination-type": "LogDestinationType",
    "--log-destination": "LogDestination",
    "--map-public-ip-on-launch": "MapPublicIpOnLaunch",
    "--no-acceptance-required": "AcceptanceRequired",
    "--acceptance-required": "AcceptanceRequired",
    "--no-map-public-ip-on-launch": "MapPublicIpOnLaunch",
    "--bgp-asn": "BgpAsn",
    "--no-source-dest-check": "SourceDestCheck",
    "--source-dest-check": "SourceDestCheck",
    "--host-recovery": "HostRecovery",
    "--end-date-type": "EndDateType",
}


def _flag_to_field(flag):
    """Convert --kebab-case CLI flag to PascalCase JSON field name."""
    parts = flag.lstrip('-').split('-')
    return ''.join(p.capitalize() for p in parts)


def _extract_cli_flags(cmd):
    """Parse all --flag value pairs from a CLI command string.
    Returns list of (flag, value) tuples. Boolean flags have value=True,
    negation flags (--no-xxx) have value=False.
    """
    try:
        parts = shlex.split(cmd)
    except ValueError:
        parts = cmd.split()

    flags = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if p.startswith('--'):
            if i + 1 < len(parts) and not parts[i + 1].startswith('--'):
                flags.append((p, parts[i + 1]))
                i += 2
            else:
                flags.append((p, True))
                i += 1
        else:
            i += 1
    return flags


def _parse_flag_value(raw_value):
    """Parse a CLI flag value, handling JSON value format and types."""
    if isinstance(raw_value, bool):
        return raw_value
    if raw_value.startswith('{') and raw_value.endswith('}'):
        try:
            parsed = json.loads(raw_value)
            if "Value" in parsed:
                return parsed["Value"]
        except (json.JSONDecodeError, TypeError):
            pass
    try:
        return int(raw_value)
    except (ValueError, TypeError):
        pass
    return raw_value


def _get_expected_fields(subcmd, cmd):
    """Extract expected field→value pairs from a CLI command.
    Returns dict of {JSONFieldName: expected_value}.
    """
    flags = _extract_cli_flags(cmd)
    expected = {}

    for flag, raw_value in flags:
        if flag in _ID_FLAGS or flag in _META_FLAGS or flag in _COMPLEX_FLAGS:
            continue

        value = _parse_flag_value(raw_value)

        if flag in _FLAG_FIELD_OVERRIDES:
            field_name = _FLAG_FIELD_OVERRIDES[flag]
        else:
            field_name = _flag_to_field(flag)

        if flag.startswith('--no-') and isinstance(value, bool):
            value = False
        elif isinstance(value, bool) and value is True:
            pass

        expected[field_name] = value

    return expected


def _get_resource_from_describe(desc_resp, describe_sub):
    """Extract the first resource object from a describe response."""
    list_key = _DESCRIBE_LIST_KEY.get(describe_sub)
    if not list_key or not desc_resp:
        return None
    items = desc_resp.get(list_key, [])
    if not items:
        return None
    item = items[0]
    extra_path = _DESCRIBE_ITEM_PATH.get(describe_sub)
    if extra_path:
        for key in extra_path:
            if isinstance(item, dict):
                item = item.get(key)
            elif isinstance(item, list) and isinstance(key, int) and key < len(item):
                item = item[key]
            else:
                return None
            if item is None:
                return None
    return item


def _verify_fields(resource_obj, expected_fields):
    """Check expected field values against a resource object.
    Returns list of {field, expected, actual, match} dicts.
    """
    if not resource_obj or not expected_fields:
        return []
    results = []
    for field, expected_val in expected_fields.items():
        actual_val = resource_obj.get(field)
        match = False
        if actual_val is not None:
            if isinstance(actual_val, list) and not isinstance(expected_val, list):
                match = str(expected_val) in [str(x) for x in actual_val]
            elif isinstance(expected_val, bool):
                match = bool(actual_val) == expected_val
            elif isinstance(expected_val, int):
                try:
                    match = int(actual_val) == expected_val
                except (ValueError, TypeError):
                    match = str(actual_val) == str(expected_val)
            else:
                match = str(actual_val) == str(expected_val)
        results.append({
            "field": field,
            "expected": expected_val,
            "actual": actual_val,
            "match": match,
        })
    return results


# ---------------------------------------------------------------------------
# Dynamic ID tracking for bundled lifecycle tests
# After a create succeeds, extract real resource IDs from the JSON response
# and replace example IDs in subsequent commands with the real ones.
# ---------------------------------------------------------------------------

_ID_PREFIXES_RE = sorted([
    "vpc-cidr-assoc-", "tgw-attach-", "tgw-rtb-", "tgw-ptb-",
    "tgw-mcast-domain-", "tgw-connect-peer-",
    "vpce-svc-", "vpce-nfn-",
    "ipam-pool-", "ipam-scope-", "ipam-res-disco-",
    "eipalloc-", "eipassoc-", "import-snap-",
    "lgw-rtb-",
    "subnet-", "fleet-", "snap-", "dopt-", "vatp-", "vagr-", "cagw-",
    "eice-", "eigw-",
    "ipam-", "vpce-", "vpc-", "nat-", "tgw-", "vol-", "ami-",
    "rtb-", "acl-", "eni-", "pcx-", "dopt-", "vgw-", "vpn-", "cgw-", "crf-",
    "tmf-", "tmt-", "tms-", "vae-", "vai-", "iew-", "nip-", "nis-",
    "sg-", "cr-", "pl-", "lt-", "fl-", "igw-", "h-", "i-",
], key=len, reverse=True)

_ID_RE = re.compile(
    r'(' + '|'.join(re.escape(p) for p in _ID_PREFIXES_RE) + r')[0-9a-f]{4,}[0-9a-zA-Z]*'
)


def _extract_ids_from_response(cmd_result):
    """Extract all AWS resource IDs found in a command's JSON response."""
    resp = _extract_json_response(cmd_result)
    if not resp:
        return {}
    ids = {}
    text = json.dumps(resp)
    for m in _ID_RE.finditer(text):
        prefix = m.group(1)
        full_id = m.group(0)
        if prefix not in ids:
            ids[prefix] = full_id
    return ids


def _replace_ids_in_command(cmd, id_registry):
    """Replace example AWS resource IDs in a command string with real IDs."""
    def _replacer(match):
        prefix = match.group(1)
        if prefix in id_registry:
            return id_registry[prefix]
        return match.group(0)
    return _ID_RE.sub(_replacer, cmd)


def _extract_ec2_subcommand(cmd):
    """Extract the ec2 subcommand from a CLI command string, e.g. 'create-vpc'."""
    # handles both 'awscli ec2 create-vpc ...' and 'aws ec2 create-vpc ...'
    parts = cmd.split()
    for i, p in enumerate(parts):
        if p == "ec2" and i + 1 < len(parts):
            return parts[i + 1]
    return None


def _extract_json_response(cmd_result):
    """Try to parse JSON from stdout, falling back to stderr extraction."""
    stdout = (cmd_result.get('stdout') or '').strip()
    if stdout:
        try:
            return json.loads(stdout)
        except Exception:
            pass
    stderr = (cmd_result.get('stderr') or '')
    marker = "b'{"
    idx = stderr.find(marker)
    if idx != -1:
        end = stderr.rfind("}'")
        if end > idx:
            raw = stderr[idx + 2 : end + 1].replace("\\n", "\n")
            try:
                return json.loads(raw)
            except Exception:
                pass
    return None


def _navigate_path(data, path):
    """Walk a list of keys/indices into nested data. Returns None on failure."""
    val = data
    for key in path:
        if isinstance(val, dict):
            val = val.get(key)
        elif isinstance(val, list) and isinstance(key, int) and key < len(val):
            val = val[key]
        else:
            return None
        if val is None:
            return None
    return val


def _extract_flag_value(cmd, flag):
    """Extract the value of a CLI flag from a command string."""
    parts = cmd.split()
    for i, p in enumerate(parts):
        if p == flag and i + 1 < len(parts):
            return parts[i + 1]
    return None


def _build_describe_cmd(cmd, describe_sub, describe_flag, resource_id):
    """Build a describe CLI command using the same prefix (awscli/aws) as the original."""
    parts = cmd.split()
    prefix = parts[0] if parts else "awscli"
    return f"{prefix} ec2 {describe_sub} {describe_flag} {resource_id} --output json"


def run_lifecycle_verify(cmd, cmd_result, is_success):
    """After a successful create/modify/delete, run a describe to verify state.

    For create/modify, also does field-level accuracy checks: extracts the CLI
    flags, maps them to expected JSON field names, then verifies those values
    appear in the describe response.

    Returns a dict with verification results or None if not applicable.
    """
    if not is_success:
        return None

    subcmd = _extract_ec2_subcommand(cmd)
    if not subcmd:
        return None

    verify = None

    if subcmd in _CREATE_DESCRIBE_MAP:
        id_path, describe_sub, describe_flag = _CREATE_DESCRIBE_MAP[subcmd]
        resp = _extract_json_response(cmd_result)
        if resp is None:
            return {"type": "create_verify", "status": "skip", "reason": "could not parse create response"}
        resource_id = _navigate_path(resp, id_path)
        if not resource_id:
            return {"type": "create_verify", "status": "skip", "reason": f"ID not found at path {id_path}"}

        desc_cmd = _build_describe_cmd(cmd, describe_sub, describe_flag, resource_id)
        desc_result = run_command(desc_cmd, timeout=15)
        desc_resp = _extract_json_response(desc_result)

        list_key = _DESCRIBE_LIST_KEY.get(describe_sub)
        found = False
        if desc_resp and list_key:
            items = desc_resp.get(list_key, [])
            found = len(items) > 0
        elif desc_result['success']:
            found = True

        expected_fields = _get_expected_fields(subcmd, cmd)
        resource_obj = _get_resource_from_describe(desc_resp, describe_sub)
        field_results = _verify_fields(resource_obj, expected_fields)

        fields_checked = len(field_results)
        fields_matched = sum(1 for f in field_results if f["match"])
        field_status = "pass"
        if not found:
            field_status = "fail"
        elif fields_checked > 0 and fields_matched < fields_checked:
            field_status = "partial"

        verify = {
            "type": "create_verify",
            "describe_cmd": desc_cmd,
            "resource_id": str(resource_id),
            "found": found,
            "status": "pass" if found else "fail",
            "field_status": field_status,
            "fields_checked": fields_checked,
            "fields_matched": fields_matched,
            "field_results": field_results,
            "describe_success": desc_result['success'],
        }

    elif subcmd in _MODIFY_DESCRIBE_MAP:
        id_flag, describe_sub, describe_flag = _MODIFY_DESCRIBE_MAP[subcmd]
        resource_id = _extract_flag_value(cmd, id_flag)
        if not resource_id:
            return {"type": "modify_verify", "status": "skip", "reason": f"ID flag {id_flag} not found in command"}

        desc_cmd = _build_describe_cmd(cmd, describe_sub, describe_flag, resource_id)
        desc_result = run_command(desc_cmd, timeout=15)
        desc_resp = _extract_json_response(desc_result)

        list_key = _DESCRIBE_LIST_KEY.get(describe_sub)
        found = False
        if desc_resp and list_key:
            items = desc_resp.get(list_key, [])
            found = len(items) > 0
        elif desc_result['success']:
            found = True

        expected_fields = _get_expected_fields(subcmd, cmd)
        resource_obj = _get_resource_from_describe(desc_resp, describe_sub)
        field_results = _verify_fields(resource_obj, expected_fields)

        fields_checked = len(field_results)
        fields_matched = sum(1 for f in field_results if f["match"])

        if not found:
            status = "fail"
        elif fields_checked > 0 and fields_matched < fields_checked:
            status = "fail"
        else:
            status = "pass"

        verify = {
            "type": "modify_verify",
            "describe_cmd": desc_cmd,
            "resource_id": resource_id,
            "found": found,
            "status": status,
            "fields_checked": fields_checked,
            "fields_matched": fields_matched,
            "field_results": field_results,
            "describe_success": desc_result['success'],
        }

    elif subcmd in _DELETE_DESCRIBE_MAP:
        id_flag, describe_sub, describe_flag = _DELETE_DESCRIBE_MAP[subcmd]
        resource_id = _extract_flag_value(cmd, id_flag)
        if not resource_id:
            return {"type": "delete_verify", "status": "skip", "reason": f"ID flag {id_flag} not found in command"}

        desc_cmd = _build_describe_cmd(cmd, describe_sub, describe_flag, resource_id)
        desc_result = run_command(desc_cmd, timeout=15)
        desc_resp = _extract_json_response(desc_result)

        list_key = _DESCRIBE_LIST_KEY.get(describe_sub)
        still_exists = False
        if desc_resp and list_key:
            items = desc_resp.get(list_key, [])
            active = [it for it in items
                      if it.get("State") not in _TERMINAL_STATES
                      and it.get("Status", {}).get("Code") not in _TERMINAL_STATES
                      and it.get("FlowLogStatus") not in ("DELETED",)]
            still_exists = len(active) > 0
        elif desc_result['success'] and desc_result['stdout'].strip():
            still_exists = True

        verify = {
            "type": "delete_verify",
            "describe_cmd": desc_cmd,
            "resource_id": resource_id,
            "still_exists": still_exists,
            "status": "pass" if not still_exists else "fail",
            "describe_success": desc_result['success'],
        }

    return verify


def run_command(cmd, timeout=30):
    """
    Run a command and capture output and status.
    
    Returns:
        dict: {'success': bool, 'exit_code': int, 'stdout': str, 'stderr': str, 'error': str}
    """
    result = {
        'success': False,
        'exit_code': None,
        'stdout': '',
        'stderr': '',
        'error': ''
    }
    
    try:
        process = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=_emulator_env(),
            executable='/bin/bash'
        )
        
        result['exit_code'] = process.returncode
        result['stdout'] = process.stdout
        result['stderr'] = process.stderr
        result['success'] = process.returncode == 0
        
    except subprocess.TimeoutExpired:
        result['error'] = f'Command timed out after {timeout}s'
    except Exception as e:
        result['error'] = str(e)
    
    return result


def check_emulator_health(endpoint_url, timeout=10, retry=3):
    """
    Check if emulator is running and healthy.
    """
    import urllib.request
    import urllib.error

    for attempt in range(retry):
        try:
            req = urllib.request.Request(endpoint_url)
            urllib.request.urlopen(req, timeout=timeout)
            return True
        except urllib.error.HTTPError:
            # Any HTTP error (400, 404, etc.) means the server is reachable
            return True
        except (urllib.error.URLError, OSError):
            time.sleep(2)

    return False


def save_checkpoint(results, checkpoint_file):
    """Save results to checkpoint file."""
    with open(checkpoint_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def run_evaluation(script_file, checkpoint_file='eval_results_emulator.json',
                   start_from=0, limit=None, endpoint_url='http://localhost:5003',
                   lifecycle=False):
    """
    Run evaluation of commands from bash script.
    
    Args:
        script_file: Path to bash script with commands
        checkpoint_file: Path to save results JSON
        start_from: Command index to start from (for resuming)
        limit: Max number of commands to run (None = all)
        endpoint_url: Endpoint URL for the emulator (used for health check)
    """
    # Parse commands (list of (label_or_none, cmd))
    print(f"Parsing commands from: {script_file}")
    commands = parse_bash_script(script_file)
    print(f"Total commands to evaluate: {len(commands)}\n")
    
    if len(commands) == 0:
        print("No commands found in script.")
        return
    
    # Check emulator health
    print(f"Checking emulator health at {endpoint_url}...")
    if not check_emulator_health(endpoint_url):
        print(f"✗ Emulator is not responding at {endpoint_url}")
        print("  Please ensure the emulator is running before starting evaluation.")
        print("  Start it with: python3 main.py")
        sys.exit(1)
    print("✓ Emulator is healthy\n")
    
    # Load existing results if resuming
    start_time = time.time()
    results = {
        'script_file': str(script_file),
        'endpoint_url': endpoint_url,
        'total_commands': len(commands),
        'started_at': datetime.now().isoformat(),
        'commands': {}
    }
    
    if start_from > 0 and Path(checkpoint_file).exists():
        print(f"Resuming from command index {start_from}...")
        with open(checkpoint_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
        # Preserve original start time if resuming
        if 'started_at' in results:
            start_time_str = results['started_at']
            start_time = datetime.fromisoformat(start_time_str).timestamp()
    
    # Main evaluation loop (apply limit if set)
    end_idx = len(commands) if limit is None else min(start_from + limit, len(commands))
    if limit:
        print(f"Running first {limit} commands (indices {start_from} to {end_idx - 1})\n")

    # ID registry for bundled lifecycle tests: {prefix: real_id}
    id_registry = {}
    prev_lifecycle_file = None

    for idx in range(start_from, end_idx):
        label, cmd = commands[idx]

        # Reset ID registry when entering a new lifecycle file
        if lifecycle and label and label.startswith("lifecycle-file:"):
            current_file = label
            if current_file != prev_lifecycle_file:
                id_registry = {}
                prev_lifecycle_file = current_file
                print(f"\n{'─'*80}")
                print(f"⟳ Lifecycle test: {current_file[len('lifecycle-file:'):]}")
                print(f"{'─'*80}")

        # Replace example IDs with real ones from the registry
        original_cmd = cmd
        if lifecycle and id_registry:
            cmd = _replace_ids_in_command(cmd, id_registry)
            if cmd != original_cmd:
                print(f"  ↻ ID replaced: {cmd[:120]}{'...' if len(cmd) > 120 else ''}")

        print(f"\n{'='*80}")
        print(f"Command {idx + 1}/{len(commands)}")
        if label:
            print(f"[label: {label}]")
        print(f"{'='*80}")
        print(f"Command: {cmd[:100]}{'...' if len(cmd) > 100 else ''}")

        # Run the command
        print(f"  → Running command...", flush=True)
        cmd_result = run_command(cmd, timeout=30)
        
        # Custom success check for JSON/XML mismatch
        # AWS CLI fails if it receives JSON instead of XML, but we consider it success if the JSON is valid and not an error
        is_success = cmd_result['success']
        if not is_success and cmd_result['exit_code'] == 255 and "invalid XML" in cmd_result['stderr']:
            output = cmd_result['stderr']
            
            # Look for b'{...}' pattern which is how AWS CLI dumps the response body
            start_marker = "b'{"
            end_marker = "}'"
            
            start_idx = output.find(start_marker)
            if start_idx != -1:
                # Find the end marker after start_marker
                # We use rfind from the end, but limiting to reasonably close to end of string if needed
                # But simple logic: find matching closing brace quote
                # Ideally we want the last }'
                end_idx = output.rfind(end_marker)
                
                if end_idx != -1 and end_idx > start_idx:
                    # Extract the content inside b'{...}'
                    # start_marker is 3 chars: b ' {
                    # We want to extract { ... }
                    # So from start_idx + 2 to end_idx + 1 (to include })
                    json_bytes_repr = output[start_idx + 2 : end_idx + 1]
                    
                    try:
                        # AWS CLI output is repr(bytes), so newlines are escaped as \n
                        # quotes might be escaped? json.loads handles escaped quotes inside strings
                        # But we need to convert literal \n to actual newlines
                        json_str = json_bytes_repr.replace("\\n", "\n")
                        
                        response = json.loads(json_str)
                        # If response doesn't contain "Error" (or Error is inside ResponseMetadata which we don't have), it's likely success
                        # Also check for lower case "error" just in case
                        if "Error" not in response and "error" not in response:
                            is_success = True
                            cmd_result['success'] = True
                            cmd_result['note'] = "Marked success despite XML parse error (valid JSON received)"
                    except Exception:
                        pass

        # Print result summary
        if is_success:
            print(f"  ✓ Success (exit code: {cmd_result['exit_code']})")
            if cmd_result.get('note'):
                print(f"    Note: {cmd_result['note']}")
        else:
            print(f"  ✗ Failed (exit code: {cmd_result['exit_code']})")
            if cmd_result['error']:
                print(f"    Error: {cmd_result['error']}")
            if cmd_result['stderr']:
                stderr_preview = cmd_result['stderr'][:200]
                print(f"    Stderr: {stderr_preview}{'...' if len(cmd_result['stderr']) > 200 else ''}")
        
        # Track resource IDs from successful commands for ID replacement
        if lifecycle and is_success:
            new_ids = _extract_ids_from_response(cmd_result)
            if new_ids:
                for prefix, real_id in new_ids.items():
                    old = id_registry.get(prefix)
                    id_registry[prefix] = real_id
                    if old and old != real_id:
                        print(f"  ✎ Updated {prefix}* → {real_id} (was {old})")
                    elif not old:
                        print(f"  ✎ Registered {prefix}* → {real_id}")

        # Lifecycle verification: after create/delete, describe to verify state
        lifecycle_result = None
        if lifecycle:
            lifecycle_result = run_lifecycle_verify(cmd, cmd_result, is_success)
            if lifecycle_result:
                status_icon = "✓" if lifecycle_result["status"] == "pass" else ("⊘" if lifecycle_result["status"] == "skip" else "✗")
                vtype = lifecycle_result["type"].replace("_verify", "").replace("_", " ")
                print(f"  {status_icon} lifecycle {vtype}: {lifecycle_result['status']}", end="")
                if lifecycle_result["status"] == "skip":
                    print(f" ({lifecycle_result.get('reason', '')})")
                else:
                    rid = lifecycle_result.get("resource_id", "")
                    fc = lifecycle_result.get("fields_checked", 0)
                    fm = lifecycle_result.get("fields_matched", 0)
                    if fc > 0:
                        print(f" (resource_id={rid}, fields: {fm}/{fc})")
                        for fr in lifecycle_result.get("field_results", []):
                            icon = "✓" if fr["match"] else "✗"
                            print(f"    {icon} {fr['field']}: expected={fr['expected']!r}, actual={fr['actual']!r}")
                    else:
                        print(f" (resource_id={rid})")

        # Save result
        entry = {
            'command': cmd,
            'index': idx,
            'label': label,
            'result': cmd_result,
            'lifecycle_verify': lifecycle_result,
            'timestamp': datetime.now().isoformat(),
        }
        if lifecycle and cmd != original_cmd:
            entry['original_command'] = original_cmd
        results['commands'][idx] = entry
        
        # Save checkpoint
        print(f"  → Saving checkpoint...", flush=True)
        save_checkpoint(results, checkpoint_file)
    
    # Calculate total runtime
    end_time = time.time()
    total_runtime = end_time - start_time
    
    # Final summary
    print(f"\n\n{'='*80}")
    print("EVALUATION COMPLETE")
    print(f"{'='*80}")
    
    total = len(results['commands'])
    successful = sum(1 for r in results['commands'].values() 
                     if r.get('result') and r['result']['success'])
    failed = sum(1 for r in results['commands'].values() 
                 if r.get('result') and not r['result']['success'])
    skipped = total - successful - failed
    
    print(f"Total commands: {total}")
    print(f"Successful: {successful} ({successful/total*100:.1f}%)")
    print(f"Failed: {failed} ({failed/total*100:.1f}%)")
    if skipped > 0:
        print(f"Skipped: {skipped}")
    print(f"Total runtime: {total_runtime:.2f}s ({total_runtime/60:.2f} minutes)")

    # Lifecycle verification summary
    if lifecycle:
        lc_results = [r.get('lifecycle_verify') for r in results['commands'].values()
                      if r.get('lifecycle_verify')]
        if lc_results:
            lc_pass = sum(1 for r in lc_results if r['status'] == 'pass')
            lc_fail = sum(1 for r in lc_results if r['status'] == 'fail')
            lc_skip = sum(1 for r in lc_results if r['status'] == 'skip')
            create_results = [r for r in lc_results if r['type'] == 'create_verify']
            modify_results = [r for r in lc_results if r['type'] == 'modify_verify']
            delete_results = [r for r in lc_results if r['type'] == 'delete_verify']
            create_pass = sum(1 for r in create_results if r['status'] == 'pass')
            create_fail = sum(1 for r in create_results if r['status'] == 'fail')
            modify_pass = sum(1 for r in modify_results if r['status'] == 'pass')
            modify_fail = sum(1 for r in modify_results if r['status'] == 'fail')
            modify_skip = sum(1 for r in modify_results if r['status'] == 'skip')
            delete_pass = sum(1 for r in delete_results if r['status'] == 'pass')
            delete_fail = sum(1 for r in delete_results if r['status'] == 'fail')
            print(f"\nLifecycle verification:")
            print(f"  Total: {len(lc_results)} (pass: {lc_pass}, fail: {lc_fail}, skip: {lc_skip})")
            print(f"  Create→Describe:  {create_pass} pass, {create_fail} fail")
            print(f"  Modify→Describe:  {modify_pass} pass, {modify_fail} fail, {modify_skip} skip")
            print(f"  Delete→Describe:  {delete_pass} pass, {delete_fail} fail")

            # Field-level accuracy
            all_field_results = []
            create_field_results = []
            modify_field_results = []
            for r in lc_results:
                frs = r.get('field_results', [])
                all_field_results.extend(frs)
                if r['type'] == 'create_verify':
                    create_field_results.extend(frs)
                elif r['type'] == 'modify_verify':
                    modify_field_results.extend(frs)

            total_fields = len(all_field_results)
            matched_fields = sum(1 for f in all_field_results if f['match'])
            create_fc = len(create_field_results)
            create_fm = sum(1 for f in create_field_results if f['match'])
            modify_fc = len(modify_field_results)
            modify_fm = sum(1 for f in modify_field_results if f['match'])

            if total_fields > 0:
                print(f"\n  Field-level accuracy:")
                print(f"    Total:  {matched_fields}/{total_fields} fields correct ({matched_fields/total_fields*100:.1f}%)")
                if create_fc > 0:
                    print(f"    Create: {create_fm}/{create_fc} ({create_fm/create_fc*100:.1f}%)")
                if modify_fc > 0:
                    print(f"    Modify: {modify_fm}/{modify_fc} ({modify_fm/modify_fc*100:.1f}%)")

                mismatches = [f for f in all_field_results if not f['match']]
                if mismatches:
                    print(f"    Mismatches ({len(mismatches)}):")
                    for f in mismatches:
                        print(f"      ✗ {f['field']}: expected={f['expected']!r}, actual={f['actual']!r}")

            if lc_fail > 0:
                print(f"\n  Failed verifications:")
                for r in results['commands'].values():
                    lv = r.get('lifecycle_verify')
                    if lv and lv['status'] == 'fail':
                        fc = lv.get('fields_checked', 0)
                        fm = lv.get('fields_matched', 0)
                        extra = f", fields={fm}/{fc}" if fc > 0 else ""
                        print(f"    ✗ {lv['type']}: {r['command'][:70]}...{extra}")

    # Summary by label if present
    by_label = {}
    for r in results['commands'].values():
        lab = r.get('label') or 'unlabeled'
        by_label.setdefault(lab, {'total': 0, 'success': 0, 'fail': 0})
        by_label[lab]['total'] += 1
        if r.get('result', {}).get('success'):
            by_label[lab]['success'] += 1
        else:
            by_label[lab]['fail'] += 1
    if any(k != 'unlabeled' for k in by_label):
        print("\nBy label:")
        for lab in sorted(by_label.keys()):
            s = by_label[lab]
            print(f"  {lab}: {s['success']}/{s['total']} ok, {s['fail']} failed")
    print(f"\nResults saved to: {checkpoint_file}")
    
    results['completed_at'] = datetime.now().isoformat()
    results['total_runtime_seconds'] = round(total_runtime, 2)
    summary = {
        'total': total,
        'successful': successful,
        'failed': failed,
        'skipped': skipped,
        'total_runtime_seconds': round(total_runtime, 2)
    }
    if lifecycle:
        lc_all = [r.get('lifecycle_verify') for r in results['commands'].values()
                  if r.get('lifecycle_verify')]
        all_frs = []
        for r in lc_all:
            all_frs.extend(r.get('field_results', []))
        summary['lifecycle'] = {
            'total': len(lc_all),
            'pass': sum(1 for r in lc_all if r['status'] == 'pass'),
            'fail': sum(1 for r in lc_all if r['status'] == 'fail'),
            'skip': sum(1 for r in lc_all if r['status'] == 'skip'),
            'fields_total': len(all_frs),
            'fields_matched': sum(1 for f in all_frs if f['match']),
            'field_accuracy': round(sum(1 for f in all_frs if f['match']) / len(all_frs) * 100, 1) if all_frs else 0,
        }
    results['summary'] = summary
    save_checkpoint(results, checkpoint_file)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Evaluate AWS CLI commands against EC2 Emulator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run evaluation on all commands
  python eval_emulator.py test.sh
  
  # Resume from command index 10
  python eval_emulator.py test.sh --start-from 10
  
  # Use custom endpoint
  python eval_emulator.py test.sh --endpoint http://localhost:5003
  
  # Use custom checkpoint file
  python eval_emulator.py test.sh --checkpoint my_results.json

  # Run only first 20 commands
  python eval_emulator.py test.sh --limit 20
        """
    )
    
    parser.add_argument(
        'script_file',
        help='Bash script file containing commands to evaluate'
    )
    
    parser.add_argument(
        '--checkpoint',
        '-c',
        default='eval_results_emulator.json',
        help='Checkpoint file to save results (default: eval_results_emulator.json)'
    )
    
    parser.add_argument(
        '--start-from',
        '-s',
        type=int,
        default=0,
        help='Command index to start from (for resuming, default: 0)'
    )
    
    parser.add_argument(
        '--limit',
        '-n',
        type=int,
        default=None,
        help='Max number of commands to run (default: all)'
    )
    
    parser.add_argument(
        '--endpoint',
        '-e',
        default='http://localhost:5003',
        help='Emulator endpoint URL (default: http://localhost:5003)'
    )

    parser.add_argument(
        '--lifecycle',
        action='store_true',
        help='Enable lifecycle verification: after create/modify/delete, run describe to verify state'
    )
    
    args = parser.parse_args()

    # Check if script file exists
    script_path = Path(args.script_file)
    if not script_path.exists():
        print(f"Error: Script file not found: {script_path}", file=sys.stderr)
        sys.exit(1)

    # Run evaluation
    try:
        run_evaluation(script_path, args.checkpoint, args.start_from,
                      args.limit, args.endpoint, lifecycle=args.lifecycle)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Progress has been saved.")
        sys.exit(0)


if __name__ == "__main__":
    main()
