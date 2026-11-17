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

**Example 2: To create an internet gateway**

The following ``create-internet-gateway`` example creates an internet gateway. ::

    aws ec2 create-internet-gateway

Output::

    {
        "InternetGateway": {
            "InternetGatewayId": "igw-0d0fb496b3EXAMPLE",
            "Attachments": [],
            "Tags": []
        }
    }

**Example 3: To describe the internet gateway**

The following ``describe-internet-gateways`` example retrieves details about the internet gateway. ::

    aws ec2 describe-internet-gateways --internet-gateway-ids igw-0d0fb496b3EXAMPLE

**Example 4: To attach the internet gateway to the VPC**

The following ``attach-internet-gateway`` example attaches the internet gateway to the VPC. ::

    aws ec2 attach-internet-gateway \
        --internet-gateway-id igw-0d0fb496b3EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE

**Example 5: To detach the internet gateway from the VPC**

The following ``detach-internet-gateway`` example detaches the internet gateway. ::

    aws ec2 detach-internet-gateway \
        --internet-gateway-id igw-0d0fb496b3EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE

**Example 6: To delete the internet gateway**

The following ``delete-internet-gateway`` example deletes the internet gateway. ::

    aws ec2 delete-internet-gateway --internet-gateway-id igw-0d0fb496b3EXAMPLE

**Example 7: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

