**Example 1: To create a VPC for the NAT gateway**

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

The following ``create-subnet`` example creates a subnet as prerequisite. ::

    aws ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24

Output::

    {
        "Subnet": {
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.1.0/24"
        }
    }

**Example 3: To create a private NAT gateway**

The following ``create-nat-gateway`` example creates a private NAT gateway in the subnet. ::

    aws ec2 create-nat-gateway \
        --subnet-id subnet-0250c25a1fEXAMPLE --connectivity-type private

Output::

    {
        "NatGateway": {
            "NatGatewayId": "nat-0c61bf8a12EXAMPLE",
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "State": "available",
            "ConnectivityType": "private"
        }
    }

**Example 4: To describe the NAT gateway**

The following ``describe-nat-gateways`` example retrieves details about the NAT gateway. ::

    aws ec2 describe-nat-gateways --nat-gateway-ids nat-0c61bf8a12EXAMPLE

**Example 5: To delete the NAT gateway**

The following ``delete-nat-gateway`` example deletes the NAT gateway. ::

    aws ec2 delete-nat-gateway --nat-gateway-id nat-0c61bf8a12EXAMPLE

