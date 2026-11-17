#!/usr/bin/env bash
# Auto-generated lifecycle bundle

# -- address-lifecycle --
# label: lifecycle-file:address-lifecycle
awscli ec2 allocate-address
# label: lifecycle-file:address-lifecycle
awscli ec2 describe-addresses --allocation-ids eipalloc-01435ba59eEXAMPLE
# label: lifecycle-file:address-lifecycle
awscli ec2 release-address --allocation-id eipalloc-01435ba59eEXAMPLE

# -- capacity-reservation-lifecycle --
# label: lifecycle-file:capacity-reservation-lifecycle
awscli ec2 create-capacity-reservation --availability-zone us-east-1a --instance-type t2.medium --instance-platform Linux/UNIX --instance-count 3
# label: lifecycle-file:capacity-reservation-lifecycle
awscli ec2 describe-capacity-reservations --capacity-reservation-ids cr-1234abcd56EXAMPLE
# label: lifecycle-file:capacity-reservation-lifecycle
awscli ec2 modify-capacity-reservation --capacity-reservation-id cr-1234abcd56EXAMPLE --instance-count 5
# label: lifecycle-file:capacity-reservation-lifecycle
awscli ec2 describe-capacity-reservations --capacity-reservation-ids cr-1234abcd56EXAMPLE
# label: lifecycle-file:capacity-reservation-lifecycle
awscli ec2 cancel-capacity-reservation --capacity-reservation-id cr-1234abcd56EXAMPLE

# -- carrier-gateway-lifecycle --
# label: lifecycle-file:carrier-gateway-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:carrier-gateway-lifecycle
awscli ec2 create-carrier-gateway --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:carrier-gateway-lifecycle
awscli ec2 describe-carrier-gateways --carrier-gateway-ids cagw-0465cdEXAMPLE1111
# label: lifecycle-file:carrier-gateway-lifecycle
awscli ec2 delete-carrier-gateway --carrier-gateway-id cagw-0465cdEXAMPLE1111
# label: lifecycle-file:carrier-gateway-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- dhcp-options-lifecycle --
# label: lifecycle-file:dhcp-options-lifecycle
awscli ec2 create-dhcp-options --dhcp-configuration "Key=domain-name-servers,Values=10.2.5.1,10.2.5.2" "Key=domain-name,Values=example.com"
# label: lifecycle-file:dhcp-options-lifecycle
awscli ec2 describe-dhcp-options --dhcp-options-ids dopt-0a1b2c3d4eEXAMPLE
# label: lifecycle-file:dhcp-options-lifecycle
awscli ec2 delete-dhcp-options --dhcp-options-id dopt-0a1b2c3d4eEXAMPLE

# -- fleet-lifecycle --
# label: lifecycle-file:fleet-lifecycle
awscli ec2 create-launch-template --launch-template-name lifecycle-fleet-lt --launch-template-data '{"ImageId":"ami-0abcdef1234567890","InstanceType":"t2.micro"}'
# label: lifecycle-file:fleet-lifecycle
awscli ec2 create-fleet --type instant --launch-template-configs 'LaunchTemplateSpecification={LaunchTemplateId=lt-0e8c754449EXAMPLE,Version=1}' --target-capacity-specification TotalTargetCapacity=1,DefaultTargetCapacityType=on-demand
# label: lifecycle-file:fleet-lifecycle
awscli ec2 describe-fleets --fleet-ids fleet-12a34b55EXAMPLE
# label: lifecycle-file:fleet-lifecycle
awscli ec2 modify-fleet --fleet-id fleet-12a34b55EXAMPLE --target-capacity-specification TotalTargetCapacity=2
# label: lifecycle-file:fleet-lifecycle
awscli ec2 delete-fleets --fleet-ids fleet-12a34b55EXAMPLE --terminate-instances
# label: lifecycle-file:fleet-lifecycle
awscli ec2 delete-launch-template --launch-template-id lt-0e8c754449EXAMPLE

# -- flow-log-lifecycle --
# label: lifecycle-file:flow-log-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:flow-log-lifecycle
awscli ec2 create-flow-logs --resource-type VPC --resource-ids vpc-0a60eb65b4EXAMPLE --traffic-type ALL --log-destination-type cloud-watch-logs --log-group-name my-flow-logs
# label: lifecycle-file:flow-log-lifecycle
awscli ec2 describe-flow-logs --flow-log-ids fl-11223344556677889
# label: lifecycle-file:flow-log-lifecycle
awscli ec2 delete-flow-logs --flow-log-ids fl-11223344556677889
# label: lifecycle-file:flow-log-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- host-lifecycle --
# label: lifecycle-file:host-lifecycle
awscli ec2 allocate-hosts --instance-type m5.large --availability-zone us-east-1a --quantity 1
# label: lifecycle-file:host-lifecycle
awscli ec2 describe-hosts --host-ids h-0029d6e3cacf1b3da
# label: lifecycle-file:host-lifecycle
awscli ec2 modify-hosts --host-ids h-0029d6e3cacf1b3da --auto-placement on
# label: lifecycle-file:host-lifecycle
awscli ec2 describe-hosts --host-ids h-0029d6e3cacf1b3da
# label: lifecycle-file:host-lifecycle
awscli ec2 release-hosts --host-ids h-0029d6e3cacf1b3da

# -- image-lifecycle --
# label: lifecycle-file:image-lifecycle
awscli ec2 register-image --name lifecycle-test-image --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}
# label: lifecycle-file:image-lifecycle
awscli ec2 describe-images --image-ids ami-1234567890EXAMPLE
# label: lifecycle-file:image-lifecycle
awscli ec2 modify-image-attribute --image-id ami-1234567890EXAMPLE --description "Updated lifecycle image"
# label: lifecycle-file:image-lifecycle
awscli ec2 describe-images --image-ids ami-1234567890EXAMPLE
# label: lifecycle-file:image-lifecycle
awscli ec2 deregister-image --image-id ami-1234567890EXAMPLE

# -- instance-lifecycle --
# label: lifecycle-file:instance-lifecycle
awscli ec2 register-image --name lifecycle-instance-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}
# label: lifecycle-file:instance-lifecycle
awscli ec2 run-instances --image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1
# label: lifecycle-file:instance-lifecycle
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle
awscli ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --instance-type "{\"Value\": \"t2.small\"}"
# label: lifecycle-file:instance-lifecycle
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle
awscli ec2 terminate-instances --instance-ids i-1234567890abcdef0

