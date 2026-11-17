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

**Example 2: To create a network ACL**

The following ``create-network-acl`` example creates a network ACL in the VPC. ::

    aws ec2 create-network-acl --vpc-id vpc-0a60eb65b4EXAMPLE

Output::

    {
        "NetworkAcl": {
            "NetworkAclId": "acl-5fb85d36EXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "IsDefault": false
        }
    }

**Example 3: To describe the network ACL**

The following ``describe-network-acls`` example retrieves details about the network ACL. ::

    aws ec2 describe-network-acls --network-acl-ids acl-5fb85d36EXAMPLE

**Example 4: To delete the network ACL**

The following ``delete-network-acl`` example deletes the network ACL. ::

    aws ec2 delete-network-acl --network-acl-id acl-5fb85d36EXAMPLE

**Example 5: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

