**Example 1: To create first VPC**

The following ``create-vpc`` example creates the requester VPC. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create second VPC**

The following ``create-vpc`` example creates the accepter VPC. ::

    aws ec2 create-vpc --cidr-block 10.1.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-11122233aaEXAMPLE",
            "CidrBlock": "10.1.0.0/16",
            "State": "available"
        }
    }

**Example 3: To create a VPC peering connection**

The following ``create-vpc-peering-connection`` example creates a peering connection between VPCs. ::

    aws ec2 create-vpc-peering-connection \
        --vpc-id vpc-0a60eb65b4EXAMPLE --peer-vpc-id vpc-11122233aaEXAMPLE

Output::

    {
        "VpcPeeringConnection": {
            "VpcPeeringConnectionId": "pcx-111aaa111EXAMPLE",
            "RequesterVpcInfo": {"VpcId": "vpc-0a60eb65b4EXAMPLE"},
            "AccepterVpcInfo": {"VpcId": "vpc-11122233aaEXAMPLE"},
            "Status": {"Code": "initiating-request"}
        }
    }

**Example 4: To accept the VPC peering connection**

The following ``accept-vpc-peering-connection`` example accepts the peering connection. ::

    aws ec2 accept-vpc-peering-connection \
        --vpc-peering-connection-id pcx-111aaa111EXAMPLE

**Example 5: To describe the peering connection**

The following ``describe-vpc-peering-connections`` example retrieves details about the peering. ::

    aws ec2 describe-vpc-peering-connections \
        --vpc-peering-connection-ids pcx-111aaa111EXAMPLE

**Example 6: To delete the VPC peering connection**

The following ``delete-vpc-peering-connection`` example deletes the peering connection. ::

    aws ec2 delete-vpc-peering-connection \
        --vpc-peering-connection-id pcx-111aaa111EXAMPLE

**Example 7: To delete first VPC**

The following ``delete-vpc`` example cleans up the requester VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

**Example 8: To delete second VPC**

The following ``delete-vpc`` example cleans up the accepter VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-11122233aaEXAMPLE

