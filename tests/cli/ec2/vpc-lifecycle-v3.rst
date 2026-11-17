**Example 1: To create a VPC**

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

**Example 2: To describe the VPC**

The following ``describe-vpcs`` example retrieves details about the VPC. ::

    aws ec2 describe-vpcs --vpc-ids vpc-0a60eb65b4EXAMPLE

**Example 3: To disable DNS support on the VPC**

The following ``modify-vpc-attribute`` example disables DNS support. ::

    aws ec2 modify-vpc-attribute \
        --vpc-id vpc-0a60eb65b4EXAMPLE --no-enable-dns-support

**Example 4: To describe the VPC after modification**

The following ``describe-vpcs`` example verifies DNS support is disabled. ::

    aws ec2 describe-vpcs --vpc-ids vpc-0a60eb65b4EXAMPLE

**Example 5: To delete the VPC**

The following ``delete-vpc`` example deletes the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

