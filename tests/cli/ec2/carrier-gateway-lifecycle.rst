**Example 1: To create a VPC for the carrier gateway**

The following ``create-vpc`` example creates a VPC as a prerequisite. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create a carrier gateway**

The following ``create-carrier-gateway`` example creates a carrier gateway in the VPC. ::

    aws ec2 create-carrier-gateway --vpc-id vpc-0a60eb65b4EXAMPLE

Output::

    {
        "CarrierGateway": {
            "CarrierGatewayId": "cagw-0465cdEXAMPLE1111",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "State": "available"
        }
    }

**Example 3: To describe the carrier gateway**

The following ``describe-carrier-gateways`` example retrieves details about the carrier gateway. ::

    aws ec2 describe-carrier-gateways --carrier-gateway-ids cagw-0465cdEXAMPLE1111

**Example 4: To delete the carrier gateway**

The following ``delete-carrier-gateway`` example deletes the carrier gateway. ::

    aws ec2 delete-carrier-gateway --carrier-gateway-id cagw-0465cdEXAMPLE1111

**Example 5: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