# -- internet-gateway-lifecycle --
# label: lifecycle-file:internet-gateway-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:internet-gateway-lifecycle
awscli ec2 create-internet-gateway
# label: lifecycle-file:internet-gateway-lifecycle
awscli ec2 describe-internet-gateways --internet-gateway-ids igw-0d0fb496b3EXAMPLE
# label: lifecycle-file:internet-gateway-lifecycle
awscli ec2 attach-internet-gateway --internet-gateway-id igw-0d0fb496b3EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:internet-gateway-lifecycle
awscli ec2 detach-internet-gateway --internet-gateway-id igw-0d0fb496b3EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:internet-gateway-lifecycle
awscli ec2 delete-internet-gateway --internet-gateway-id igw-0d0fb496b3EXAMPLE
# label: lifecycle-file:internet-gateway-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- key-pair-lifecycle --
# label: lifecycle-file:key-pair-lifecycle
awscli ec2 create-key-pair --key-name lifecycle-test-key --key-type rsa
# label: lifecycle-file:key-pair-lifecycle
awscli ec2 describe-key-pairs --key-names lifecycle-test-key
# label: lifecycle-file:key-pair-lifecycle
awscli ec2 delete-key-pair --key-name lifecycle-test-key

# -- instance-connect-endpoint-lifecycle --
# label: lifecycle-file:instance-connect-endpoint-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:instance-connect-endpoint-lifecycle
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:instance-connect-endpoint-lifecycle
awscli ec2 create-instance-connect-endpoint --subnet-id subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:instance-connect-endpoint-lifecycle
awscli ec2 describe-instance-connect-endpoints --instance-connect-endpoint-ids eice-03f5e49b83EXAMPLE
# label: lifecycle-file:instance-connect-endpoint-lifecycle
awscli ec2 delete-instance-connect-endpoint --instance-connect-endpoint-id eice-03f5e49b83EXAMPLE

# -- instance-event-window-lifecycle --
# label: lifecycle-file:instance-event-window-lifecycle
awscli ec2 create-instance-event-window --time-range StartWeekDay=monday,StartHour=2,EndWeekDay=wednesday,EndHour=8 --tag-specifications 'ResourceType=instance-event-window,Tags=[{Key=Name,Value=lifecycle-test}]' --name lifecycle-event-window
# label: lifecycle-file:instance-event-window-lifecycle
awscli ec2 describe-instance-event-windows --instance-event-window-ids iew-0abcdef1234567890
# label: lifecycle-file:instance-event-window-lifecycle
awscli ec2 modify-instance-event-window --instance-event-window-id iew-0abcdef1234567890 --time-range StartWeekDay=tuesday,StartHour=4,EndWeekDay=thursday,EndHour=10
# label: lifecycle-file:instance-event-window-lifecycle
awscli ec2 describe-instance-event-windows --instance-event-window-ids iew-0abcdef1234567890
# label: lifecycle-file:instance-event-window-lifecycle
awscli ec2 delete-instance-event-window --instance-event-window-id iew-0abcdef1234567890

# -- ipam-lifecycle --
# label: lifecycle-file:ipam-lifecycle
awscli ec2 create-ipam --description 'Lifecycle test IPAM' --operating-regions RegionName=us-east-1 --tag-specifications 'ResourceType=ipam,Tags=[{Key=Name,Value=lifecycle-ipam}]'
# label: lifecycle-file:ipam-lifecycle
awscli ec2 describe-ipams --ipam-ids ipam-08440e7a3aEXAMPLE
# label: lifecycle-file:ipam-lifecycle
awscli ec2 modify-ipam --ipam-id ipam-08440e7a3aEXAMPLE --add-operating-regions RegionName=us-west-2
# label: lifecycle-file:ipam-lifecycle
awscli ec2 describe-ipams --ipam-ids ipam-08440e7a3aEXAMPLE
# label: lifecycle-file:ipam-lifecycle
awscli ec2 delete-ipam --ipam-id ipam-08440e7a3aEXAMPLE

# -- ipam-pool-lifecycle --
# label: lifecycle-file:ipam-pool-lifecycle
awscli ec2 create-ipam --description 'Pool prerequisite' --operating-regions RegionName=us-east-1
# label: lifecycle-file:ipam-pool-lifecycle
awscli ec2 create-ipam-pool --ipam-scope-id ipam-scope-02fc38cd4cEXAMPLE --address-family ipv4 --allocation-min-netmask-length 16 --allocation-max-netmask-length 26
# label: lifecycle-file:ipam-pool-lifecycle
awscli ec2 describe-ipam-pools --ipam-pool-ids ipam-pool-0533048da7EXAMPLE
# label: lifecycle-file:ipam-pool-lifecycle
awscli ec2 modify-ipam-pool --ipam-pool-id ipam-pool-0533048da7EXAMPLE --allocation-min-netmask-length 14
# label: lifecycle-file:ipam-pool-lifecycle
awscli ec2 delete-ipam-pool --ipam-pool-id ipam-pool-0533048da7EXAMPLE
# label: lifecycle-file:ipam-pool-lifecycle
awscli ec2 delete-ipam --ipam-id ipam-08440e7a3aEXAMPLE

# -- ipam-resource-discovery-lifecycle --
# label: lifecycle-file:ipam-resource-discovery-lifecycle
awscli ec2 create-ipam-resource-discovery --description 'Lifecycle test discovery' --operating-regions RegionName=us-east-1 --tag-specifications 'ResourceType=ipam-resource-discovery,Tags=[{Key=Name,Value=lifecycle-disc}]'
# label: lifecycle-file:ipam-resource-discovery-lifecycle
awscli ec2 describe-ipam-resource-discoveries --ipam-resource-discovery-ids ipam-res-disco-0e39761475EXAMPLE
# label: lifecycle-file:ipam-resource-discovery-lifecycle
awscli ec2 modify-ipam-resource-discovery --ipam-resource-discovery-id ipam-res-disco-0e39761475EXAMPLE --add-operating-regions RegionName=us-west-1
# label: lifecycle-file:ipam-resource-discovery-lifecycle
awscli ec2 delete-ipam-resource-discovery --ipam-resource-discovery-id ipam-res-disco-0e39761475EXAMPLE

# -- ipam-scope-lifecycle --
# label: lifecycle-file:ipam-scope-lifecycle
awscli ec2 create-ipam --description 'Scope prerequisite' --operating-regions RegionName=us-east-1
# label: lifecycle-file:ipam-scope-lifecycle
awscli ec2 create-ipam-scope --ipam-id ipam-08440e7a3aEXAMPLE --description 'Lifecycle test scope'
# label: lifecycle-file:ipam-scope-lifecycle
awscli ec2 describe-ipam-scopes --ipam-scope-ids ipam-scope-01c1ebab2bEXAMPLE
# label: lifecycle-file:ipam-scope-lifecycle
awscli ec2 modify-ipam-scope --ipam-scope-id ipam-scope-01c1ebab2bEXAMPLE --description 'Updated scope'
# label: lifecycle-file:ipam-scope-lifecycle
awscli ec2 delete-ipam-scope --ipam-scope-id ipam-scope-01c1ebab2bEXAMPLE
# label: lifecycle-file:ipam-scope-lifecycle
awscli ec2 delete-ipam --ipam-id ipam-08440e7a3aEXAMPLE

