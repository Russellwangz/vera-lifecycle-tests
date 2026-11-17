#!/usr/bin/env bash
# Auto-generated lifecycle bundle

# Subset: lifecycle tests whose name ends with -lifecycle-vN (N >= 2)

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
