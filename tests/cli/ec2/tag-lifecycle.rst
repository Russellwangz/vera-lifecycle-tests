**Example 1: To create a VPC to tag**

The following ``create-vpc`` example creates a VPC as the tagging target. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create tags on the VPC**

The following ``create-tags`` example adds Name and Environment tags to the VPC. ::

    aws ec2 create-tags \
        --resources vpc-0a60eb65b4EXAMPLE --tags Key=Name,Value=lifecycle-vpc Key=Environment,Value=test

**Example 3: To describe tags**

The following ``describe-tags`` example retrieves tags for the VPC. ::

    aws ec2 describe-tags --filters "Name=resource-id,Values=vpc-0a60eb65b4EXAMPLE"

**Example 4: To delete the Environment tag**

The following ``delete-tags`` example removes the Environment tag from the VPC. ::

    aws ec2 delete-tags --resources vpc-0a60eb65b4EXAMPLE --tags Key=Environment

**Example 5: To describe tags after deletion**

The following ``describe-tags`` example verifies the Environment tag was removed. ::

    aws ec2 describe-tags --filters "Name=resource-id,Values=vpc-0a60eb65b4EXAMPLE"

**Example 6: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