# -- managed-prefix-list-lifecycle --
# label: lifecycle-file:managed-prefix-list-lifecycle
awscli ec2 create-managed-prefix-list --address-family IPv4 --max-entries 10 --entries Cidr=10.0.0.0/16,Description=vpc-a --prefix-list-name lifecycle-prefix-list
# label: lifecycle-file:managed-prefix-list-lifecycle
awscli ec2 describe-managed-prefix-lists --prefix-list-ids pl-0123456abcEXAMPLE
# label: lifecycle-file:managed-prefix-list-lifecycle
awscli ec2 modify-managed-prefix-list --prefix-list-id pl-0123456abcEXAMPLE --add-entries Cidr=10.2.0.0/16,Description=vpc-b --current-version 1
# label: lifecycle-file:managed-prefix-list-lifecycle
awscli ec2 describe-managed-prefix-lists --prefix-list-ids pl-0123456abcEXAMPLE
# label: lifecycle-file:managed-prefix-list-lifecycle
awscli ec2 delete-managed-prefix-list --prefix-list-id pl-0123456abcEXAMPLE

# -- nat-gateway-lifecycle --
# label: lifecycle-file:nat-gateway-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:nat-gateway-lifecycle
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:nat-gateway-lifecycle
awscli ec2 create-nat-gateway --subnet-id subnet-0250c25a1fEXAMPLE --connectivity-type private
# label: lifecycle-file:nat-gateway-lifecycle
awscli ec2 describe-nat-gateways --nat-gateway-ids nat-0c61bf8a12EXAMPLE
# label: lifecycle-file:nat-gateway-lifecycle
awscli ec2 delete-nat-gateway --nat-gateway-id nat-0c61bf8a12EXAMPLE

# -- network-acl-lifecycle --
# label: lifecycle-file:network-acl-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:network-acl-lifecycle
awscli ec2 create-network-acl --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:network-acl-lifecycle
awscli ec2 describe-network-acls --network-acl-ids acl-5fb85d36EXAMPLE
# label: lifecycle-file:network-acl-lifecycle
awscli ec2 delete-network-acl --network-acl-id acl-5fb85d36EXAMPLE
# label: lifecycle-file:network-acl-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- network-insights-path-lifecycle --
# label: lifecycle-file:network-insights-path-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:network-insights-path-lifecycle
awscli ec2 create-internet-gateway
# label: lifecycle-file:network-insights-path-lifecycle
awscli ec2 create-network-insights-path --source igw-0d0fb496b3EXAMPLE --destination vpc-0a60eb65b4EXAMPLE --protocol TCP
# label: lifecycle-file:network-insights-path-lifecycle
awscli ec2 describe-network-insights-paths --network-insights-path-ids nip-0b26f224f1EXAMPLE
# label: lifecycle-file:network-insights-path-lifecycle
awscli ec2 delete-network-insights-path --network-insights-path-id nip-0b26f224f1EXAMPLE

# -- network-insights-access-scope-lifecycle --
# label: lifecycle-file:network-insights-access-scope-lifecycle
awscli ec2 create-network-insights-access-scope --match-paths 'Source={ResourceStatement={ResourceTypes=[AWS::EC2::NetworkInterface]}}'
# label: lifecycle-file:network-insights-access-scope-lifecycle
awscli ec2 describe-network-insights-access-scopes --network-insights-access-scope-ids nis-123456789aEXAMPLE
# label: lifecycle-file:network-insights-access-scope-lifecycle
awscli ec2 delete-network-insights-access-scope --network-insights-access-scope-id nis-123456789aEXAMPLE

# -- route-table-lifecycle --
# label: lifecycle-file:route-table-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:route-table-lifecycle
awscli ec2 create-route-table --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:route-table-lifecycle
awscli ec2 describe-route-tables --route-table-ids rtb-22574640EXAMPLE
# label: lifecycle-file:route-table-lifecycle
awscli ec2 delete-route-table --route-table-id rtb-22574640EXAMPLE
# label: lifecycle-file:route-table-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- security-group-lifecycle --
# label: lifecycle-file:security-group-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:security-group-lifecycle
awscli ec2 create-security-group --group-name lifecycle-sg --description "Lifecycle test security group" --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:security-group-lifecycle
awscli ec2 describe-security-groups --group-ids sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle
awscli ec2 authorize-security-group-ingress --group-id sg-1234567890abcdef0 --protocol tcp --port 22 --cidr 203.0.113.0/24
# label: lifecycle-file:security-group-lifecycle
awscli ec2 describe-security-groups --group-ids sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle
awscli ec2 delete-security-group --group-id sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- spot-datafeed-subscription-lifecycle --
# label: lifecycle-file:spot-datafeed-subscription-lifecycle
awscli ec2 create-spot-datafeed-subscription --bucket amzn-s3-demo-bucket --prefix spot-data-feed
# label: lifecycle-file:spot-datafeed-subscription-lifecycle
awscli ec2 describe-spot-datafeed-subscription
# label: lifecycle-file:spot-datafeed-subscription-lifecycle
awscli ec2 delete-spot-datafeed-subscription

# -- subnet-lifecycle --
# label: lifecycle-file:subnet-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:subnet-lifecycle
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=lifecycle-subnet}]'
# label: lifecycle-file:subnet-lifecycle
awscli ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle
awscli ec2 modify-subnet-attribute --subnet-id subnet-0250c25a1fEXAMPLE --map-public-ip-on-launch
# label: lifecycle-file:subnet-lifecycle
awscli ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle
awscli ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- tag-lifecycle --
# label: lifecycle-file:tag-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:tag-lifecycle
awscli ec2 create-tags --resources vpc-0a60eb65b4EXAMPLE --tags Key=Name,Value=lifecycle-vpc Key=Environment,Value=test
# label: lifecycle-file:tag-lifecycle
awscli ec2 describe-tags --filters "Name=resource-id,Values=vpc-0a60eb65b4EXAMPLE"
# label: lifecycle-file:tag-lifecycle
awscli ec2 delete-tags --resources vpc-0a60eb65b4EXAMPLE --tags Key=Environment
# label: lifecycle-file:tag-lifecycle
awscli ec2 describe-tags --filters "Name=resource-id,Values=vpc-0a60eb65b4EXAMPLE"
# label: lifecycle-file:tag-lifecycle
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- traffic-mirror-filter-lifecycle --
# label: lifecycle-file:traffic-mirror-filter-lifecycle
awscli ec2 create-traffic-mirror-filter --description 'Lifecycle TCP Filter'
# label: lifecycle-file:traffic-mirror-filter-lifecycle
awscli ec2 describe-traffic-mirror-filters --traffic-mirror-filter-ids tmf-0be0b25fcdEXAMPLE
# label: lifecycle-file:traffic-mirror-filter-lifecycle
awscli ec2 delete-traffic-mirror-filter --traffic-mirror-filter-id tmf-0be0b25fcdEXAMPLE

