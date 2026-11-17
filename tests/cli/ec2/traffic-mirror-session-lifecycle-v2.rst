**Example 1: To create a VPC as prerequisite**

The following ``create-vpc`` example creates a VPC. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create a subnet as prerequisite**

The following ``create-subnet`` example creates a subnet in the VPC. ::

    aws ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24

Output::

    {
        "Subnet": {
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE"
        }
    }

**Example 3: To create a network interface as prerequisite**

The following ``create-network-interface`` example creates an ENI for traffic mirroring. ::

    aws ec2 create-network-interface \
        --subnet-id subnet-0250c25a1fEXAMPLE --description tm-source

Output::

    {
        "NetworkInterface": {
            "NetworkInterfaceId": "eni-070203f901EXAMPLE",
            "SubnetId": "subnet-0250c25a1fEXAMPLE"
        }
    }

**Example 4: To create a traffic mirror filter**

The following ``create-traffic-mirror-filter`` example creates a filter as prerequisite. ::

    aws ec2 create-traffic-mirror-filter --description 'Session v2 filter'

Output::

    {
        "TrafficMirrorFilter": {
            "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE"
        }
    }

**Example 5: To create a traffic mirror target**

The following ``create-traffic-mirror-target`` example creates a target as prerequisite. ::

    aws ec2 create-traffic-mirror-target \
        --description 'Session v2 target' --network-interface-id eni-070203f901EXAMPLE

Output::

    {
        "TrafficMirrorTarget": {
            "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",
            "NetworkInterfaceId": "eni-070203f901EXAMPLE"
        }
    }

**Example 6: To create a traffic mirror session**

The following ``create-traffic-mirror-session`` example creates a traffic mirror session. ::

    aws ec2 create-traffic-mirror-session \
        --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE --network-interface-id eni-070203f901EXAMPLE --session-number 1 --traffic-mirror-filter-id tmf-04812ff784EXAMPLE

Output::

    {
        "TrafficMirrorSession": {
            "TrafficMirrorSessionId": "tms-0af3141ce5EXAMPLE",
            "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",
            "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE",
            "SessionNumber": 1
        }
    }

**Example 7: To describe the traffic mirror session**

The following ``describe-traffic-mirror-sessions`` example retrieves details about the session. ::

    aws ec2 describe-traffic-mirror-sessions \
        --traffic-mirror-session-ids tms-0af3141ce5EXAMPLE

**Example 8: To modify the traffic mirror session description**

The following ``modify-traffic-mirror-session`` example updates the session description. ::

    aws ec2 modify-traffic-mirror-session \
        --traffic-mirror-session-id tms-0af3141ce5EXAMPLE --description "Updated v2 session"

**Example 9: To describe after modification**

The following ``describe-traffic-mirror-sessions`` example verifies the description was updated. ::

    aws ec2 describe-traffic-mirror-sessions \
        --traffic-mirror-session-ids tms-0af3141ce5EXAMPLE

**Example 10: To delete the traffic mirror session**

The following ``delete-traffic-mirror-session`` example deletes the session. ::

    aws ec2 delete-traffic-mirror-session \
        --traffic-mirror-session-id tms-0af3141ce5EXAMPLE

**Example 11: To delete the traffic mirror target**

The following ``delete-traffic-mirror-target`` example cleans up the target. ::

    aws ec2 delete-traffic-mirror-target \
        --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE

**Example 12: To delete the traffic mirror filter**

The following ``delete-traffic-mirror-filter`` example cleans up the filter. ::

    aws ec2 delete-traffic-mirror-filter \
        --traffic-mirror-filter-id tmf-04812ff784EXAMPLE

**Example 13: To delete the network interface**

The following ``delete-network-interface`` example cleans up the ENI. ::

    aws ec2 delete-network-interface --network-interface-id eni-070203f901EXAMPLE

**Example 14: To delete the subnet**

The following ``delete-subnet`` example cleans up the subnet. ::

    aws ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE

**Example 15: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

