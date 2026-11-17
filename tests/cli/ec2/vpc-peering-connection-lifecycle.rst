**Example 1: To create the first VPC**

The following ``create-vpc`` example creates the requester VPC. ::

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

**Example 2: To create the second VPC**

The following ``create-vpc`` example creates the peer VPC. ::

    aws ec2 create-vpc \
        --cidr-block 10.1.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-11122233aaEXAMPLE",
            "CidrBlock": "10.1.0.0/16",
            "State": "available"
        }
    }

**Example 3: To create a VPC peering connection**

The following ``create-vpc-peering-connection`` example creates a peering connection between the two VPCs. ::

    aws ec2 create-vpc-peering-connection \
        --vpc-id vpc-0a60eb65b4EXAMPLE \
        --peer-vpc-id vpc-11122233aaEXAMPLE

Output::

    {
        "VpcPeeringConnection": {
            "VpcPeeringConnectionId": "pcx-1a2b3c4dEXAMPLE",
            "RequesterVpcInfo": {
                "VpcId": "vpc-0a60eb65b4EXAMPLE",
                "CidrBlock": "10.0.0.0/16"
            },
            "AccepterVpcInfo": {
                "VpcId": "vpc-11122233aaEXAMPLE",
                "CidrBlock": "10.1.0.0/16"
            },
            "Status": {
                "Code": "pending-acceptance"
            }
        }
    }

**Example 4: To describe the VPC peering connection**

The following ``describe-vpc-peering-connections`` example retrieves details. ::

    aws ec2 describe-vpc-peering-connections \
        --vpc-peering-connection-ids pcx-1a2b3c4dEXAMPLE

**Example 5: To delete the VPC peering connection**

The following ``delete-vpc-peering-connection`` example deletes the peering connection. ::

    aws ec2 delete-vpc-peering-connection \
        --vpc-peering-connection-id pcx-1a2b3c4dEXAMPLE

**Example 6: To delete the VPCs**

The following ``delete-vpc`` example cleans up the first VPC. ::

    aws ec2 delete-vpc \
        --vpc-id vpc-0a60eb65b4EXAMPLE

**Example 7: To delete the second VPC**

The following ``delete-vpc`` example cleans up the second VPC. ::

    aws ec2 delete-vpc \
        --vpc-id vpc-11122233aaEXAMPLE