# -- traffic-mirror-session-lifecycle --
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 create-traffic-mirror-filter --description 'Session filter'
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 create-traffic-mirror-target --description 'Session target' --network-interface-id eni-070203f901EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 create-traffic-mirror-session --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE --network-interface-id eni-070203f901EXAMPLE --session-number 1 --traffic-mirror-filter-id tmf-04812ff784EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 describe-traffic-mirror-sessions --traffic-mirror-session-ids tms-0af3141ce5EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 modify-traffic-mirror-session --traffic-mirror-session-id tms-0af3141ce5EXAMPLE --description "Updated session"
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 delete-traffic-mirror-session --traffic-mirror-session-id tms-0af3141ce5EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 delete-traffic-mirror-target --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle
awscli ec2 delete-traffic-mirror-filter --traffic-mirror-filter-id tmf-04812ff784EXAMPLE

# -- traffic-mirror-target-lifecycle --
# label: lifecycle-file:traffic-mirror-target-lifecycle
awscli ec2 create-traffic-mirror-target --description 'Lifecycle target' --network-interface-id eni-070203f901EXAMPLE
# label: lifecycle-file:traffic-mirror-target-lifecycle
awscli ec2 describe-traffic-mirror-targets --traffic-mirror-target-ids tmt-060f48ce9EXAMPLE
# label: lifecycle-file:traffic-mirror-target-lifecycle
awscli ec2 delete-traffic-mirror-target --traffic-mirror-target-id tmt-060f48ce9EXAMPLE

# -- transit-gateway-lifecycle --
# label: lifecycle-file:transit-gateway-lifecycle
awscli ec2 create-transit-gateway --description MyTGW --options AmazonSideAsn=64516,AutoAcceptSharedAttachments=enable,DefaultRouteTableAssociation=enable,DefaultRouteTablePropagation=enable,VpnEcmpSupport=enable,DnsSupport=enable
# label: lifecycle-file:transit-gateway-lifecycle
awscli ec2 describe-transit-gateways --transit-gateway-ids tgw-0262a0e521EXAMPLE
# label: lifecycle-file:transit-gateway-lifecycle
awscli ec2 modify-transit-gateway --transit-gateway-id tgw-0262a0e521EXAMPLE --options VpnEcmpSupport=disable
# label: lifecycle-file:transit-gateway-lifecycle
awscli ec2 describe-transit-gateways --transit-gateway-ids tgw-0262a0e521EXAMPLE
# label: lifecycle-file:transit-gateway-lifecycle
awscli ec2 delete-transit-gateway --transit-gateway-id tgw-0262a0e521EXAMPLE

# -- transit-gateway-connect-lifecycle --
# label: lifecycle-file:transit-gateway-connect-lifecycle
awscli ec2 create-transit-gateway --description ConnectTGW
# label: lifecycle-file:transit-gateway-connect-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:transit-gateway-connect-lifecycle
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:transit-gateway-connect-lifecycle
awscli ec2 create-transit-gateway-vpc-attachment --transit-gateway-id tgw-0262a0e521EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:transit-gateway-connect-lifecycle
awscli ec2 create-transit-gateway-connect --transport-transit-gateway-attachment-id tgw-attach-0a89069f57EXAMPLE --options Protocol=gre
# label: lifecycle-file:transit-gateway-connect-lifecycle
awscli ec2 describe-transit-gateway-connects --transit-gateway-attachment-ids tgw-attach-037012e5dcEXAMPLE
# label: lifecycle-file:transit-gateway-connect-lifecycle
awscli ec2 delete-transit-gateway-connect --transit-gateway-attachment-id tgw-attach-037012e5dcEXAMPLE

# -- transit-gateway-connect-peer-lifecycle --
# label: lifecycle-file:transit-gateway-connect-peer-lifecycle
awscli ec2 create-transit-gateway-connect-peer --transit-gateway-attachment-id tgw-attach-0f0927767cEXAMPLE --peer-address 172.31.1.11 --inside-cidr-blocks 169.254.6.0/29
# label: lifecycle-file:transit-gateway-connect-peer-lifecycle
awscli ec2 describe-transit-gateway-connect-peers --transit-gateway-connect-peer-ids tgw-connect-peer-0666adbac4EXAMPLE
# label: lifecycle-file:transit-gateway-connect-peer-lifecycle
awscli ec2 delete-transit-gateway-connect-peer --transit-gateway-connect-peer-id tgw-connect-peer-0666adbac4EXAMPLE

# -- transit-gateway-multicast-domain-lifecycle --
# label: lifecycle-file:transit-gateway-multicast-domain-lifecycle
awscli ec2 create-transit-gateway --description MulticastTGW --options MulticastSupport=enable
# label: lifecycle-file:transit-gateway-multicast-domain-lifecycle
awscli ec2 create-transit-gateway-multicast-domain --transit-gateway-id tgw-0bf0bffefaEXAMPLE --options StaticSourcesSupport=disable,Igmpv2Support=enable
# label: lifecycle-file:transit-gateway-multicast-domain-lifecycle
awscli ec2 describe-transit-gateway-multicast-domains --transit-gateway-multicast-domain-ids tgw-mcast-domain-0c4905cef7EXAMPLE
# label: lifecycle-file:transit-gateway-multicast-domain-lifecycle
awscli ec2 delete-transit-gateway-multicast-domain --transit-gateway-multicast-domain-id tgw-mcast-domain-0c4905cef7EXAMPLE
# label: lifecycle-file:transit-gateway-multicast-domain-lifecycle
awscli ec2 delete-transit-gateway --transit-gateway-id tgw-0bf0bffefaEXAMPLE

# -- transit-gateway-peering-attachment-lifecycle --
# label: lifecycle-file:transit-gateway-peering-attachment-lifecycle
awscli ec2 create-transit-gateway-peering-attachment --transit-gateway-id tgw-123abc05e04123abc --peer-transit-gateway-id tgw-11223344aabbcc112 --peer-account-id 123456789012 --peer-region us-east-2
# label: lifecycle-file:transit-gateway-peering-attachment-lifecycle
awscli ec2 describe-transit-gateway-peering-attachments --transit-gateway-attachment-ids tgw-attach-4455667788EXAMPLE
# label: lifecycle-file:transit-gateway-peering-attachment-lifecycle
awscli ec2 delete-transit-gateway-peering-attachment --transit-gateway-attachment-id tgw-attach-4455667788EXAMPLE

