**Example 1: To create a VPC**

The following ``create-vpc`` example creates a VPC as prerequisite. ::

    aws ec2 create-vpc \
        --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create a subnet**

The following ``create-subnet`` example creates a subnet as prerequisite. ::

    aws ec2 create-subnet \
        --vpc-id vpc-0a60eb65b4EXAMPLE \
        --cidr-block 10.0.1.0/24

Output::

    {
        "Subnet": {
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.1.0/24"
        }
    }

**Example 3: To create a network interface**

The following ``create-network-interface`` example creates a network interface in the subnet. ::

    aws ec2 create-network-interface \
        --subnet-id subnet-0250c25a1fEXAMPLE \
        --description "Lifecycle test ENI"

Output::

    {
        "NetworkInterface": {
            "NetworkInterfaceId": "eni-e5aa89a3EXAMPLE",
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "Description": "Lifecycle test ENI",
            "Status": "available"
        }
    }

**Example 4: To describe the network interface**

The following ``describe-network-interfaces`` example retrieves details. ::

    aws ec2 describe-network-interfaces \
        --network-interface-ids eni-e5aa89a3EXAMPLE

**Example 5: To delete the network interface**

The following ``delete-network-interface`` example deletes the ENI. ::

    aws ec2 delete-network-interface \
        --network-interface-id eni-e5aa89a3EXAMPLE

**Example 6: To delete the subnet**

The following ``delete-subnet`` example cleans up the subnet. ::

    aws ec2 delete-subnet \
        --subnet-id subnet-0250c25a1fEXAMPLE

**Example 7: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc \
        --vpc-id vpc-0a60eb65b4EXAMPLE
