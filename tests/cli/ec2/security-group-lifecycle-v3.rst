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

**Example 2: To create a security group**

The following ``create-security-group`` example creates a security group in the VPC. ::

    aws ec2 create-security-group \
        --group-name lifecycle-sg-v3 --description "Lifecycle v3 security group" --vpc-id vpc-0a60eb65b4EXAMPLE

Output::

    {
        "GroupId": "sg-1234567890abcdef0"
    }

**Example 3: To describe the security group**

The following ``describe-security-groups`` example retrieves details about the security group. ::

    aws ec2 describe-security-groups --group-ids sg-1234567890abcdef0

**Example 4: To authorize egress HTTPS access**

The following ``authorize-security-group-egress`` example adds an outbound rule for HTTPS. ::

    aws ec2 authorize-security-group-egress \
        --group-id sg-1234567890abcdef0 --protocol tcp --port 443 --cidr 0.0.0.0/0

**Example 5: To describe the security group after rule addition**

The following ``describe-security-groups`` example verifies the HTTPS egress rule was added. ::

    aws ec2 describe-security-groups --group-ids sg-1234567890abcdef0

**Example 6: To delete the security group**

The following ``delete-security-group`` example deletes the security group. ::

    aws ec2 delete-security-group --group-id sg-1234567890abcdef0

**Example 7: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