# -- transit-gateway-policy-table-lifecycle --
# label: lifecycle-file:transit-gateway-policy-table-lifecycle
awscli ec2 create-transit-gateway --description PolicyTGW
# label: lifecycle-file:transit-gateway-policy-table-lifecycle
awscli ec2 create-transit-gateway-policy-table --transit-gateway-id tgw-067f8505c18f0bd6e
# label: lifecycle-file:transit-gateway-policy-table-lifecycle
awscli ec2 describe-transit-gateway-policy-tables --transit-gateway-policy-table-ids tgw-ptb-0a16f134b7EXAMPLE
# label: lifecycle-file:transit-gateway-policy-table-lifecycle
awscli ec2 delete-transit-gateway-policy-table --transit-gateway-policy-table-id tgw-ptb-0a16f134b7EXAMPLE
# label: lifecycle-file:transit-gateway-policy-table-lifecycle
awscli ec2 delete-transit-gateway --transit-gateway-id tgw-067f8505c18f0bd6e

# -- transit-gateway-route-table-lifecycle --
# label: lifecycle-file:transit-gateway-route-table-lifecycle
awscli ec2 create-transit-gateway --description RouteTGW
# label: lifecycle-file:transit-gateway-route-table-lifecycle
awscli ec2 create-transit-gateway-route-table --transit-gateway-id tgw-0262a0e521EXAMPLE
# label: lifecycle-file:transit-gateway-route-table-lifecycle
awscli ec2 describe-transit-gateway-route-tables --transit-gateway-route-table-ids tgw-rtb-0b6f6aaa01EXAMPLE
# label: lifecycle-file:transit-gateway-route-table-lifecycle
awscli ec2 delete-transit-gateway-route-table --transit-gateway-route-table-id tgw-rtb-0b6f6aaa01EXAMPLE
# label: lifecycle-file:transit-gateway-route-table-lifecycle
awscli ec2 delete-transit-gateway --transit-gateway-id tgw-0262a0e521EXAMPLE

# -- transit-gateway-vpc-attachment-lifecycle --
# label: lifecycle-file:transit-gateway-vpc-attachment-lifecycle
awscli ec2 create-transit-gateway --description VpcAttachTGW
# label: lifecycle-file:transit-gateway-vpc-attachment-lifecycle
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:transit-gateway-vpc-attachment-lifecycle
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:transit-gateway-vpc-attachment-lifecycle
awscli ec2 create-transit-gateway-vpc-attachment --transit-gateway-id tgw-0262a0e521EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:transit-gateway-vpc-attachment-lifecycle
awscli ec2 describe-transit-gateway-vpc-attachments --transit-gateway-attachment-ids tgw-attach-0d2c54bdbEXAMPLE
# label: lifecycle-file:transit-gateway-vpc-attachment-lifecycle
awscli ec2 delete-transit-gateway-vpc-attachment --transit-gateway-attachment-id tgw-attach-0d2c54bdbEXAMPLE

# -- verified-access-instance-lifecycle --
# label: lifecycle-file:verified-access-instance-lifecycle
awscli ec2 create-verified-access-instance --tag-specifications 'ResourceType=verified-access-instance,Tags=[{Key=Name,Value=lifecycle-va-instance}]'
# label: lifecycle-file:verified-access-instance-lifecycle
awscli ec2 describe-verified-access-instances --verified-access-instance-ids vai-0ce000c0b7EXAMPLE
# label: lifecycle-file:verified-access-instance-lifecycle
awscli ec2 modify-verified-access-instance --verified-access-instance-id vai-0ce000c0b7EXAMPLE --description 'Updated lifecycle instance'
# label: lifecycle-file:verified-access-instance-lifecycle
awscli ec2 describe-verified-access-instances --verified-access-instance-ids vai-0ce000c0b7EXAMPLE
# label: lifecycle-file:verified-access-instance-lifecycle
awscli ec2 delete-verified-access-instance --verified-access-instance-id vai-0ce000c0b7EXAMPLE

# -- verified-access-trust-provider-lifecycle --
# label: lifecycle-file:verified-access-trust-provider-lifecycle
awscli ec2 create-verified-access-trust-provider --trust-provider-type user --user-trust-provider-type iam-identity-center --policy-reference-name idc --tag-specifications 'ResourceType=verified-access-trust-provider,Tags=[{Key=Name,Value=lifecycle-tp}]'
# label: lifecycle-file:verified-access-trust-provider-lifecycle
awscli ec2 describe-verified-access-trust-providers --verified-access-trust-provider-ids vatp-0bb32de759EXAMPLE
# label: lifecycle-file:verified-access-trust-provider-lifecycle
awscli ec2 modify-verified-access-trust-provider --verified-access-trust-provider-id vatp-0bb32de759EXAMPLE --description 'Updated trust provider'
# label: lifecycle-file:verified-access-trust-provider-lifecycle
awscli ec2 delete-verified-access-trust-provider --verified-access-trust-provider-id vatp-0bb32de759EXAMPLE

# -- verified-access-group-lifecycle --
# label: lifecycle-file:verified-access-group-lifecycle
awscli ec2 create-verified-access-instance --description 'Group prerequisite'
# label: lifecycle-file:verified-access-group-lifecycle
awscli ec2 create-verified-access-group --verified-access-instance-id vai-0ce000c0b7EXAMPLE --tag-specifications 'ResourceType=verified-access-group,Tags=[{Key=Name,Value=lifecycle-va-group}]'
# label: lifecycle-file:verified-access-group-lifecycle
awscli ec2 describe-verified-access-groups --verified-access-group-ids vagr-0dbe967bafEXAMPLE
# label: lifecycle-file:verified-access-group-lifecycle
awscli ec2 modify-verified-access-group --verified-access-group-id vagr-0dbe967bafEXAMPLE --description 'Updated group'
# label: lifecycle-file:verified-access-group-lifecycle
awscli ec2 delete-verified-access-group --verified-access-group-id vagr-0dbe967bafEXAMPLE
# label: lifecycle-file:verified-access-group-lifecycle
awscli ec2 delete-verified-access-instance --verified-access-instance-id vai-0ce000c0b7EXAMPLE

