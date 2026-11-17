#!/usr/bin/env python3
"""Generate proper bundled lifecycle RST test files.

Each lifecycle RST bundles create → describe → (modify →) delete in order,
using consistent example IDs so eval_emulator.py's ID replacement logic can
chain them together at runtime.
"""
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RST_DIR = SCRIPT_DIR / "cli" / "ec2"

# ---------------------------------------------------------------------------
# Lifecycle test definitions
# Each entry: (filename_stem, list_of_steps)
# A step is (title, description_text, subcommand, command_args, output_or_none)
# ---------------------------------------------------------------------------

LIFECYCLE_TESTS = [
    # ──────────────────────────────────────────
    # 1. Address (Elastic IP)
    # ──────────────────────────────────────────
    ("address-lifecycle", [
        ("To allocate an Elastic IP address",
         "allocate-address", "allocates an Elastic IP address",
         "",
         '{\n    "PublicIp": "70.224.234.241",\n    "AllocationId": "eipalloc-01435ba59eEXAMPLE",\n    "PublicIpv4Pool": "amazon",\n    "NetworkBorderGroup": "us-east-1",\n    "Domain": "vpc"\n}'),
        ("To describe the Elastic IP address",
         "describe-addresses", "retrieves details about the allocated Elastic IP address",
         "--allocation-ids eipalloc-01435ba59eEXAMPLE",
         None),
        ("To release the Elastic IP address",
         "release-address", "releases the Elastic IP address",
         "--allocation-id eipalloc-01435ba59eEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 2. Capacity Reservation
    # ──────────────────────────────────────────
    ("capacity-reservation-lifecycle", [
        ("To create a Capacity Reservation",
         "create-capacity-reservation", "creates a Capacity Reservation",
         "--availability-zone us-east-1a --instance-type t2.medium --instance-platform Linux/UNIX --instance-count 3",
         '{\n    "CapacityReservation": {\n        "CapacityReservationId": "cr-1234abcd56EXAMPLE",\n        "InstanceType": "t2.medium",\n        "InstancePlatform": "Linux/UNIX",\n        "AvailabilityZone": "us-east-1a",\n        "TotalInstanceCount": 3,\n        "AvailableInstanceCount": 3,\n        "State": "active"\n    }\n}'),
        ("To describe the Capacity Reservation",
         "describe-capacity-reservations", "retrieves details about the Capacity Reservation",
         "--capacity-reservation-ids cr-1234abcd56EXAMPLE",
         None),
        ("To modify the Capacity Reservation",
         "modify-capacity-reservation", "modifies the instance count of the Capacity Reservation",
         "--capacity-reservation-id cr-1234abcd56EXAMPLE --instance-count 5",
         None),
        ("To describe the Capacity Reservation after modification",
         "describe-capacity-reservations", "verifies the modification was applied",
         "--capacity-reservation-ids cr-1234abcd56EXAMPLE",
         None),
        ("To cancel the Capacity Reservation",
         "cancel-capacity-reservation", "cancels the Capacity Reservation",
         "--capacity-reservation-id cr-1234abcd56EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 3. Carrier Gateway
    # ──────────────────────────────────────────
    ("carrier-gateway-lifecycle", [
        ("To create a VPC for the carrier gateway",
         "create-vpc", "creates a VPC as a prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a carrier gateway",
         "create-carrier-gateway", "creates a carrier gateway in the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         '{\n    "CarrierGateway": {\n        "CarrierGatewayId": "cagw-0465cdEXAMPLE1111",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "State": "available"\n    }\n}'),
        ("To describe the carrier gateway",
         "describe-carrier-gateways", "retrieves details about the carrier gateway",
         "--carrier-gateway-ids cagw-0465cdEXAMPLE1111",
         None),
        ("To delete the carrier gateway",
         "delete-carrier-gateway", "deletes the carrier gateway",
         "--carrier-gateway-id cagw-0465cdEXAMPLE1111",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 4. DHCP Options
    # ──────────────────────────────────────────
    ("dhcp-options-lifecycle", [
        ("To create DHCP options",
         "create-dhcp-options", "creates a DHCP options set",
         '--dhcp-configuration "Key=domain-name-servers,Values=10.2.5.1,10.2.5.2" "Key=domain-name,Values=example.com"',
         '{\n    "DhcpOptions": {\n        "DhcpOptionsId": "dopt-0a1b2c3d4eEXAMPLE",\n        "DhcpConfigurations": [\n            {"Key": "domain-name-servers", "Values": [{"Value": "10.2.5.1"}, {"Value": "10.2.5.2"}]},\n            {"Key": "domain-name", "Values": [{"Value": "example.com"}]}\n        ]\n    }\n}'),
        ("To describe the DHCP options",
         "describe-dhcp-options", "retrieves details about the DHCP options",
         "--dhcp-options-ids dopt-0a1b2c3d4eEXAMPLE",
         None),
        ("To delete the DHCP options",
         "delete-dhcp-options", "deletes the DHCP options set",
         "--dhcp-options-id dopt-0a1b2c3d4eEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 5. Fleet (using inline args, not file://)
    # ──────────────────────────────────────────
    ("fleet-lifecycle", [
        ("To create a launch template for the fleet",
         "create-launch-template", "creates a launch template as prerequisite",
         '--launch-template-name lifecycle-fleet-lt --launch-template-data \'{"ImageId":"ami-0abcdef1234567890","InstanceType":"t2.micro"}\'',
         '{\n    "LaunchTemplate": {\n        "LaunchTemplateId": "lt-0e8c754449EXAMPLE",\n        "LaunchTemplateName": "lifecycle-fleet-lt",\n        "LatestVersionNumber": 1\n    }\n}'),
        ("To create an EC2 Fleet",
         "create-fleet", "creates an EC2 Fleet",
         '--type instant --launch-template-configs \'LaunchTemplateSpecification={LaunchTemplateId=lt-0e8c754449EXAMPLE,Version=1}\' --target-capacity-specification TotalTargetCapacity=1,DefaultTargetCapacityType=on-demand',
         '{\n    "FleetId": "fleet-12a34b55EXAMPLE",\n    "Instances": []\n}'),
        ("To describe the fleet",
         "describe-fleets", "retrieves details about the fleet",
         "--fleet-ids fleet-12a34b55EXAMPLE",
         None),
        ("To modify the fleet target capacity",
         "modify-fleet", "modifies the fleet target capacity",
         "--fleet-id fleet-12a34b55EXAMPLE --target-capacity-specification TotalTargetCapacity=2",
         None),
        ("To delete the fleet",
         "delete-fleets", "deletes the fleet",
         "--fleet-ids fleet-12a34b55EXAMPLE --terminate-instances",
         None),
        ("To delete the launch template",
         "delete-launch-template", "cleans up the launch template",
         "--launch-template-id lt-0e8c754449EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 6. Flow Logs
    # ──────────────────────────────────────────
    ("flow-log-lifecycle", [
        ("To create a VPC for flow logs",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a flow log for the VPC",
         "create-flow-logs", "creates a flow log that captures all traffic for the VPC",
         "--resource-type VPC --resource-ids vpc-0a60eb65b4EXAMPLE --traffic-type ALL --log-destination-type cloud-watch-logs --log-group-name my-flow-logs",
         '{\n    "ClientToken": "abc123",\n    "FlowLogIds": ["fl-11223344556677889"],\n    "Unsuccessful": []\n}'),
        ("To describe the flow log",
         "describe-flow-logs", "retrieves details about the flow log",
         "--flow-log-ids fl-11223344556677889",
         None),
        ("To delete the flow log",
         "delete-flow-logs", "deletes the flow log",
         "--flow-log-ids fl-11223344556677889",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 7. Dedicated Host
    # ──────────────────────────────────────────
    ("host-lifecycle", [
        ("To allocate a Dedicated Host",
         "allocate-hosts", "allocates a Dedicated Host",
         "--instance-type m5.large --availability-zone us-east-1a --quantity 1",
         '{\n    "HostIds": ["h-0029d6e3cacf1b3da"]\n}'),
        ("To describe the Dedicated Host",
         "describe-hosts", "retrieves details about the Dedicated Host",
         "--host-ids h-0029d6e3cacf1b3da",
         None),
        ("To modify the Dedicated Host",
         "modify-hosts", "enables auto-placement on the host",
         "--host-ids h-0029d6e3cacf1b3da --auto-placement on",
         None),
        ("To describe the Dedicated Host after modification",
         "describe-hosts", "verifies auto-placement is enabled",
         "--host-ids h-0029d6e3cacf1b3da",
         None),
        ("To release the Dedicated Host",
         "release-hosts", "releases the Dedicated Host",
         "--host-ids h-0029d6e3cacf1b3da",
         None),
    ]),

    # ──────────────────────────────────────────
    # 8. AMI (Image)
    # ──────────────────────────────────────────
    ("image-lifecycle", [
        ("To register an AMI",
         "register-image", "registers an AMI",
         "--name lifecycle-test-image --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}",
         '{\n    "ImageId": "ami-1234567890EXAMPLE"\n}'),
        ("To describe the AMI",
         "describe-images", "retrieves details about the AMI",
         "--image-ids ami-1234567890EXAMPLE",
         None),
        ("To modify the AMI description",
         "modify-image-attribute", "modifies the description of the AMI",
         "--image-id ami-1234567890EXAMPLE --description \"Updated lifecycle image\"",
         None),
        ("To describe the AMI after modification",
         "describe-images", "verifies the description was updated",
         "--image-ids ami-1234567890EXAMPLE",
         None),
        ("To deregister the AMI",
         "deregister-image", "deregisters the AMI",
         "--image-id ami-1234567890EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 9. Instance
    # ──────────────────────────────────────────
    ("instance-lifecycle", [
        ("To register an AMI for the instance",
         "register-image", "registers a minimal AMI as prerequisite",
         "--name lifecycle-instance-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}",
         '{\n    "ImageId": "ami-1234567890EXAMPLE"\n}'),
        ("To launch an instance",
         "run-instances", "launches an EC2 instance",
         "--image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1",
         '{\n    "Instances": [\n        {\n            "InstanceId": "i-1234567890abcdef0",\n            "InstanceType": "t2.micro",\n            "State": {"Name": "pending", "Code": 0},\n            "ImageId": "ami-1234567890EXAMPLE"\n        }\n    ]\n}'),
        ("To describe the instance",
         "describe-instances", "retrieves details about the launched instance",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To modify the instance type",
         "modify-instance-attribute", "changes the instance type (instance must be stopped first)",
         "--instance-id i-1234567890abcdef0 --instance-type \"{\\\"Value\\\": \\\"t2.small\\\"}\"",
         None),
        ("To describe the instance after modification",
         "describe-instances", "verifies the instance type change",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To terminate the instance",
         "terminate-instances", "terminates the instance",
         "--instance-ids i-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # 10. Internet Gateway
    # ──────────────────────────────────────────
    ("internet-gateway-lifecycle", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create an internet gateway",
         "create-internet-gateway", "creates an internet gateway",
         "",
         '{\n    "InternetGateway": {\n        "InternetGatewayId": "igw-0d0fb496b3EXAMPLE",\n        "Attachments": [],\n        "Tags": []\n    }\n}'),
        ("To describe the internet gateway",
         "describe-internet-gateways", "retrieves details about the internet gateway",
         "--internet-gateway-ids igw-0d0fb496b3EXAMPLE",
         None),
        ("To attach the internet gateway to the VPC",
         "attach-internet-gateway", "attaches the internet gateway to the VPC",
         "--internet-gateway-id igw-0d0fb496b3EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
        ("To detach the internet gateway from the VPC",
         "detach-internet-gateway", "detaches the internet gateway",
         "--internet-gateway-id igw-0d0fb496b3EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
        ("To delete the internet gateway",
         "delete-internet-gateway", "deletes the internet gateway",
         "--internet-gateway-id igw-0d0fb496b3EXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 11. Key Pair
    # ──────────────────────────────────────────
    ("key-pair-lifecycle", [
        ("To create a key pair",
         "create-key-pair", "creates a key pair",
         "--key-name lifecycle-test-key --key-type rsa",
         '{\n    "KeyFingerprint": "1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f",\n    "KeyMaterial": "-----BEGIN RSA PRIVATE KEY-----\\nEXAMPLE...\\n-----END RSA PRIVATE KEY-----",\n    "KeyName": "lifecycle-test-key",\n    "KeyPairId": "key-0d4fb2e3caEXAMPLE"\n}'),
        ("To describe the key pair",
         "describe-key-pairs", "retrieves details about the key pair",
         "--key-names lifecycle-test-key",
         None),
        ("To delete the key pair",
         "delete-key-pair", "deletes the key pair",
         "--key-name lifecycle-test-key",
         None),
    ]),

    # ──────────────────────────────────────────
    # 12. Instance Connect Endpoint
    # ──────────────────────────────────────────
    ("instance-connect-endpoint-lifecycle", [
        ("To create a VPC and subnet",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet as prerequisite",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.1.0/24"\n    }\n}'),
        ("To create an Instance Connect Endpoint",
         "create-instance-connect-endpoint", "creates an Instance Connect Endpoint in the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE",
         '{\n    "InstanceConnectEndpoint": {\n        "InstanceConnectEndpointId": "eice-03f5e49b83EXAMPLE",\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "State": "create-complete"\n    }\n}'),
        ("To describe the Instance Connect Endpoint",
         "describe-instance-connect-endpoints", "retrieves details about the endpoint",
         "--instance-connect-endpoint-ids eice-03f5e49b83EXAMPLE",
         None),
        ("To delete the Instance Connect Endpoint",
         "delete-instance-connect-endpoint", "deletes the endpoint",
         "--instance-connect-endpoint-id eice-03f5e49b83EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 13. Instance Event Window
    # ──────────────────────────────────────────
    ("instance-event-window-lifecycle", [
        ("To create an instance event window",
         "create-instance-event-window", "creates an instance event window",
         "--time-range StartWeekDay=monday,StartHour=2,EndWeekDay=wednesday,EndHour=8 --tag-specifications 'ResourceType=instance-event-window,Tags=[{Key=Name,Value=lifecycle-test}]' --name lifecycle-event-window",
         '{\n    "InstanceEventWindow": {\n        "InstanceEventWindowId": "iew-0abcdef1234567890",\n        "Name": "lifecycle-event-window",\n        "TimeRanges": [{"StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8}],\n        "State": "active"\n    }\n}'),
        ("To describe the instance event window",
         "describe-instance-event-windows", "retrieves details about the event window",
         "--instance-event-window-ids iew-0abcdef1234567890",
         None),
        ("To modify the instance event window",
         "modify-instance-event-window", "changes the time range",
         "--instance-event-window-id iew-0abcdef1234567890 --time-range StartWeekDay=tuesday,StartHour=4,EndWeekDay=thursday,EndHour=10",
         None),
        ("To describe the instance event window after modification",
         "describe-instance-event-windows", "verifies the time range was updated",
         "--instance-event-window-ids iew-0abcdef1234567890",
         None),
        ("To delete the instance event window",
         "delete-instance-event-window", "deletes the event window",
         "--instance-event-window-id iew-0abcdef1234567890",
         None),
    ]),

    # ──────────────────────────────────────────
    # 14. IPAM
    # ──────────────────────────────────────────
    ("ipam-lifecycle", [
        ("To create an IPAM",
         "create-ipam", "creates an IP Address Manager",
         "--description 'Lifecycle test IPAM' --operating-regions RegionName=us-east-1 --tag-specifications 'ResourceType=ipam,Tags=[{Key=Name,Value=lifecycle-ipam}]'",
         '{\n    "Ipam": {\n        "IpamId": "ipam-08440e7a3aEXAMPLE",\n        "Description": "Lifecycle test IPAM",\n        "State": "create-complete"\n    }\n}'),
        ("To describe the IPAM",
         "describe-ipams", "retrieves details about the IPAM",
         "--ipam-ids ipam-08440e7a3aEXAMPLE",
         None),
        ("To modify the IPAM",
         "modify-ipam", "adds an operating region to the IPAM",
         "--ipam-id ipam-08440e7a3aEXAMPLE --add-operating-regions RegionName=us-west-2",
         None),
        ("To describe the IPAM after modification",
         "describe-ipams", "verifies the operating region was added",
         "--ipam-ids ipam-08440e7a3aEXAMPLE",
         None),
        ("To delete the IPAM",
         "delete-ipam", "deletes the IPAM",
         "--ipam-id ipam-08440e7a3aEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 15. IPAM Pool
    # ──────────────────────────────────────────
    ("ipam-pool-lifecycle", [
        ("To create an IPAM for the pool",
         "create-ipam", "creates an IPAM as prerequisite",
         "--description 'Pool prerequisite' --operating-regions RegionName=us-east-1",
         '{\n    "Ipam": {\n        "IpamId": "ipam-08440e7a3aEXAMPLE",\n        "PublicDefaultScopeId": "ipam-scope-02fc38cd4cEXAMPLE",\n        "PrivateDefaultScopeId": "ipam-scope-02fc38cd4cEXAMPLE"\n    }\n}'),
        ("To create an IPAM pool",
         "create-ipam-pool", "creates an IPAM pool under the default scope",
         "--ipam-scope-id ipam-scope-02fc38cd4cEXAMPLE --address-family ipv4 --allocation-min-netmask-length 16 --allocation-max-netmask-length 26",
         '{\n    "IpamPool": {\n        "IpamPoolId": "ipam-pool-0533048da7EXAMPLE",\n        "IpamScopeId": "ipam-scope-02fc38cd4cEXAMPLE",\n        "AddressFamily": "ipv4",\n        "State": "create-complete"\n    }\n}'),
        ("To describe the IPAM pool",
         "describe-ipam-pools", "retrieves details about the IPAM pool",
         "--ipam-pool-ids ipam-pool-0533048da7EXAMPLE",
         None),
        ("To modify the IPAM pool",
         "modify-ipam-pool", "modifies allocation settings on the pool",
         "--ipam-pool-id ipam-pool-0533048da7EXAMPLE --allocation-min-netmask-length 14",
         None),
        ("To delete the IPAM pool",
         "delete-ipam-pool", "deletes the IPAM pool",
         "--ipam-pool-id ipam-pool-0533048da7EXAMPLE",
         None),
        ("To delete the IPAM",
         "delete-ipam", "cleans up the IPAM",
         "--ipam-id ipam-08440e7a3aEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 16. IPAM Resource Discovery
    # ──────────────────────────────────────────
    ("ipam-resource-discovery-lifecycle", [
        ("To create an IPAM resource discovery",
         "create-ipam-resource-discovery", "creates an IPAM resource discovery",
         "--description 'Lifecycle test discovery' --operating-regions RegionName=us-east-1 --tag-specifications 'ResourceType=ipam-resource-discovery,Tags=[{Key=Name,Value=lifecycle-disc}]'",
         '{\n    "IpamResourceDiscovery": {\n        "IpamResourceDiscoveryId": "ipam-res-disco-0e39761475EXAMPLE",\n        "Description": "Lifecycle test discovery",\n        "State": "create-complete"\n    }\n}'),
        ("To describe the resource discovery",
         "describe-ipam-resource-discoveries", "retrieves details about the discovery",
         "--ipam-resource-discovery-ids ipam-res-disco-0e39761475EXAMPLE",
         None),
        ("To modify the resource discovery",
         "modify-ipam-resource-discovery", "adds an operating region",
         "--ipam-resource-discovery-id ipam-res-disco-0e39761475EXAMPLE --add-operating-regions RegionName=us-west-1",
         None),
        ("To delete the resource discovery",
         "delete-ipam-resource-discovery", "deletes the resource discovery",
         "--ipam-resource-discovery-id ipam-res-disco-0e39761475EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 17. IPAM Scope
    # ──────────────────────────────────────────
    ("ipam-scope-lifecycle", [
        ("To create an IPAM for the scope",
         "create-ipam", "creates an IPAM as prerequisite",
         "--description 'Scope prerequisite' --operating-regions RegionName=us-east-1",
         '{\n    "Ipam": {\n        "IpamId": "ipam-08440e7a3aEXAMPLE"\n    }\n}'),
        ("To create an IPAM scope",
         "create-ipam-scope", "creates an IPAM scope",
         "--ipam-id ipam-08440e7a3aEXAMPLE --description 'Lifecycle test scope'",
         '{\n    "IpamScope": {\n        "IpamScopeId": "ipam-scope-01c1ebab2bEXAMPLE",\n        "IpamId": "ipam-08440e7a3aEXAMPLE",\n        "Description": "Lifecycle test scope",\n        "State": "create-complete"\n    }\n}'),
        ("To describe the IPAM scope",
         "describe-ipam-scopes", "retrieves details about the scope",
         "--ipam-scope-ids ipam-scope-01c1ebab2bEXAMPLE",
         None),
        ("To modify the IPAM scope",
         "modify-ipam-scope", "updates the description",
         "--ipam-scope-id ipam-scope-01c1ebab2bEXAMPLE --description 'Updated scope'",
         None),
        ("To delete the IPAM scope",
         "delete-ipam-scope", "deletes the IPAM scope",
         "--ipam-scope-id ipam-scope-01c1ebab2bEXAMPLE",
         None),
        ("To delete the IPAM",
         "delete-ipam", "cleans up the IPAM",
         "--ipam-id ipam-08440e7a3aEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 18. Managed Prefix List
    # ──────────────────────────────────────────
    ("managed-prefix-list-lifecycle", [
        ("To create a managed prefix list",
         "create-managed-prefix-list", "creates a managed prefix list",
         "--address-family IPv4 --max-entries 10 --entries Cidr=10.0.0.0/16,Description=vpc-a --prefix-list-name lifecycle-prefix-list",
         '{\n    "PrefixList": {\n        "PrefixListId": "pl-0123456abcEXAMPLE",\n        "AddressFamily": "IPv4",\n        "State": "create-complete",\n        "PrefixListName": "lifecycle-prefix-list",\n        "MaxEntries": 10,\n        "Version": 1\n    }\n}'),
        ("To describe the prefix list",
         "describe-managed-prefix-lists", "retrieves details about the prefix list",
         "--prefix-list-ids pl-0123456abcEXAMPLE",
         None),
        ("To modify the prefix list",
         "modify-managed-prefix-list", "adds an entry to the prefix list",
         "--prefix-list-id pl-0123456abcEXAMPLE --add-entries Cidr=10.2.0.0/16,Description=vpc-b --current-version 1",
         None),
        ("To describe the prefix list after modification",
         "describe-managed-prefix-lists", "verifies the entry was added",
         "--prefix-list-ids pl-0123456abcEXAMPLE",
         None),
        ("To delete the prefix list",
         "delete-managed-prefix-list", "deletes the prefix list",
         "--prefix-list-id pl-0123456abcEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 19. NAT Gateway
    # ──────────────────────────────────────────
    ("nat-gateway-lifecycle", [
        ("To create a VPC for the NAT gateway",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet as prerequisite",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.1.0/24"\n    }\n}'),
        ("To create a private NAT gateway",
         "create-nat-gateway", "creates a private NAT gateway in the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE --connectivity-type private",
         '{\n    "NatGateway": {\n        "NatGatewayId": "nat-0c61bf8a12EXAMPLE",\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "State": "available",\n        "ConnectivityType": "private"\n    }\n}'),
        ("To describe the NAT gateway",
         "describe-nat-gateways", "retrieves details about the NAT gateway",
         "--nat-gateway-ids nat-0c61bf8a12EXAMPLE",
         None),
        ("To delete the NAT gateway",
         "delete-nat-gateway", "deletes the NAT gateway",
         "--nat-gateway-id nat-0c61bf8a12EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 20. Network ACL
    # ──────────────────────────────────────────
    ("network-acl-lifecycle", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a network ACL",
         "create-network-acl", "creates a network ACL in the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         '{\n    "NetworkAcl": {\n        "NetworkAclId": "acl-5fb85d36EXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "IsDefault": false\n    }\n}'),
        ("To describe the network ACL",
         "describe-network-acls", "retrieves details about the network ACL",
         "--network-acl-ids acl-5fb85d36EXAMPLE",
         None),
        ("To delete the network ACL",
         "delete-network-acl", "deletes the network ACL",
         "--network-acl-id acl-5fb85d36EXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 21. Network Insights Path
    # ──────────────────────────────────────────
    ("network-insights-path-lifecycle", [
        ("To create a VPC and internet gateway",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "State": "available"\n    }\n}'),
        ("To create an internet gateway",
         "create-internet-gateway", "creates an IGW as prerequisite",
         "",
         '{\n    "InternetGateway": {\n        "InternetGatewayId": "igw-0d0fb496b3EXAMPLE"\n    }\n}'),
        ("To create a network insights path",
         "create-network-insights-path", "creates a path from IGW to VPC",
         "--source igw-0d0fb496b3EXAMPLE --destination vpc-0a60eb65b4EXAMPLE --protocol TCP",
         '{\n    "NetworkInsightsPath": {\n        "NetworkInsightsPathId": "nip-0b26f224f1EXAMPLE",\n        "Source": "igw-0d0fb496b3EXAMPLE",\n        "Destination": "vpc-0a60eb65b4EXAMPLE",\n        "Protocol": "tcp"\n    }\n}'),
        ("To describe the network insights path",
         "describe-network-insights-paths", "retrieves details about the path",
         "--network-insights-path-ids nip-0b26f224f1EXAMPLE",
         None),
        ("To delete the network insights path",
         "delete-network-insights-path", "deletes the path",
         "--network-insights-path-id nip-0b26f224f1EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 22. Network Insights Access Scope
    # ──────────────────────────────────────────
    ("network-insights-access-scope-lifecycle", [
        ("To create a network insights access scope",
         "create-network-insights-access-scope", "creates an access scope for network analysis",
         "--match-paths 'Source={ResourceStatement={ResourceTypes=[AWS::EC2::NetworkInterface]}}'",
         '{\n    "NetworkInsightsAccessScope": {\n        "NetworkInsightsAccessScopeId": "nis-123456789aEXAMPLE"\n    },\n    "NetworkInsightsAccessScopeContent": {\n        "NetworkInsightsAccessScopeId": "nis-123456789aEXAMPLE"\n    }\n}'),
        ("To describe the access scope",
         "describe-network-insights-access-scopes", "retrieves details about the access scope",
         "--network-insights-access-scope-ids nis-123456789aEXAMPLE",
         None),
        ("To delete the access scope",
         "delete-network-insights-access-scope", "deletes the access scope",
         "--network-insights-access-scope-id nis-123456789aEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 23. Route Table
    # ──────────────────────────────────────────
    ("route-table-lifecycle", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a route table",
         "create-route-table", "creates a route table in the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         '{\n    "RouteTable": {\n        "RouteTableId": "rtb-22574640EXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "Routes": [{"DestinationCidrBlock": "10.0.0.0/16", "GatewayId": "local", "State": "active"}]\n    }\n}'),
        ("To describe the route table",
         "describe-route-tables", "retrieves details about the route table",
         "--route-table-ids rtb-22574640EXAMPLE",
         None),
        ("To delete the route table",
         "delete-route-table", "deletes the route table",
         "--route-table-id rtb-22574640EXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 24. Security Group
    # ──────────────────────────────────────────
    ("security-group-lifecycle", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a security group",
         "create-security-group", "creates a security group in the VPC",
         "--group-name lifecycle-sg --description \"Lifecycle test security group\" --vpc-id vpc-0a60eb65b4EXAMPLE",
         '{\n    "GroupId": "sg-1234567890abcdef0"\n}'),
        ("To describe the security group",
         "describe-security-groups", "retrieves details about the security group",
         "--group-ids sg-1234567890abcdef0",
         None),
        ("To authorize inbound SSH access",
         "authorize-security-group-ingress", "adds an inbound rule for SSH",
         "--group-id sg-1234567890abcdef0 --protocol tcp --port 22 --cidr 203.0.113.0/24",
         None),
        ("To describe the security group after rule addition",
         "describe-security-groups", "verifies the SSH rule was added",
         "--group-ids sg-1234567890abcdef0",
         None),
        ("To delete the security group",
         "delete-security-group", "deletes the security group",
         "--group-id sg-1234567890abcdef0",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 25. Spot Datafeed Subscription
    # ──────────────────────────────────────────
    ("spot-datafeed-subscription-lifecycle", [
        ("To create a Spot datafeed subscription",
         "create-spot-datafeed-subscription", "creates a Spot datafeed subscription",
         "--bucket amzn-s3-demo-bucket --prefix spot-data-feed",
         '{\n    "SpotDatafeedSubscription": {\n        "Bucket": "amzn-s3-demo-bucket",\n        "OwnerId": "123456789012",\n        "Prefix": "spot-data-feed",\n        "State": "Active"\n    }\n}'),
        ("To describe the Spot datafeed subscription",
         "describe-spot-datafeed-subscription", "retrieves details about the subscription",
         "",
         None),
        ("To delete the Spot datafeed subscription",
         "delete-spot-datafeed-subscription", "deletes the subscription",
         "",
         None),
    ]),

    # ──────────────────────────────────────────
    # 26. Subnet
    # ──────────────────────────────────────────
    ("subnet-lifecycle", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet in the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=lifecycle-subnet}]'",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.1.0/24",\n        "State": "available"\n    }\n}'),
        ("To describe the subnet",
         "describe-subnets", "retrieves details about the subnet",
         "--subnet-ids subnet-0250c25a1fEXAMPLE",
         None),
        ("To modify the subnet to enable public IPs",
         "modify-subnet-attribute", "enables auto-assign public IP on the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE --map-public-ip-on-launch",
         None),
        ("To describe the subnet after modification",
         "describe-subnets", "verifies public IP assignment is enabled",
         "--subnet-ids subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the subnet",
         "delete-subnet", "deletes the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 27. Tag
    # ──────────────────────────────────────────
    ("tag-lifecycle", [
        ("To create a VPC to tag",
         "create-vpc", "creates a VPC as the tagging target",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create tags on the VPC",
         "create-tags", "adds Name and Environment tags to the VPC",
         "--resources vpc-0a60eb65b4EXAMPLE --tags Key=Name,Value=lifecycle-vpc Key=Environment,Value=test",
         None),
        ("To describe tags",
         "describe-tags", "retrieves tags for the VPC",
         "--filters \"Name=resource-id,Values=vpc-0a60eb65b4EXAMPLE\"",
         None),
        ("To delete the Environment tag",
         "delete-tags", "removes the Environment tag from the VPC",
         "--resources vpc-0a60eb65b4EXAMPLE --tags Key=Environment",
         None),
        ("To describe tags after deletion",
         "describe-tags", "verifies the Environment tag was removed",
         "--filters \"Name=resource-id,Values=vpc-0a60eb65b4EXAMPLE\"",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 28. Traffic Mirror Filter
    # ──────────────────────────────────────────
    ("traffic-mirror-filter-lifecycle", [
        ("To create a traffic mirror filter",
         "create-traffic-mirror-filter", "creates a traffic mirror filter",
         "--description 'Lifecycle TCP Filter'",
         '{\n    "TrafficMirrorFilter": {\n        "TrafficMirrorFilterId": "tmf-0be0b25fcdEXAMPLE",\n        "Description": "Lifecycle TCP Filter"\n    }\n}'),
        ("To describe the traffic mirror filter",
         "describe-traffic-mirror-filters", "retrieves details about the filter",
         "--traffic-mirror-filter-ids tmf-0be0b25fcdEXAMPLE",
         None),
        ("To delete the traffic mirror filter",
         "delete-traffic-mirror-filter", "deletes the filter",
         "--traffic-mirror-filter-id tmf-0be0b25fcdEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 29. Traffic Mirror Session
    # ──────────────────────────────────────────
    ("traffic-mirror-session-lifecycle", [
        ("To create a traffic mirror filter",
         "create-traffic-mirror-filter", "creates a filter as prerequisite",
         "--description 'Session filter'",
         '{\n    "TrafficMirrorFilter": {\n        "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE"\n    }\n}'),
        ("To create a traffic mirror target",
         "create-traffic-mirror-target", "creates a target as prerequisite",
         "--description 'Session target' --network-interface-id eni-070203f901EXAMPLE",
         '{\n    "TrafficMirrorTarget": {\n        "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",\n        "NetworkInterfaceId": "eni-070203f901EXAMPLE"\n    }\n}'),
        ("To create a traffic mirror session",
         "create-traffic-mirror-session", "creates a traffic mirror session",
         "--traffic-mirror-target-id tmt-07f75d8feeEXAMPLE --network-interface-id eni-070203f901EXAMPLE --session-number 1 --traffic-mirror-filter-id tmf-04812ff784EXAMPLE",
         '{\n    "TrafficMirrorSession": {\n        "TrafficMirrorSessionId": "tms-0af3141ce5EXAMPLE",\n        "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",\n        "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE",\n        "SessionNumber": 1\n    }\n}'),
        ("To describe the traffic mirror session",
         "describe-traffic-mirror-sessions", "retrieves details about the session",
         "--traffic-mirror-session-ids tms-0af3141ce5EXAMPLE",
         None),
        ("To modify the traffic mirror session",
         "modify-traffic-mirror-session", "changes the session description",
         "--traffic-mirror-session-id tms-0af3141ce5EXAMPLE --description \"Updated session\"",
         None),
        ("To delete the traffic mirror session",
         "delete-traffic-mirror-session", "deletes the session",
         "--traffic-mirror-session-id tms-0af3141ce5EXAMPLE",
         None),
        ("To delete the traffic mirror target",
         "delete-traffic-mirror-target", "cleans up the target",
         "--traffic-mirror-target-id tmt-07f75d8feeEXAMPLE",
         None),
        ("To delete the traffic mirror filter",
         "delete-traffic-mirror-filter", "cleans up the filter",
         "--traffic-mirror-filter-id tmf-04812ff784EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 30. Traffic Mirror Target
    # ──────────────────────────────────────────
    ("traffic-mirror-target-lifecycle", [
        ("To create a traffic mirror target",
         "create-traffic-mirror-target", "creates a traffic mirror target using a network interface",
         "--description 'Lifecycle target' --network-interface-id eni-070203f901EXAMPLE",
         '{\n    "TrafficMirrorTarget": {\n        "TrafficMirrorTargetId": "tmt-060f48ce9EXAMPLE",\n        "NetworkInterfaceId": "eni-070203f901EXAMPLE",\n        "Description": "Lifecycle target"\n    }\n}'),
        ("To describe the traffic mirror target",
         "describe-traffic-mirror-targets", "retrieves details about the target",
         "--traffic-mirror-target-ids tmt-060f48ce9EXAMPLE",
         None),
        ("To delete the traffic mirror target",
         "delete-traffic-mirror-target", "deletes the target",
         "--traffic-mirror-target-id tmt-060f48ce9EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 31. Transit Gateway
    # ──────────────────────────────────────────
    ("transit-gateway-lifecycle", [
        ("To create a transit gateway",
         "create-transit-gateway", "creates a transit gateway",
         "--description MyTGW --options AmazonSideAsn=64516,AutoAcceptSharedAttachments=enable,DefaultRouteTableAssociation=enable,DefaultRouteTablePropagation=enable,VpnEcmpSupport=enable,DnsSupport=enable",
         '{\n    "TransitGateway": {\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE",\n        "State": "available",\n        "Description": "MyTGW",\n        "Options": {\n            "AmazonSideAsn": 64516,\n            "AutoAcceptSharedAttachments": "enable",\n            "DnsSupport": "enable"\n        }\n    }\n}'),
        ("To describe the transit gateway",
         "describe-transit-gateways", "retrieves details about the transit gateway",
         "--transit-gateway-ids tgw-0262a0e521EXAMPLE",
         None),
        ("To modify the transit gateway",
         "modify-transit-gateway", "disables VPN ECMP support",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE --options VpnEcmpSupport=disable",
         None),
        ("To describe the transit gateway after modification",
         "describe-transit-gateways", "verifies the modification",
         "--transit-gateway-ids tgw-0262a0e521EXAMPLE",
         None),
        ("To delete the transit gateway",
         "delete-transit-gateway", "deletes the transit gateway",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 32. Transit Gateway Connect
    # ──────────────────────────────────────────
    ("transit-gateway-connect-lifecycle", [
        ("To create a transit gateway",
         "create-transit-gateway", "creates a TGW as prerequisite",
         "--description ConnectTGW",
         '{\n    "TransitGateway": {\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE",\n        "State": "available"\n    }\n}'),
        ("To create a VPC attachment",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE"\n    }\n}'),
        ("To create a subnet for the attachment",
         "create-subnet", "creates a subnet",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE"\n    }\n}'),
        ("To create a transit gateway VPC attachment",
         "create-transit-gateway-vpc-attachment", "creates a VPC attachment for the connect",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE --subnet-ids subnet-0250c25a1fEXAMPLE",
         '{\n    "TransitGatewayVpcAttachment": {\n        "TransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE",\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE"\n    }\n}'),
        ("To create a transit gateway connect",
         "create-transit-gateway-connect", "creates a Connect attachment using GRE",
         "--transport-transit-gateway-attachment-id tgw-attach-0a89069f57EXAMPLE --options Protocol=gre",
         '{\n    "TransitGatewayConnect": {\n        "TransitGatewayAttachmentId": "tgw-attach-037012e5dcEXAMPLE",\n        "TransportTransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE"\n    }\n}'),
        ("To describe the transit gateway connect",
         "describe-transit-gateway-connects", "retrieves details about the connect",
         "--transit-gateway-attachment-ids tgw-attach-037012e5dcEXAMPLE",
         None),
        ("To delete the transit gateway connect",
         "delete-transit-gateway-connect", "deletes the connect",
         "--transit-gateway-attachment-id tgw-attach-037012e5dcEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 33. Transit Gateway Connect Peer
    # ──────────────────────────────────────────
    ("transit-gateway-connect-peer-lifecycle", [
        ("To create a transit gateway connect peer",
         "create-transit-gateway-connect-peer", "creates a Connect peer",
         "--transit-gateway-attachment-id tgw-attach-0f0927767cEXAMPLE --peer-address 172.31.1.11 --inside-cidr-blocks 169.254.6.0/29",
         '{\n    "TransitGatewayConnectPeer": {\n        "TransitGatewayConnectPeerId": "tgw-connect-peer-0666adbac4EXAMPLE",\n        "TransitGatewayAttachmentId": "tgw-attach-0f0927767cEXAMPLE"\n    }\n}'),
        ("To describe the connect peer",
         "describe-transit-gateway-connect-peers", "retrieves details about the peer",
         "--transit-gateway-connect-peer-ids tgw-connect-peer-0666adbac4EXAMPLE",
         None),
        ("To delete the connect peer",
         "delete-transit-gateway-connect-peer", "deletes the peer",
         "--transit-gateway-connect-peer-id tgw-connect-peer-0666adbac4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 34. Transit Gateway Multicast Domain
    # ──────────────────────────────────────────
    ("transit-gateway-multicast-domain-lifecycle", [
        ("To create a transit gateway",
         "create-transit-gateway", "creates a TGW with multicast enabled",
         "--description MulticastTGW --options MulticastSupport=enable",
         '{\n    "TransitGateway": {\n        "TransitGatewayId": "tgw-0bf0bffefaEXAMPLE"\n    }\n}'),
        ("To create a transit gateway multicast domain",
         "create-transit-gateway-multicast-domain", "creates a multicast domain",
         "--transit-gateway-id tgw-0bf0bffefaEXAMPLE --options StaticSourcesSupport=disable,Igmpv2Support=enable",
         '{\n    "TransitGatewayMulticastDomain": {\n        "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef7EXAMPLE",\n        "TransitGatewayId": "tgw-0bf0bffefaEXAMPLE"\n    }\n}'),
        ("To describe the multicast domain",
         "describe-transit-gateway-multicast-domains", "retrieves details",
         "--transit-gateway-multicast-domain-ids tgw-mcast-domain-0c4905cef7EXAMPLE",
         None),
        ("To delete the multicast domain",
         "delete-transit-gateway-multicast-domain", "deletes the multicast domain",
         "--transit-gateway-multicast-domain-id tgw-mcast-domain-0c4905cef7EXAMPLE",
         None),
        ("To delete the transit gateway",
         "delete-transit-gateway", "cleans up the TGW",
         "--transit-gateway-id tgw-0bf0bffefaEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 35. Transit Gateway Peering Attachment
    # ──────────────────────────────────────────
    ("transit-gateway-peering-attachment-lifecycle", [
        ("To create a transit gateway peering attachment",
         "create-transit-gateway-peering-attachment", "creates a peering attachment",
         "--transit-gateway-id tgw-123abc05e04123abc --peer-transit-gateway-id tgw-11223344aabbcc112 --peer-account-id 123456789012 --peer-region us-east-2",
         '{\n    "TransitGatewayPeeringAttachment": {\n        "TransitGatewayAttachmentId": "tgw-attach-4455667788EXAMPLE",\n        "RequesterTgwInfo": {"TransitGatewayId": "tgw-123abc05e04123abc"},\n        "AccepterTgwInfo": {"TransitGatewayId": "tgw-11223344aabbcc112"},\n        "State": "pendingAcceptance"\n    }\n}'),
        ("To describe the peering attachment",
         "describe-transit-gateway-peering-attachments", "retrieves details",
         "--transit-gateway-attachment-ids tgw-attach-4455667788EXAMPLE",
         None),
        ("To delete the peering attachment",
         "delete-transit-gateway-peering-attachment", "deletes the peering attachment",
         "--transit-gateway-attachment-id tgw-attach-4455667788EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 36. Transit Gateway Policy Table
    # ──────────────────────────────────────────
    ("transit-gateway-policy-table-lifecycle", [
        ("To create a transit gateway",
         "create-transit-gateway", "creates a TGW as prerequisite",
         "--description PolicyTGW",
         '{\n    "TransitGateway": {\n        "TransitGatewayId": "tgw-067f8505c18f0bd6e"\n    }\n}'),
        ("To create a transit gateway policy table",
         "create-transit-gateway-policy-table", "creates a policy table",
         "--transit-gateway-id tgw-067f8505c18f0bd6e",
         '{\n    "TransitGatewayPolicyTable": {\n        "TransitGatewayPolicyTableId": "tgw-ptb-0a16f134b7EXAMPLE",\n        "TransitGatewayId": "tgw-067f8505c18f0bd6e"\n    }\n}'),
        ("To describe the policy table",
         "describe-transit-gateway-policy-tables", "retrieves details",
         "--transit-gateway-policy-table-ids tgw-ptb-0a16f134b7EXAMPLE",
         None),
        ("To delete the policy table",
         "delete-transit-gateway-policy-table", "deletes the policy table",
         "--transit-gateway-policy-table-id tgw-ptb-0a16f134b7EXAMPLE",
         None),
        ("To delete the transit gateway",
         "delete-transit-gateway", "cleans up the TGW",
         "--transit-gateway-id tgw-067f8505c18f0bd6e",
         None),
    ]),

    # ──────────────────────────────────────────
    # 37. Transit Gateway Route Table
    # ──────────────────────────────────────────
    ("transit-gateway-route-table-lifecycle", [
        ("To create a transit gateway",
         "create-transit-gateway", "creates a TGW as prerequisite",
         "--description RouteTGW",
         '{\n    "TransitGateway": {\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE"\n    }\n}'),
        ("To create a transit gateway route table",
         "create-transit-gateway-route-table", "creates a route table",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE",
         '{\n    "TransitGatewayRouteTable": {\n        "TransitGatewayRouteTableId": "tgw-rtb-0b6f6aaa01EXAMPLE",\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE"\n    }\n}'),
        ("To describe the route table",
         "describe-transit-gateway-route-tables", "retrieves details",
         "--transit-gateway-route-table-ids tgw-rtb-0b6f6aaa01EXAMPLE",
         None),
        ("To delete the route table",
         "delete-transit-gateway-route-table", "deletes the route table",
         "--transit-gateway-route-table-id tgw-rtb-0b6f6aaa01EXAMPLE",
         None),
        ("To delete the transit gateway",
         "delete-transit-gateway", "cleans up the TGW",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 38. Transit Gateway VPC Attachment
    # ──────────────────────────────────────────
    ("transit-gateway-vpc-attachment-lifecycle", [
        ("To create a transit gateway",
         "create-transit-gateway", "creates a TGW as prerequisite",
         "--description VpcAttachTGW",
         '{\n    "TransitGateway": {\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE"\n    }\n}'),
        ("To create a VPC",
         "create-vpc", "creates a VPC",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE"\n    }\n}'),
        ("To create a transit gateway VPC attachment",
         "create-transit-gateway-vpc-attachment", "creates a VPC attachment",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE --subnet-ids subnet-0250c25a1fEXAMPLE",
         '{\n    "TransitGatewayVpcAttachment": {\n        "TransitGatewayAttachmentId": "tgw-attach-0d2c54bdbEXAMPLE",\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE"\n    }\n}'),
        ("To describe the VPC attachment",
         "describe-transit-gateway-vpc-attachments", "retrieves details",
         "--transit-gateway-attachment-ids tgw-attach-0d2c54bdbEXAMPLE",
         None),
        ("To delete the VPC attachment",
         "delete-transit-gateway-vpc-attachment", "deletes the attachment",
         "--transit-gateway-attachment-id tgw-attach-0d2c54bdbEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 39-43. Verified Access (instance, trust-provider, group, endpoint, log)
    # verified-access-log is already GOOD, skip it here
    # ──────────────────────────────────────────
    ("verified-access-instance-lifecycle", [
        ("To create a Verified Access instance",
         "create-verified-access-instance", "creates a Verified Access instance",
         "--tag-specifications 'ResourceType=verified-access-instance,Tags=[{Key=Name,Value=lifecycle-va-instance}]'",
         '{\n    "VerifiedAccessInstance": {\n        "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE",\n        "CreationTime": "2023-01-01T00:00:00",\n        "LastUpdatedTime": "2023-01-01T00:00:00"\n    }\n}'),
        ("To describe the Verified Access instance",
         "describe-verified-access-instances", "retrieves details",
         "--verified-access-instance-ids vai-0ce000c0b7EXAMPLE",
         None),
        ("To modify the Verified Access instance",
         "modify-verified-access-instance", "updates the description",
         "--verified-access-instance-id vai-0ce000c0b7EXAMPLE --description 'Updated lifecycle instance'",
         None),
        ("To describe after modification",
         "describe-verified-access-instances", "verifies the update",
         "--verified-access-instance-ids vai-0ce000c0b7EXAMPLE",
         None),
        ("To delete the Verified Access instance",
         "delete-verified-access-instance", "deletes the instance",
         "--verified-access-instance-id vai-0ce000c0b7EXAMPLE",
         None),
    ]),

    ("verified-access-trust-provider-lifecycle", [
        ("To create a Verified Access trust provider",
         "create-verified-access-trust-provider", "creates a trust provider",
         "--trust-provider-type user --user-trust-provider-type iam-identity-center --policy-reference-name idc --tag-specifications 'ResourceType=verified-access-trust-provider,Tags=[{Key=Name,Value=lifecycle-tp}]'",
         '{\n    "VerifiedAccessTrustProvider": {\n        "VerifiedAccessTrustProviderId": "vatp-0bb32de759EXAMPLE",\n        "TrustProviderType": "user",\n        "UserTrustProviderType": "iam-identity-center",\n        "PolicyReferenceName": "idc"\n    }\n}'),
        ("To describe the trust provider",
         "describe-verified-access-trust-providers", "retrieves details",
         "--verified-access-trust-provider-ids vatp-0bb32de759EXAMPLE",
         None),
        ("To modify the trust provider",
         "modify-verified-access-trust-provider", "updates the description",
         "--verified-access-trust-provider-id vatp-0bb32de759EXAMPLE --description 'Updated trust provider'",
         None),
        ("To delete the trust provider",
         "delete-verified-access-trust-provider", "deletes the trust provider",
         "--verified-access-trust-provider-id vatp-0bb32de759EXAMPLE",
         None),
    ]),

    ("verified-access-group-lifecycle", [
        ("To create a Verified Access instance for the group",
         "create-verified-access-instance", "creates a VA instance as prerequisite",
         "--description 'Group prerequisite'",
         '{\n    "VerifiedAccessInstance": {\n        "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE"\n    }\n}'),
        ("To create a Verified Access group",
         "create-verified-access-group", "creates a Verified Access group",
         "--verified-access-instance-id vai-0ce000c0b7EXAMPLE --tag-specifications 'ResourceType=verified-access-group,Tags=[{Key=Name,Value=lifecycle-va-group}]'",
         '{\n    "VerifiedAccessGroup": {\n        "VerifiedAccessGroupId": "vagr-0dbe967bafEXAMPLE",\n        "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE"\n    }\n}'),
        ("To describe the Verified Access group",
         "describe-verified-access-groups", "retrieves details",
         "--verified-access-group-ids vagr-0dbe967bafEXAMPLE",
         None),
        ("To modify the Verified Access group",
         "modify-verified-access-group", "updates the description",
         "--verified-access-group-id vagr-0dbe967bafEXAMPLE --description 'Updated group'",
         None),
        ("To delete the Verified Access group",
         "delete-verified-access-group", "deletes the group",
         "--verified-access-group-id vagr-0dbe967bafEXAMPLE",
         None),
        ("To delete the Verified Access instance",
         "delete-verified-access-instance", "cleans up the VA instance",
         "--verified-access-instance-id vai-0ce000c0b7EXAMPLE",
         None),
    ]),

    ("verified-access-endpoint-lifecycle", [
        ("To create a Verified Access instance",
         "create-verified-access-instance", "creates a VA instance",
         "--description 'Endpoint prerequisite'",
         '{\n    "VerifiedAccessInstance": {\n        "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE"\n    }\n}'),
        ("To create a Verified Access group",
         "create-verified-access-group", "creates a VA group",
         "--verified-access-instance-id vai-0ce000c0b7EXAMPLE",
         '{\n    "VerifiedAccessGroup": {\n        "VerifiedAccessGroupId": "vagr-0dbe967bafEXAMPLE"\n    }\n}'),
        ("To create a Verified Access endpoint",
         "create-verified-access-endpoint", "creates a Verified Access endpoint",
         "--verified-access-group-id vagr-0dbe967bafEXAMPLE --endpoint-type network-interface --attachment-type vpc --domain-certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/eb065ea0EXAMPLE --application-domain example.com --endpoint-domain-prefix my-app --security-group-ids sg-1234567890abcdef0 --network-interface-options NetworkInterfaceId=eni-070203f901EXAMPLE,Protocol=https,Port=443",
         '{\n    "VerifiedAccessEndpoint": {\n        "VerifiedAccessEndpointId": "vae-066fac616dEXAMPLE",\n        "VerifiedAccessGroupId": "vagr-0dbe967bafEXAMPLE"\n    }\n}'),
        ("To describe the endpoint",
         "describe-verified-access-endpoints", "retrieves details",
         "--verified-access-endpoint-ids vae-066fac616dEXAMPLE",
         None),
        ("To modify the endpoint",
         "modify-verified-access-endpoint", "updates the description",
         "--verified-access-endpoint-id vae-066fac616dEXAMPLE --description 'Updated endpoint'",
         None),
        ("To delete the endpoint",
         "delete-verified-access-endpoint", "deletes the endpoint",
         "--verified-access-endpoint-id vae-066fac616dEXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 44. VPC Endpoint Service Configuration
    # ──────────────────────────────────────────
    ("vpc-endpoint-service-configuration-lifecycle", [
        ("To create a VPC endpoint service configuration",
         "create-vpc-endpoint-service-configuration", "creates a VPC endpoint service",
         "--network-load-balancer-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532 --acceptance-required",
         '{\n    "ServiceConfiguration": {\n        "ServiceId": "vpce-svc-03d5ebb7d9EXAMPLE",\n        "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-03d5ebb7d9EXAMPLE",\n        "AcceptanceRequired": true\n    }\n}'),
        ("To describe the service configuration",
         "describe-vpc-endpoint-service-configurations", "retrieves details",
         "--service-ids vpce-svc-03d5ebb7d9EXAMPLE",
         None),
        ("To modify the service configuration",
         "modify-vpc-endpoint-service-configuration", "disables acceptance requirement",
         "--service-id vpce-svc-03d5ebb7d9EXAMPLE --no-acceptance-required",
         None),
        ("To describe after modification",
         "describe-vpc-endpoint-service-configurations", "verifies the change",
         "--service-ids vpce-svc-03d5ebb7d9EXAMPLE",
         None),
        ("To delete the service configuration",
         "delete-vpc-endpoint-service-configurations", "deletes the service",
         "--service-ids vpce-svc-03d5ebb7d9EXAMPLE",
         None),
    ]),

    # ==================================================================
    # MODIFY VARIANTS — same create/delete, different modify parameter
    # ==================================================================

    # ──────────────────────────────────────────
    # V1. Volume – modify size only
    # ──────────────────────────────────────────
    ("volume-lifecycle-v2", [
        ("To create a gp3 EBS volume",
         "create-volume", "creates a 100 GiB gp3 volume",
         "--volume-type gp3 --size 100 --availability-zone us-east-1a",
         '{\n    "AvailabilityZone": "us-east-1a",\n    "Encrypted": false,\n    "VolumeType": "gp3",\n    "VolumeId": "vol-1234567890abcdef0",\n    "State": "creating",\n    "Iops": 3000,\n    "Size": 100\n}'),
        ("To describe the volume",
         "describe-volumes", "retrieves details about the volume",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To modify the volume size only",
         "modify-volume", "increases the volume to 150 GiB",
         "--volume-id vol-1234567890abcdef0 --size 150",
         None),
        ("To describe the volume after modification",
         "describe-volumes", "verifies the size change",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To delete the volume",
         "delete-volume", "deletes the volume",
         "--volume-id vol-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # V2. Volume – modify type only
    # ──────────────────────────────────────────
    ("volume-lifecycle-v3", [
        ("To create a gp3 EBS volume",
         "create-volume", "creates a 100 GiB gp3 volume",
         "--volume-type gp3 --size 100 --availability-zone us-east-1a",
         '{\n    "AvailabilityZone": "us-east-1a",\n    "Encrypted": false,\n    "VolumeType": "gp3",\n    "VolumeId": "vol-1234567890abcdef0",\n    "State": "creating",\n    "Iops": 3000,\n    "Size": 100\n}'),
        ("To describe the volume",
         "describe-volumes", "retrieves details about the volume",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To modify the volume type only",
         "modify-volume", "changes the volume type to gp2",
         "--volume-id vol-1234567890abcdef0 --volume-type gp2",
         None),
        ("To describe the volume after modification",
         "describe-volumes", "verifies the type change",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To delete the volume",
         "delete-volume", "deletes the volume",
         "--volume-id vol-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # V4. Volume – modify IOPS only (gp3)
    # ──────────────────────────────────────────
    ("volume-lifecycle-v4", [
        ("To create a gp3 EBS volume",
         "create-volume", "creates a 100 GiB gp3 volume",
         "--volume-type gp3 --size 100 --availability-zone us-east-1a",
         '{\n    "AvailabilityZone": "us-east-1a",\n    "Encrypted": false,\n    "VolumeType": "gp3",\n    "VolumeId": "vol-1234567890abcdef0",\n    "State": "creating",\n    "Iops": 3000,\n    "Size": 100\n}'),
        ("To describe the volume",
         "describe-volumes", "retrieves details about the volume",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To modify the volume IOPS only",
         "modify-volume", "raises provisioned IOPS on gp3",
         "--volume-id vol-1234567890abcdef0 --iops 6000",
         None),
        ("To describe the volume after modification",
         "describe-volumes", "verifies the IOPS change",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To delete the volume",
         "delete-volume", "deletes the volume",
         "--volume-id vol-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # V5. Volume – modify throughput only (gp3)
    # ──────────────────────────────────────────
    ("volume-lifecycle-v5", [
        ("To create a gp3 EBS volume",
         "create-volume", "creates a 100 GiB gp3 volume",
         "--volume-type gp3 --size 100 --availability-zone us-east-1a",
         '{\n    "AvailabilityZone": "us-east-1a",\n    "Encrypted": false,\n    "VolumeType": "gp3",\n    "VolumeId": "vol-1234567890abcdef0",\n    "State": "creating",\n    "Iops": 3000,\n    "Size": 100\n}'),
        ("To describe the volume",
         "describe-volumes", "retrieves details about the volume",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To modify the volume throughput only",
         "modify-volume", "sets gp3 throughput (MiB/s)",
         "--volume-id vol-1234567890abcdef0 --throughput 500",
         None),
        ("To describe the volume after modification",
         "describe-volumes", "verifies the throughput change",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To delete the volume",
         "delete-volume", "deletes the volume",
         "--volume-id vol-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # V6. Volume – modify to io2 with IOPS
    # ──────────────────────────────────────────
    ("volume-lifecycle-v6", [
        ("To create a gp3 EBS volume",
         "create-volume", "creates a 100 GiB gp3 volume",
         "--volume-type gp3 --size 100 --availability-zone us-east-1a",
         '{\n    "AvailabilityZone": "us-east-1a",\n    "Encrypted": false,\n    "VolumeType": "gp3",\n    "VolumeId": "vol-1234567890abcdef0",\n    "State": "creating",\n    "Iops": 3000,\n    "Size": 100\n}'),
        ("To describe the volume",
         "describe-volumes", "retrieves details about the volume",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To modify the volume to io2",
         "modify-volume", "converts to Provisioned IOPS SSD (io2)",
         "--volume-id vol-1234567890abcdef0 --volume-type io2 --iops 3000 --size 100",
         None),
        ("To describe the volume after modification",
         "describe-volumes", "verifies io2 and IOPS",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To delete the volume",
         "delete-volume", "deletes the volume",
         "--volume-id vol-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # V3. Instance – modify source/dest check
    # ──────────────────────────────────────────
    ("instance-lifecycle-v2", [
        ("To register an AMI for the instance",
         "register-image", "registers a minimal AMI as prerequisite",
         "--name lifecycle-instance-v2-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}",
         '{\n    "ImageId": "ami-1234567890EXAMPLE"\n}'),
        ("To launch an instance",
         "run-instances", "launches an EC2 instance",
         "--image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1",
         '{\n    "Instances": [\n        {\n            "InstanceId": "i-1234567890abcdef0",\n            "InstanceType": "t2.micro",\n            "State": {"Name": "pending", "Code": 0},\n            "ImageId": "ami-1234567890EXAMPLE"\n        }\n    ]\n}'),
        ("To describe the instance",
         "describe-instances", "retrieves details about the launched instance",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To disable source/dest check on the instance",
         "modify-instance-attribute", "disables the source/destination check",
         "--instance-id i-1234567890abcdef0 --source-dest-check \"{\\\"Value\\\": false}\"",
         None),
        ("To describe the instance after modification",
         "describe-instances", "verifies the source/dest check was disabled",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To terminate the instance",
         "terminate-instances", "terminates the instance",
         "--instance-ids i-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # V4. Host – modify host-recovery
    # ──────────────────────────────────────────
    ("host-lifecycle-v2", [
        ("To allocate a Dedicated Host",
         "allocate-hosts", "allocates a Dedicated Host",
         "--instance-type m5.large --availability-zone us-east-1a --quantity 1",
         '{\n    "HostIds": ["h-0029d6e3cacf1b3da"]\n}'),
        ("To describe the Dedicated Host",
         "describe-hosts", "retrieves details about the Dedicated Host",
         "--host-ids h-0029d6e3cacf1b3da",
         None),
        ("To enable host recovery",
         "modify-hosts", "enables host recovery on the Dedicated Host",
         "--host-ids h-0029d6e3cacf1b3da --host-recovery on",
         None),
        ("To describe the Dedicated Host after modification",
         "describe-hosts", "verifies host recovery is enabled",
         "--host-ids h-0029d6e3cacf1b3da",
         None),
        ("To release the Dedicated Host",
         "release-hosts", "releases the Dedicated Host",
         "--host-ids h-0029d6e3cacf1b3da",
         None),
    ]),

    # ──────────────────────────────────────────
    # V5. Capacity Reservation – modify end-date-type
    # ──────────────────────────────────────────
    ("capacity-reservation-lifecycle-v2", [
        ("To create a Capacity Reservation",
         "create-capacity-reservation", "creates a Capacity Reservation",
         "--availability-zone us-east-1a --instance-type t2.medium --instance-platform Linux/UNIX --instance-count 3",
         '{\n    "CapacityReservation": {\n        "CapacityReservationId": "cr-1234abcd56EXAMPLE",\n        "InstanceType": "t2.medium",\n        "InstancePlatform": "Linux/UNIX",\n        "AvailabilityZone": "us-east-1a",\n        "TotalInstanceCount": 3,\n        "AvailableInstanceCount": 3,\n        "State": "active"\n    }\n}'),
        ("To describe the Capacity Reservation",
         "describe-capacity-reservations", "retrieves details about the Capacity Reservation",
         "--capacity-reservation-ids cr-1234abcd56EXAMPLE",
         None),
        ("To modify the Capacity Reservation end date type",
         "modify-capacity-reservation", "changes the end date type to limited",
         "--capacity-reservation-id cr-1234abcd56EXAMPLE --end-date-type limited --end-date 2029-12-31T23:59:59Z",
         None),
        ("To describe the Capacity Reservation after modification",
         "describe-capacity-reservations", "verifies the end date type was changed",
         "--capacity-reservation-ids cr-1234abcd56EXAMPLE",
         None),
        ("To cancel the Capacity Reservation",
         "cancel-capacity-reservation", "cancels the Capacity Reservation",
         "--capacity-reservation-id cr-1234abcd56EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # V6. Image – modify launch permission
    # ──────────────────────────────────────────
    ("image-lifecycle-v2", [
        ("To register an AMI",
         "register-image", "registers an AMI",
         "--name lifecycle-image-v2 --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}",
         '{\n    "ImageId": "ami-1234567890EXAMPLE"\n}'),
        ("To describe the AMI",
         "describe-images", "retrieves details about the AMI",
         "--image-ids ami-1234567890EXAMPLE",
         None),
        ("To make the AMI public",
         "modify-image-attribute", "adds public launch permission",
         "--image-id ami-1234567890EXAMPLE --launch-permission \"Add=[{Group=all}]\"",
         None),
        ("To describe the AMI after modification",
         "describe-images", "verifies the AMI is accessible",
         "--image-ids ami-1234567890EXAMPLE",
         None),
        ("To deregister the AMI",
         "deregister-image", "deregisters the AMI",
         "--image-id ami-1234567890EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # V7. Network Interface – modify description
    # ──────────────────────────────────────────
    ("network-interface-lifecycle-v2", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet as prerequisite",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.1.0/24"\n    }\n}'),
        ("To create a network interface",
         "create-network-interface", "creates a network interface in the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE --description \"Lifecycle test ENI v2\"",
         '{\n    "NetworkInterface": {\n        "NetworkInterfaceId": "eni-e5aa89a3EXAMPLE",\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "Description": "Lifecycle test ENI v2",\n        "Status": "available"\n    }\n}'),
        ("To describe the network interface",
         "describe-network-interfaces", "retrieves details",
         "--network-interface-ids eni-e5aa89a3EXAMPLE",
         None),
        ("To modify the network interface description",
         "modify-network-interface-attribute", "changes the description of the ENI",
         "--network-interface-id eni-e5aa89a3EXAMPLE --description \"Modified ENI description\"",
         None),
        ("To describe the network interface after modification",
         "describe-network-interfaces", "verifies the description was updated",
         "--network-interface-ids eni-e5aa89a3EXAMPLE",
         None),
        ("To delete the network interface",
         "delete-network-interface", "deletes the ENI",
         "--network-interface-id eni-e5aa89a3EXAMPLE",
         None),
        ("To delete the subnet",
         "delete-subnet", "cleans up the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # V8. Network Interface – modify source/dest check
    # ──────────────────────────────────────────
    ("network-interface-lifecycle-v3", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet as prerequisite",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.1.0/24"\n    }\n}'),
        ("To create a network interface",
         "create-network-interface", "creates a network interface in the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE --description \"Lifecycle test ENI v3\"",
         '{\n    "NetworkInterface": {\n        "NetworkInterfaceId": "eni-e5aa89a3EXAMPLE",\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "Description": "Lifecycle test ENI v3",\n        "Status": "available"\n    }\n}'),
        ("To describe the network interface",
         "describe-network-interfaces", "retrieves details",
         "--network-interface-ids eni-e5aa89a3EXAMPLE",
         None),
        ("To disable source/dest check on the ENI",
         "modify-network-interface-attribute", "disables the source/destination check",
         "--network-interface-id eni-e5aa89a3EXAMPLE --no-source-dest-check",
         None),
        ("To describe the network interface after modification",
         "describe-network-interfaces", "verifies source/dest check was disabled",
         "--network-interface-ids eni-e5aa89a3EXAMPLE",
         None),
        ("To delete the network interface",
         "delete-network-interface", "deletes the ENI",
         "--network-interface-id eni-e5aa89a3EXAMPLE",
         None),
        ("To delete the subnet",
         "delete-subnet", "cleans up the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # V9. Security Group – authorize egress rule
    # ──────────────────────────────────────────
    ("security-group-lifecycle-v2", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a security group",
         "create-security-group", "creates a security group in the VPC",
         "--group-name lifecycle-sg-v2 --description \"Lifecycle v2 security group\" --vpc-id vpc-0a60eb65b4EXAMPLE",
         '{\n    "GroupId": "sg-1234567890abcdef0"\n}'),
        ("To describe the security group",
         "describe-security-groups", "retrieves details about the security group",
         "--group-ids sg-1234567890abcdef0",
         None),
        ("To authorize inbound HTTPS access",
         "authorize-security-group-ingress", "adds an inbound rule for HTTPS",
         "--group-id sg-1234567890abcdef0 --protocol tcp --port 443 --cidr 0.0.0.0/0",
         None),
        ("To describe the security group after rule addition",
         "describe-security-groups", "verifies the HTTPS rule was added",
         "--group-ids sg-1234567890abcdef0",
         None),
        ("To delete the security group",
         "delete-security-group", "deletes the security group",
         "--group-id sg-1234567890abcdef0",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # V10. VPC Endpoint Service Config – enable acceptance
    # ──────────────────────────────────────────
    ("vpc-endpoint-service-configuration-lifecycle-v2", [
        ("To create a VPC endpoint service without acceptance",
         "create-vpc-endpoint-service-configuration", "creates a VPC endpoint service without acceptance required",
         "--network-load-balancer-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532 --no-acceptance-required",
         '{\n    "ServiceConfiguration": {\n        "ServiceId": "vpce-svc-03d5ebb7d9EXAMPLE",\n        "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-03d5ebb7d9EXAMPLE",\n        "AcceptanceRequired": false\n    }\n}'),
        ("To describe the service configuration",
         "describe-vpc-endpoint-service-configurations", "retrieves details",
         "--service-ids vpce-svc-03d5ebb7d9EXAMPLE",
         None),
        ("To enable acceptance requirement",
         "modify-vpc-endpoint-service-configuration", "enables acceptance requirement",
         "--service-id vpce-svc-03d5ebb7d9EXAMPLE --acceptance-required",
         None),
        ("To describe after modification",
         "describe-vpc-endpoint-service-configurations", "verifies acceptance is now required",
         "--service-ids vpce-svc-03d5ebb7d9EXAMPLE",
         None),
        ("To delete the service configuration",
         "delete-vpc-endpoint-service-configurations", "deletes the service",
         "--service-ids vpce-svc-03d5ebb7d9EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # V11. Transit Gateway – modify description
    # ──────────────────────────────────────────
    ("transit-gateway-lifecycle-v2", [
        ("To create a transit gateway",
         "create-transit-gateway", "creates a transit gateway",
         "--description OriginalTGW",
         '{\n    "TransitGateway": {\n        "TransitGatewayId": "tgw-0262a0e521EXAMPLE",\n        "State": "available",\n        "Description": "OriginalTGW"\n    }\n}'),
        ("To describe the transit gateway",
         "describe-transit-gateways", "retrieves details about the transit gateway",
         "--transit-gateway-ids tgw-0262a0e521EXAMPLE",
         None),
        ("To modify the transit gateway description",
         "modify-transit-gateway", "updates the transit gateway description",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE --description UpdatedTGW",
         None),
        ("To describe the transit gateway after modification",
         "describe-transit-gateways", "verifies the description was updated",
         "--transit-gateway-ids tgw-0262a0e521EXAMPLE",
         None),
        ("To delete the transit gateway",
         "delete-transit-gateway", "deletes the transit gateway",
         "--transit-gateway-id tgw-0262a0e521EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # 45. VPN Connection
    # ──────────────────────────────────────────
    ("vpn-connection-lifecycle", [
        ("To create a customer gateway",
         "create-customer-gateway", "creates a customer gateway as prerequisite",
         "--type ipsec.1 --public-ip 203.0.113.12 --bgp-asn 65534",
         '{\n    "CustomerGateway": {\n        "CustomerGatewayId": "cgw-001122334455aabbc",\n        "BgpAsn": "65534",\n        "IpAddress": "203.0.113.12",\n        "Type": "ipsec.1",\n        "State": "available"\n    }\n}'),
        ("To create a virtual private gateway",
         "create-vpn-gateway", "creates a VPN gateway as prerequisite",
         "--type ipsec.1",
         '{\n    "VpnGateway": {\n        "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2",\n        "Type": "ipsec.1",\n        "State": "available"\n    }\n}'),
        ("To create a VPN connection",
         "create-vpn-connection", "creates a site-to-site VPN connection",
         "--type ipsec.1 --customer-gateway-id cgw-001122334455aabbc --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2",
         '{\n    "VpnConnection": {\n        "VpnConnectionId": "vpn-12345678901234567",\n        "CustomerGatewayId": "cgw-001122334455aabbc",\n        "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2",\n        "State": "pending"\n    }\n}'),
        ("To describe the VPN connection",
         "describe-vpn-connections", "retrieves details about the VPN connection",
         "--vpn-connection-ids vpn-12345678901234567",
         None),
        ("To modify the VPN connection",
         "modify-vpn-connection", "changes the VPN gateway for the connection",
         "--vpn-connection-id vpn-12345678901234567 --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2",
         None),
        ("To delete the VPN connection",
         "delete-vpn-connection", "deletes the VPN connection",
         "--vpn-connection-id vpn-12345678901234567",
         None),
    ]),

    # ──────────────────────────────────────────
    # 46. Local Gateway Route Table (may fail on emulator but included for completeness)
    # ──────────────────────────────────────────
    ("local-gateway-route-table-lifecycle", [
        ("To create a local gateway route table",
         "create-local-gateway-route-table", "creates a local gateway route table",
         "--local-gateway-id lgw-1a2b3c4d5e6f7g8h9 --mode direct-vpc-routing",
         '{\n    "LocalGatewayRouteTable": {\n        "LocalGatewayRouteTableId": "lgw-rtb-abcdefg123EXAMPLE",\n        "LocalGatewayId": "lgw-1a2b3c4d5e6f7g8h9",\n        "Mode": "direct-vpc-routing"\n    }\n}'),
        ("To describe the local gateway route table",
         "describe-local-gateway-route-tables", "retrieves details",
         "--local-gateway-route-table-ids lgw-rtb-abcdefg123EXAMPLE",
         None),
        ("To delete the local gateway route table",
         "delete-local-gateway-route-table", "deletes the route table",
         "--local-gateway-route-table-id lgw-rtb-abcdefg123EXAMPLE",
         None),
    ]),

    # ==================================================================
    # EDGE-CASE MODIFY VARIANTS — expose .Value parsing & nested bugs
    # ==================================================================

    # ──────────────────────────────────────────
    # EC1. Instance – modify disable-api-termination (bool via .Value)
    # ──────────────────────────────────────────
    ("instance-lifecycle-v3", [
        ("To register an AMI for the instance",
         "register-image", "registers a minimal AMI as prerequisite",
         "--name lifecycle-instance-v3-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}",
         '{\n    "ImageId": "ami-1234567890EXAMPLE"\n}'),
        ("To launch an instance",
         "run-instances", "launches an EC2 instance",
         "--image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1",
         '{\n    "Instances": [\n        {\n            "InstanceId": "i-1234567890abcdef0",\n            "InstanceType": "t2.micro",\n            "State": {"Name": "pending", "Code": 0},\n            "ImageId": "ami-1234567890EXAMPLE"\n        }\n    ]\n}'),
        ("To describe the instance",
         "describe-instances", "retrieves details about the launched instance",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To disable API termination on the instance",
         "modify-instance-attribute", "sets DisableApiTermination to true",
         "--instance-id i-1234567890abcdef0 --disable-api-termination",
         None),
        ("To describe the instance after modification",
         "describe-instances", "verifies disable-api-termination was set",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To re-enable API termination before cleanup",
         "modify-instance-attribute", "sets DisableApiTermination back to false",
         "--instance-id i-1234567890abcdef0 --no-disable-api-termination",
         None),
        ("To terminate the instance",
         "terminate-instances", "terminates the instance",
         "--instance-ids i-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC2. Instance – modify ebs-optimized (bool via .Value)
    # ──────────────────────────────────────────
    ("instance-lifecycle-v4", [
        ("To register an AMI for the instance",
         "register-image", "registers a minimal AMI as prerequisite",
         "--name lifecycle-instance-v4-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}",
         '{\n    "ImageId": "ami-1234567890EXAMPLE"\n}'),
        ("To launch an instance",
         "run-instances", "launches an EC2 instance",
         "--image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1",
         '{\n    "Instances": [\n        {\n            "InstanceId": "i-1234567890abcdef0",\n            "InstanceType": "t2.micro",\n            "State": {"Name": "pending", "Code": 0},\n            "ImageId": "ami-1234567890EXAMPLE"\n        }\n    ]\n}'),
        ("To describe the instance",
         "describe-instances", "retrieves details about the launched instance",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To enable EBS optimization on the instance",
         "modify-instance-attribute", "enables EBS optimization",
         "--instance-id i-1234567890abcdef0 --ebs-optimized",
         None),
        ("To describe the instance after modification",
         "describe-instances", "verifies EBS optimization was enabled",
         "--instance-ids i-1234567890abcdef0",
         None),
        ("To terminate the instance",
         "terminate-instances", "terminates the instance",
         "--instance-ids i-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC3. Subnet – modify map-public-ip-on-launch (bool via .Value)
    # ──────────────────────────────────────────
    ("subnet-lifecycle-v2", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet in the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.1.0/24",\n        "State": "available"\n    }\n}'),
        ("To describe the subnet",
         "describe-subnets", "retrieves details about the subnet",
         "--subnet-ids subnet-0250c25a1fEXAMPLE",
         None),
        ("To enable auto-assign public IP on the subnet",
         "modify-subnet-attribute", "enables auto-assign public IP",
         "--subnet-id subnet-0250c25a1fEXAMPLE --map-public-ip-on-launch",
         None),
        ("To describe the subnet after modification",
         "describe-subnets", "verifies public IP assignment is enabled",
         "--subnet-ids subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the subnet",
         "delete-subnet", "deletes the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC4. Subnet – modify enable-dns64 (bool via .Value)
    # ──────────────────────────────────────────
    ("subnet-lifecycle-v3", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet",
         "create-subnet", "creates a subnet in the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.1.0/24",\n        "State": "available"\n    }\n}'),
        ("To describe the subnet",
         "describe-subnets", "retrieves details about the subnet",
         "--subnet-ids subnet-0250c25a1fEXAMPLE",
         None),
        ("To enable DNS64 on the subnet",
         "modify-subnet-attribute", "enables DNS64",
         "--subnet-id subnet-0250c25a1fEXAMPLE --enable-dns64",
         None),
        ("To describe the subnet after modification",
         "describe-subnets", "verifies DNS64 is enabled",
         "--subnet-ids subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the subnet",
         "delete-subnet", "deletes the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC5. VPC – modify enable-dns-hostnames (bool via .Value)
    # ──────────────────────────────────────────
    ("vpc-lifecycle-v2", [
        ("To create a VPC",
         "create-vpc", "creates a VPC",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To describe the VPC",
         "describe-vpcs", "retrieves details about the VPC",
         "--vpc-ids vpc-0a60eb65b4EXAMPLE",
         None),
        ("To enable DNS hostnames on the VPC",
         "modify-vpc-attribute", "enables DNS hostnames",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --enable-dns-hostnames",
         None),
        ("To describe the VPC after modification",
         "describe-vpcs", "verifies DNS hostnames is enabled",
         "--vpc-ids vpc-0a60eb65b4EXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "deletes the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC6. VPC – modify enable-dns-support (bool via .Value)
    # ──────────────────────────────────────────
    ("vpc-lifecycle-v3", [
        ("To create a VPC",
         "create-vpc", "creates a VPC",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To describe the VPC",
         "describe-vpcs", "retrieves details about the VPC",
         "--vpc-ids vpc-0a60eb65b4EXAMPLE",
         None),
        ("To disable DNS support on the VPC",
         "modify-vpc-attribute", "disables DNS support",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --no-enable-dns-support",
         None),
        ("To describe the VPC after modification",
         "describe-vpcs", "verifies DNS support is disabled",
         "--vpc-ids vpc-0a60eb65b4EXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "deletes the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC7. Volume – modify-volume-attribute --auto-enable-io (via .Value)
    # ──────────────────────────────────────────
    ("volume-lifecycle-v7", [
        ("To create a gp3 EBS volume",
         "create-volume", "creates a 100 GiB gp3 volume",
         "--volume-type gp3 --size 100 --availability-zone us-east-1a",
         '{\n    "AvailabilityZone": "us-east-1a",\n    "Encrypted": false,\n    "VolumeType": "gp3",\n    "VolumeId": "vol-1234567890abcdef0",\n    "State": "creating",\n    "Iops": 3000,\n    "Size": 100\n}'),
        ("To describe the volume",
         "describe-volumes", "retrieves details about the volume",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To enable auto-enable-io on the volume",
         "modify-volume-attribute", "enables automatic IO recovery",
         "--volume-id vol-1234567890abcdef0 --auto-enable-io",
         None),
        ("To describe the volume after modification",
         "describe-volumes", "verifies auto-enable-io",
         "--volume-ids vol-1234567890abcdef0",
         None),
        ("To delete the volume",
         "delete-volume", "deletes the volume",
         "--volume-id vol-1234567890abcdef0",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC8. Security Group – authorize egress rule (nested IpPermissions)
    # ──────────────────────────────────────────
    ("security-group-lifecycle-v3", [
        ("To create a VPC",
         "create-vpc", "creates a VPC as prerequisite",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a security group",
         "create-security-group", "creates a security group in the VPC",
         "--group-name lifecycle-sg-v3 --description \"Lifecycle v3 security group\" --vpc-id vpc-0a60eb65b4EXAMPLE",
         '{\n    "GroupId": "sg-1234567890abcdef0"\n}'),
        ("To describe the security group",
         "describe-security-groups", "retrieves details about the security group",
         "--group-ids sg-1234567890abcdef0",
         None),
        ("To authorize egress HTTPS access",
         "authorize-security-group-egress", "adds an outbound rule for HTTPS",
         "--group-id sg-1234567890abcdef0 --protocol tcp --port 443 --cidr 0.0.0.0/0",
         None),
        ("To describe the security group after rule addition",
         "describe-security-groups", "verifies the HTTPS egress rule was added",
         "--group-ids sg-1234567890abcdef0",
         None),
        ("To delete the security group",
         "delete-security-group", "deletes the security group",
         "--group-id sg-1234567890abcdef0",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC9. Image – modify description via --description string
    # ──────────────────────────────────────────
    ("image-lifecycle-v3", [
        ("To register an AMI",
         "register-image", "registers an AMI",
         "--name lifecycle-image-v3 --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}",
         '{\n    "ImageId": "ami-1234567890EXAMPLE"\n}'),
        ("To describe the AMI",
         "describe-images", "retrieves details about the AMI",
         "--image-ids ami-1234567890EXAMPLE",
         None),
        ("To modify the AMI description",
         "modify-image-attribute", "updates the AMI description",
         "--image-id ami-1234567890EXAMPLE --description \"Edge case v3 description\"",
         None),
        ("To describe the AMI after modification",
         "describe-images", "verifies the description was updated",
         "--image-ids ami-1234567890EXAMPLE",
         None),
        ("To deregister the AMI",
         "deregister-image", "deregisters the AMI",
         "--image-id ami-1234567890EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC10. Capacity Reservation – modify instance-match-criteria
    # ──────────────────────────────────────────
    ("capacity-reservation-lifecycle-v3", [
        ("To create a Capacity Reservation",
         "create-capacity-reservation", "creates a Capacity Reservation",
         "--availability-zone us-east-1a --instance-type t2.medium --instance-platform Linux/UNIX --instance-count 3",
         '{\n    "CapacityReservation": {\n        "CapacityReservationId": "cr-1234abcd56EXAMPLE",\n        "InstanceType": "t2.medium",\n        "InstancePlatform": "Linux/UNIX",\n        "AvailabilityZone": "us-east-1a",\n        "TotalInstanceCount": 3,\n        "AvailableInstanceCount": 3,\n        "State": "active"\n    }\n}'),
        ("To describe the Capacity Reservation",
         "describe-capacity-reservations", "retrieves details about the Capacity Reservation",
         "--capacity-reservation-ids cr-1234abcd56EXAMPLE",
         None),
        ("To modify the Capacity Reservation match criteria",
         "modify-capacity-reservation", "changes the instance match criteria to open",
         "--capacity-reservation-id cr-1234abcd56EXAMPLE --instance-match-criteria open",
         None),
        ("To describe the Capacity Reservation after modification",
         "describe-capacity-reservations", "verifies the match criteria was changed",
         "--capacity-reservation-ids cr-1234abcd56EXAMPLE",
         None),
        ("To cancel the Capacity Reservation",
         "cancel-capacity-reservation", "cancels the Capacity Reservation",
         "--capacity-reservation-id cr-1234abcd56EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC11. Traffic Mirror Session – modify description (parser bug: parse_filters)
    # ──────────────────────────────────────────
    ("traffic-mirror-session-lifecycle-v2", [
        ("To create a VPC as prerequisite",
         "create-vpc", "creates a VPC",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a subnet as prerequisite",
         "create-subnet", "creates a subnet in the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24",
         '{\n    "Subnet": {\n        "SubnetId": "subnet-0250c25a1fEXAMPLE",\n        "VpcId": "vpc-0a60eb65b4EXAMPLE"\n    }\n}'),
        ("To create a network interface as prerequisite",
         "create-network-interface", "creates an ENI for traffic mirroring",
         "--subnet-id subnet-0250c25a1fEXAMPLE --description tm-source",
         '{\n    "NetworkInterface": {\n        "NetworkInterfaceId": "eni-070203f901EXAMPLE",\n        "SubnetId": "subnet-0250c25a1fEXAMPLE"\n    }\n}'),
        ("To create a traffic mirror filter",
         "create-traffic-mirror-filter", "creates a filter as prerequisite",
         "--description 'Session v2 filter'",
         '{\n    "TrafficMirrorFilter": {\n        "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE"\n    }\n}'),
        ("To create a traffic mirror target",
         "create-traffic-mirror-target", "creates a target as prerequisite",
         "--description 'Session v2 target' --network-interface-id eni-070203f901EXAMPLE",
         '{\n    "TrafficMirrorTarget": {\n        "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",\n        "NetworkInterfaceId": "eni-070203f901EXAMPLE"\n    }\n}'),
        ("To create a traffic mirror session",
         "create-traffic-mirror-session", "creates a traffic mirror session",
         "--traffic-mirror-target-id tmt-07f75d8feeEXAMPLE --network-interface-id eni-070203f901EXAMPLE --session-number 1 --traffic-mirror-filter-id tmf-04812ff784EXAMPLE",
         '{\n    "TrafficMirrorSession": {\n        "TrafficMirrorSessionId": "tms-0af3141ce5EXAMPLE",\n        "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",\n        "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE",\n        "SessionNumber": 1\n    }\n}'),
        ("To describe the traffic mirror session",
         "describe-traffic-mirror-sessions", "retrieves details about the session",
         "--traffic-mirror-session-ids tms-0af3141ce5EXAMPLE",
         None),
        ("To modify the traffic mirror session description",
         "modify-traffic-mirror-session", "updates the session description",
         "--traffic-mirror-session-id tms-0af3141ce5EXAMPLE --description \"Updated v2 session\"",
         None),
        ("To describe after modification",
         "describe-traffic-mirror-sessions", "verifies the description was updated",
         "--traffic-mirror-session-ids tms-0af3141ce5EXAMPLE",
         None),
        ("To delete the traffic mirror session",
         "delete-traffic-mirror-session", "deletes the session",
         "--traffic-mirror-session-id tms-0af3141ce5EXAMPLE",
         None),
        ("To delete the traffic mirror target",
         "delete-traffic-mirror-target", "cleans up the target",
         "--traffic-mirror-target-id tmt-07f75d8feeEXAMPLE",
         None),
        ("To delete the traffic mirror filter",
         "delete-traffic-mirror-filter", "cleans up the filter",
         "--traffic-mirror-filter-id tmf-04812ff784EXAMPLE",
         None),
        ("To delete the network interface",
         "delete-network-interface", "cleans up the ENI",
         "--network-interface-id eni-070203f901EXAMPLE",
         None),
        ("To delete the subnet",
         "delete-subnet", "cleans up the subnet",
         "--subnet-id subnet-0250c25a1fEXAMPLE",
         None),
        ("To delete the VPC",
         "delete-vpc", "cleans up the VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
    ]),

    # ──────────────────────────────────────────
    # EC12. VPC Peering – modify peering options
    # ──────────────────────────────────────────
    ("vpc-peering-connection-lifecycle-v2", [
        ("To create first VPC",
         "create-vpc", "creates the requester VPC",
         "--cidr-block 10.0.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-0a60eb65b4EXAMPLE",\n        "CidrBlock": "10.0.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create second VPC",
         "create-vpc", "creates the accepter VPC",
         "--cidr-block 10.1.0.0/16",
         '{\n    "Vpc": {\n        "VpcId": "vpc-11122233aaEXAMPLE",\n        "CidrBlock": "10.1.0.0/16",\n        "State": "available"\n    }\n}'),
        ("To create a VPC peering connection",
         "create-vpc-peering-connection", "creates a peering connection between VPCs",
         "--vpc-id vpc-0a60eb65b4EXAMPLE --peer-vpc-id vpc-11122233aaEXAMPLE",
         '{\n    "VpcPeeringConnection": {\n        "VpcPeeringConnectionId": "pcx-111aaa111EXAMPLE",\n        "RequesterVpcInfo": {"VpcId": "vpc-0a60eb65b4EXAMPLE"},\n        "AccepterVpcInfo": {"VpcId": "vpc-11122233aaEXAMPLE"},\n        "Status": {"Code": "initiating-request"}\n    }\n}'),
        ("To accept the VPC peering connection",
         "accept-vpc-peering-connection", "accepts the peering connection",
         "--vpc-peering-connection-id pcx-111aaa111EXAMPLE",
         None),
        ("To describe the peering connection",
         "describe-vpc-peering-connections", "retrieves details about the peering",
         "--vpc-peering-connection-ids pcx-111aaa111EXAMPLE",
         None),
        ("To delete the VPC peering connection",
         "delete-vpc-peering-connection", "deletes the peering connection",
         "--vpc-peering-connection-id pcx-111aaa111EXAMPLE",
         None),
        ("To delete first VPC",
         "delete-vpc", "cleans up the requester VPC",
         "--vpc-id vpc-0a60eb65b4EXAMPLE",
         None),
        ("To delete second VPC",
         "delete-vpc", "cleans up the accepter VPC",
         "--vpc-id vpc-11122233aaEXAMPLE",
         None),
    ]),
]


def generate_rst(filename_stem, steps):
    """Generate a lifecycle RST file from the step definitions."""
    lines = []
    for i, step in enumerate(steps, 1):
        title, subcmd, desc_text, args, output = step
        cmd = f"aws ec2 {subcmd}"
        if args:
            cmd += f" \\\n        {args}" if len(f"aws ec2 {subcmd} {args}") > 80 else f" {args}"

        lines.append(f"**Example {i}: {title}**")
        lines.append("")
        lines.append(f"The following ``{subcmd}`` example {desc_text}. ::")
        lines.append("")
        # Format the command: if it has line continuations, indent properly
        if " \\\n" in cmd:
            lines.append(f"    {cmd}")
        else:
            lines.append(f"    {cmd}")
        lines.append("")

        if output:
            lines.append("Output::")
            lines.append("")
            for output_line in output.split('\n'):
                lines.append(f"    {output_line}")
            lines.append("")

    return '\n'.join(lines) + '\n'


def generate_bundle(tests):
    """Generate test_lifecycle_bundle.sh from the lifecycle test definitions."""
    lines = ["#!/usr/bin/env bash", "# Auto-generated lifecycle bundle", ""]
    for filename_stem, steps in tests:
        lines.append(f"# -- {filename_stem} --")
        for step in steps:
            _title, subcmd, _desc, args, _output = step
            cmd = f"awscli ec2 {subcmd}"
            if args:
                cmd += f" {args}"
            lines.append(f"# label: lifecycle-file:{filename_stem}")
            lines.append(cmd)
        lines.append("")
    return "\n".join(lines)


def main():
    generated = 0
    for filename_stem, steps in LIFECYCLE_TESTS:
        rst_path = RST_DIR / f"{filename_stem}.rst"
        content = generate_rst(filename_stem, steps)
        rst_path.write_text(content, encoding='utf-8')
        generated += 1
        print(f"  ✓ {filename_stem}.rst ({len(steps)} steps)")

    print(f"\nGenerated {generated} lifecycle RST files in {RST_DIR}")

    bundle_path = SCRIPT_DIR / "test_lifecycle_bundle.sh"
    bundle_content = generate_bundle(LIFECYCLE_TESTS)
    bundle_path.write_text(bundle_content, encoding='utf-8')
    total_cmds = sum(len(steps) for _, steps in LIFECYCLE_TESTS)
    print(f"Generated {bundle_path.name}: {generated} sections, {total_cmds} commands")


if __name__ == "__main__":
    main()
