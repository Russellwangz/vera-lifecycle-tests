**Example 1: To create a VPC**

The following ``create-vpc`` example creates a VPC as prerequisite. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create a subnet**

The following ``create-subnet`` example creates a subnet in the VPC. ::

    aws ec2 create-subnet \
        --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=lifecycle-subnet}]'

Output::

    {
        "Subnet": {
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.1.0/24",
            "State": "available"
        }
    }

**Example 3: To describe the subnet**

The following ``describe-subnets`` example retrieves details about the subnet. ::

    aws ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE

**Example 4: To modify the subnet to enable public IPs**

The following ``modify-subnet-attribute`` example enables auto-assign public IP on the subnet. ::

    aws ec2 modify-subnet-attribute \
        --subnet-id subnet-0250c25a1fEXAMPLE --map-public-ip-on-launch

**Example 5: To describe the subnet after modification**

The following ``describe-subnets`` example verifies public IP assignment is enabled. ::

    aws ec2 describe-subnets --subnet-ids subnet-0250c25a1fEXAMPLE

**Example 6: To delete the subnet**

The following ``delete-subnet`` example deletes the subnet. ::

    aws ec2 delete-subnet --subnet-id subnet-0250c25a1fEXAMPLE

**Example 7: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