# -- verified-access-endpoint-lifecycle --
# label: lifecycle-file:verified-access-endpoint-lifecycle
awscli ec2 create-verified-access-instance --description 'Endpoint prerequisite'
# label: lifecycle-file:verified-access-endpoint-lifecycle
awscli ec2 create-verified-access-group --verified-access-instance-id vai-0ce000c0b7EXAMPLE
# label: lifecycle-file:verified-access-endpoint-lifecycle
awscli ec2 create-verified-access-endpoint --verified-access-group-id vagr-0dbe967bafEXAMPLE --endpoint-type network-interface --attachment-type vpc --domain-certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/eb065ea0EXAMPLE --application-domain example.com --endpoint-domain-prefix my-app --security-group-ids sg-1234567890abcdef0 --network-interface-options NetworkInterfaceId=eni-070203f901EXAMPLE,Protocol=https,Port=443
# label: lifecycle-file:verified-access-endpoint-lifecycle
awscli ec2 describe-verified-access-endpoints --verified-access-endpoint-ids vae-066fac616dEXAMPLE
# label: lifecycle-file:verified-access-endpoint-lifecycle
awscli ec2 modify-verified-access-endpoint --verified-access-endpoint-id vae-066fac616dEXAMPLE --description 'Updated endpoint'
# label: lifecycle-file:verified-access-endpoint-lifecycle
awscli ec2 delete-verified-access-endpoint --verified-access-endpoint-id vae-066fac616dEXAMPLE

# -- vpc-endpoint-service-configuration-lifecycle --
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle
awscli ec2 create-vpc-endpoint-service-configuration --network-load-balancer-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532 --acceptance-required
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle
awscli ec2 describe-vpc-endpoint-service-configurations --service-ids vpce-svc-03d5ebb7d9EXAMPLE
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle
awscli ec2 modify-vpc-endpoint-service-configuration --service-id vpce-svc-03d5ebb7d9EXAMPLE --no-acceptance-required
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle
awscli ec2 describe-vpc-endpoint-service-configurations --service-ids vpce-svc-03d5ebb7d9EXAMPLE
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle
awscli ec2 delete-vpc-endpoint-service-configurations --service-ids vpce-svc-03d5ebb7d9EXAMPLE

# -- volume-lifecycle-v2 --
# label: lifecycle-file:volume-lifecycle-v2
awscli ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a
# label: lifecycle-file:volume-lifecycle-v2
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v2
awscli ec2 modify-volume --volume-id vol-1234567890abcdef0 --size 150
# label: lifecycle-file:volume-lifecycle-v2
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v2
awscli ec2 delete-volume --volume-id vol-1234567890abcdef0

# -- volume-lifecycle-v3 --
# label: lifecycle-file:volume-lifecycle-v3
awscli ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a
# label: lifecycle-file:volume-lifecycle-v3
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v3
awscli ec2 modify-volume --volume-id vol-1234567890abcdef0 --volume-type gp2
# label: lifecycle-file:volume-lifecycle-v3
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v3
awscli ec2 delete-volume --volume-id vol-1234567890abcdef0

# -- volume-lifecycle-v4 --
# label: lifecycle-file:volume-lifecycle-v4
awscli ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a
# label: lifecycle-file:volume-lifecycle-v4
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v4
awscli ec2 modify-volume --volume-id vol-1234567890abcdef0 --iops 6000
# label: lifecycle-file:volume-lifecycle-v4
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v4
awscli ec2 delete-volume --volume-id vol-1234567890abcdef0

# -- volume-lifecycle-v5 --
# label: lifecycle-file:volume-lifecycle-v5
awscli ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a
# label: lifecycle-file:volume-lifecycle-v5
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v5
awscli ec2 modify-volume --volume-id vol-1234567890abcdef0 --throughput 500
# label: lifecycle-file:volume-lifecycle-v5
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v5
awscli ec2 delete-volume --volume-id vol-1234567890abcdef0

# -- volume-lifecycle-v6 --
# label: lifecycle-file:volume-lifecycle-v6
awscli ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a
# label: lifecycle-file:volume-lifecycle-v6
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v6
awscli ec2 modify-volume --volume-id vol-1234567890abcdef0 --volume-type io2 --iops 3000 --size 100
# label: lifecycle-file:volume-lifecycle-v6
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v6
awscli ec2 delete-volume --volume-id vol-1234567890abcdef0

# -- instance-lifecycle-v2 --
# label: lifecycle-file:instance-lifecycle-v2
awscli ec2 register-image --name lifecycle-instance-v2-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}
# label: lifecycle-file:instance-lifecycle-v2
awscli ec2 run-instances --image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1
# label: lifecycle-file:instance-lifecycle-v2
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle-v2
awscli ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --source-dest-check "{\"Value\": false}"
# label: lifecycle-file:instance-lifecycle-v2
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle-v2
awscli ec2 terminate-instances --instance-ids i-1234567890abcdef0

# -- host-lifecycle-v2 --
# label: lifecycle-file:host-lifecycle-v2
awscli ec2 allocate-hosts --instance-type m5.large --availability-zone us-east-1a --quantity 1
# label: lifecycle-file:host-lifecycle-v2
awscli ec2 describe-hosts --host-ids h-0029d6e3cacf1b3da
# label: lifecycle-file:host-lifecycle-v2
awscli ec2 modify-hosts --host-ids h-0029d6e3cacf1b3da --host-recovery on
# label: lifecycle-file:host-lifecycle-v2
awscli ec2 describe-hosts --host-ids h-0029d6e3cacf1b3da
# label: lifecycle-file:host-lifecycle-v2
awscli ec2 release-hosts --host-ids h-0029d6e3cacf1b3da

# -- capacity-reservation-lifecycle-v2 --
# label: lifecycle-file:capacity-reservation-lifecycle-v2
awscli ec2 create-capacity-reservation --availability-zone us-east-1a --instance-type t2.medium --instance-platform Linux/UNIX --instance-count 3
# label: lifecycle-file:capacity-reservation-lifecycle-v2
awscli ec2 describe-capacity-reservations --capacity-reservation-ids cr-1234abcd56EXAMPLE
# label: lifecycle-file:capacity-reservation-lifecycle-v2
awscli ec2 modify-capacity-reservation --capacity-reservation-id cr-1234abcd56EXAMPLE --end-date-type limited --end-date 2029-12-31T23:59:59Z
# label: lifecycle-file:capacity-reservation-lifecycle-v2
awscli ec2 describe-capacity-reservations --capacity-reservation-ids cr-1234abcd56EXAMPLE
# label: lifecycle-file:capacity-reservation-lifecycle-v2
awscli ec2 cancel-capacity-reservation --capacity-reservation-id cr-1234abcd56EXAMPLE

# -- image-lifecycle-v2 --
# label: lifecycle-file:image-lifecycle-v2
awscli ec2 register-image --name lifecycle-image-v2 --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}
# label: lifecycle-file:image-lifecycle-v2
awscli ec2 describe-images --image-ids ami-1234567890EXAMPLE
# label: lifecycle-file:image-lifecycle-v2
awscli ec2 modify-image-attribute --image-id ami-1234567890EXAMPLE --launch-permission "Add=[{Group=all}]"
# label: lifecycle-file:image-lifecycle-v2
awscli ec2 describe-images --image-ids ami-1234567890EXAMPLE
# label: lifecycle-file:image-lifecycle-v2
awscli ec2 deregister-image --image-id ami-1234567890EXAMPLE

# -- network-interface-lifecycle-v2 --
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 create-network-interface --subnet-id subnet-0250c25a1fEXAMPLE --description "Lifecycle test ENI v2"
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 describe-network-interfaces --network-interface-ids eni-e5aa89a3EXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 modify-network-interface-attribute --network-interface-id eni-e5aa89a3EXAMPLE --description "Modified ENI description"
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 describe-network-interfaces --network-interface-ids eni-e5aa89a3EXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 delete-network-interface --network-interface-id eni-e5aa89a3EXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v2
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- network-interface-lifecycle-v3 --
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 create-network-interface --subnet-id subnet-0250c25a1fEXAMPLE --description "Lifecycle test ENI v3"
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 describe-network-interfaces --network-interface-ids eni-e5aa89a3EXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 modify-network-interface-attribute --network-interface-id eni-e5aa89a3EXAMPLE --no-source-dest-check
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 describe-network-interfaces --network-interface-ids eni-e5aa89a3EXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 delete-network-interface --network-interface-id eni-e5aa89a3EXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:network-interface-lifecycle-v3
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- security-group-lifecycle-v2 --
# label: lifecycle-file:security-group-lifecycle-v2
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:security-group-lifecycle-v2
awscli ec2 create-security-group --group-name lifecycle-sg-v2 --description "Lifecycle v2 security group" --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:security-group-lifecycle-v2
awscli ec2 describe-security-groups --group-ids sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle-v2
awscli ec2 authorize-security-group-ingress --group-id sg-1234567890abcdef0 --protocol tcp --port 443 --cidr 0.0.0.0/0
# label: lifecycle-file:security-group-lifecycle-v2
awscli ec2 describe-security-groups --group-ids sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle-v2
awscli ec2 delete-security-group --group-id sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle-v2
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- vpc-endpoint-service-configuration-lifecycle-v2 --
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle-v2
awscli ec2 create-vpc-endpoint-service-configuration --network-load-balancer-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532 --no-acceptance-required
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle-v2
awscli ec2 describe-vpc-endpoint-service-configurations --service-ids vpce-svc-03d5ebb7d9EXAMPLE
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle-v2
awscli ec2 modify-vpc-endpoint-service-configuration --service-id vpce-svc-03d5ebb7d9EXAMPLE --acceptance-required
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle-v2
awscli ec2 describe-vpc-endpoint-service-configurations --service-ids vpce-svc-03d5ebb7d9EXAMPLE
# label: lifecycle-file:vpc-endpoint-service-configuration-lifecycle-v2
awscli ec2 delete-vpc-endpoint-service-configurations --service-ids vpce-svc-03d5ebb7d9EXAMPLE

# -- transit-gateway-lifecycle-v2 --
# label: lifecycle-file:transit-gateway-lifecycle-v2
awscli ec2 create-transit-gateway --description OriginalTGW
# label: lifecycle-file:transit-gateway-lifecycle-v2
awscli ec2 describe-transit-gateways --transit-gateway-ids tgw-0262a0e521EXAMPLE
# label: lifecycle-file:transit-gateway-lifecycle-v2
awscli ec2 modify-transit-gateway --transit-gateway-id tgw-0262a0e521EXAMPLE --description UpdatedTGW
# label: lifecycle-file:transit-gateway-lifecycle-v2
awscli ec2 describe-transit-gateways --transit-gateway-ids tgw-0262a0e521EXAMPLE
# label: lifecycle-file:transit-gateway-lifecycle-v2
awscli ec2 delete-transit-gateway --transit-gateway-id tgw-0262a0e521EXAMPLE

# -- vpn-connection-lifecycle --
# label: lifecycle-file:vpn-connection-lifecycle
awscli ec2 create-customer-gateway --type ipsec.1 --public-ip 203.0.113.12 --bgp-asn 65534
# label: lifecycle-file:vpn-connection-lifecycle
awscli ec2 create-vpn-gateway --type ipsec.1
# label: lifecycle-file:vpn-connection-lifecycle
awscli ec2 create-vpn-connection --type ipsec.1 --customer-gateway-id cgw-001122334455aabbc --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2
# label: lifecycle-file:vpn-connection-lifecycle
awscli ec2 describe-vpn-connections --vpn-connection-ids vpn-12345678901234567
# label: lifecycle-file:vpn-connection-lifecycle
awscli ec2 modify-vpn-connection --vpn-connection-id vpn-12345678901234567 --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2
# label: lifecycle-file:vpn-connection-lifecycle
awscli ec2 delete-vpn-connection --vpn-connection-id vpn-12345678901234567

# -- local-gateway-route-table-lifecycle --
# label: lifecycle-file:local-gateway-route-table-lifecycle
awscli ec2 create-local-gateway-route-table --local-gateway-id lgw-1a2b3c4d5e6f7g8h9 --mode direct-vpc-routing
# label: lifecycle-file:local-gateway-route-table-lifecycle
awscli ec2 describe-local-gateway-route-tables --local-gateway-route-table-ids lgw-rtb-abcdefg123EXAMPLE
# label: lifecycle-file:local-gateway-route-table-lifecycle
awscli ec2 delete-local-gateway-route-table --local-gateway-route-table-id lgw-rtb-abcdefg123EXAMPLE

# -- instance-lifecycle-v3 --
# label: lifecycle-file:instance-lifecycle-v3
awscli ec2 register-image --name lifecycle-instance-v3-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}
# label: lifecycle-file:instance-lifecycle-v3
awscli ec2 run-instances --image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1
# label: lifecycle-file:instance-lifecycle-v3
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle-v3
awscli ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --disable-api-termination
# label: lifecycle-file:instance-lifecycle-v3
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle-v3
awscli ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --no-disable-api-termination
# label: lifecycle-file:instance-lifecycle-v3
awscli ec2 terminate-instances --instance-ids i-1234567890abcdef0

# -- instance-lifecycle-v4 --
# label: lifecycle-file:instance-lifecycle-v4
awscli ec2 register-image --name lifecycle-instance-v4-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}
# label: lifecycle-file:instance-lifecycle-v4
awscli ec2 run-instances --image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1
# label: lifecycle-file:instance-lifecycle-v4
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle-v4
awscli ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --ebs-optimized
# label: lifecycle-file:instance-lifecycle-v4
awscli ec2 describe-instances --instance-ids i-1234567890abcdef0
# label: lifecycle-file:instance-lifecycle-v4
awscli ec2 terminate-instances --instance-ids i-1234567890abcdef0

# -- subnet-lifecycle-v2 --
# label: lifecycle-file:subnet-lifecycle-v2
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:subnet-lifecycle-v2
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:subnet-lifecycle-v2
awscli ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle-v2
awscli ec2 modify-subnet-attribute --subnet-id subnet-0250c25a1fEXAMPLE --map-public-ip-on-launch
# label: lifecycle-file:subnet-lifecycle-v2
awscli ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle-v2
awscli ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle-v2
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- subnet-lifecycle-v3 --
# label: lifecycle-file:subnet-lifecycle-v3
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:subnet-lifecycle-v3
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:subnet-lifecycle-v3
awscli ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle-v3
awscli ec2 modify-subnet-attribute --subnet-id subnet-0250c25a1fEXAMPLE --enable-dns64
# label: lifecycle-file:subnet-lifecycle-v3
awscli ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle-v3
awscli ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:subnet-lifecycle-v3
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- vpc-lifecycle-v2 --
# label: lifecycle-file:vpc-lifecycle-v2
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:vpc-lifecycle-v2
awscli ec2 describe-vpcs --vpc-ids vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:vpc-lifecycle-v2
awscli ec2 modify-vpc-attribute --vpc-id vpc-0a60eb65b4EXAMPLE --enable-dns-hostnames
# label: lifecycle-file:vpc-lifecycle-v2
awscli ec2 describe-vpcs --vpc-ids vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:vpc-lifecycle-v2
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- vpc-lifecycle-v3 --
# label: lifecycle-file:vpc-lifecycle-v3
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:vpc-lifecycle-v3
awscli ec2 describe-vpcs --vpc-ids vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:vpc-lifecycle-v3
awscli ec2 modify-vpc-attribute --vpc-id vpc-0a60eb65b4EXAMPLE --no-enable-dns-support
# label: lifecycle-file:vpc-lifecycle-v3
awscli ec2 describe-vpcs --vpc-ids vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:vpc-lifecycle-v3
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- volume-lifecycle-v7 --
# label: lifecycle-file:volume-lifecycle-v7
awscli ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a
# label: lifecycle-file:volume-lifecycle-v7
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v7
awscli ec2 modify-volume-attribute --volume-id vol-1234567890abcdef0 --auto-enable-io
# label: lifecycle-file:volume-lifecycle-v7
awscli ec2 describe-volumes --volume-ids vol-1234567890abcdef0
# label: lifecycle-file:volume-lifecycle-v7
awscli ec2 delete-volume --volume-id vol-1234567890abcdef0

# -- security-group-lifecycle-v3 --
# label: lifecycle-file:security-group-lifecycle-v3
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:security-group-lifecycle-v3
awscli ec2 create-security-group --group-name lifecycle-sg-v3 --description "Lifecycle v3 security group" --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:security-group-lifecycle-v3
awscli ec2 describe-security-groups --group-ids sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle-v3
awscli ec2 authorize-security-group-egress --group-id sg-1234567890abcdef0 --protocol tcp --port 443 --cidr 0.0.0.0/0
# label: lifecycle-file:security-group-lifecycle-v3
awscli ec2 describe-security-groups --group-ids sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle-v3
awscli ec2 delete-security-group --group-id sg-1234567890abcdef0
# label: lifecycle-file:security-group-lifecycle-v3
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- image-lifecycle-v3 --
# label: lifecycle-file:image-lifecycle-v3
awscli ec2 register-image --name lifecycle-image-v3 --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}
# label: lifecycle-file:image-lifecycle-v3
awscli ec2 describe-images --image-ids ami-1234567890EXAMPLE
# label: lifecycle-file:image-lifecycle-v3
awscli ec2 modify-image-attribute --image-id ami-1234567890EXAMPLE --description "Edge case v3 description"
# label: lifecycle-file:image-lifecycle-v3
awscli ec2 describe-images --image-ids ami-1234567890EXAMPLE
# label: lifecycle-file:image-lifecycle-v3
awscli ec2 deregister-image --image-id ami-1234567890EXAMPLE

# -- capacity-reservation-lifecycle-v3 --
# label: lifecycle-file:capacity-reservation-lifecycle-v3
awscli ec2 create-capacity-reservation --availability-zone us-east-1a --instance-type t2.medium --instance-platform Linux/UNIX --instance-count 3
# label: lifecycle-file:capacity-reservation-lifecycle-v3
awscli ec2 describe-capacity-reservations --capacity-reservation-ids cr-1234abcd56EXAMPLE
# label: lifecycle-file:capacity-reservation-lifecycle-v3
awscli ec2 modify-capacity-reservation --capacity-reservation-id cr-1234abcd56EXAMPLE --instance-match-criteria open
# label: lifecycle-file:capacity-reservation-lifecycle-v3
awscli ec2 describe-capacity-reservations --capacity-reservation-ids cr-1234abcd56EXAMPLE
# label: lifecycle-file:capacity-reservation-lifecycle-v3
awscli ec2 cancel-capacity-reservation --capacity-reservation-id cr-1234abcd56EXAMPLE

# -- traffic-mirror-session-lifecycle-v2 --
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 create-network-interface --subnet-id subnet-0250c25a1fEXAMPLE --description tm-source
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 create-traffic-mirror-filter --description 'Session v2 filter'
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 create-traffic-mirror-target --description 'Session v2 target' --network-interface-id eni-070203f901EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 create-traffic-mirror-session --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE --network-interface-id eni-070203f901EXAMPLE --session-number 1 --traffic-mirror-filter-id tmf-04812ff784EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 describe-traffic-mirror-sessions --traffic-mirror-session-ids tms-0af3141ce5EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 modify-traffic-mirror-session --traffic-mirror-session-id tms-0af3141ce5EXAMPLE --description "Updated v2 session"
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 describe-traffic-mirror-sessions --traffic-mirror-session-ids tms-0af3141ce5EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 delete-traffic-mirror-session --traffic-mirror-session-id tms-0af3141ce5EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 delete-traffic-mirror-target --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 delete-traffic-mirror-filter --traffic-mirror-filter-id tmf-04812ff784EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 delete-network-interface --network-interface-id eni-070203f901EXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE
# label: lifecycle-file:traffic-mirror-session-lifecycle-v2
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

# -- vpc-peering-connection-lifecycle-v2 --
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 create-vpc --cidr-block 10.0.0.0/16
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 create-vpc --cidr-block 10.1.0.0/16
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 create-vpc-peering-connection --vpc-id vpc-0a60eb65b4EXAMPLE --peer-vpc-id vpc-11122233aaEXAMPLE
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 accept-vpc-peering-connection --vpc-peering-connection-id pcx-111aaa111EXAMPLE
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 describe-vpc-peering-connections --vpc-peering-connection-ids pcx-111aaa111EXAMPLE
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 delete-vpc-peering-connection --vpc-peering-connection-id pcx-111aaa111EXAMPLE
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE
# label: lifecycle-file:vpc-peering-connection-lifecycle-v2
awscli ec2 delete-vpc --vpc-id vpc-11122233aaEXAMPLE
