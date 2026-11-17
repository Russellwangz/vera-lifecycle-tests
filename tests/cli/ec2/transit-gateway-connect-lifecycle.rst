**Example 1: To create a transit gateway**

The following ``create-transit-gateway`` example creates a TGW as prerequisite. ::

    aws ec2 create-transit-gateway --description ConnectTGW

Output::

    {
        "TransitGateway": {
            "TransitGatewayId": "tgw-0262a0e521EXAMPLE",
            "State": "available"
        }
    }

**Example 2: To create a VPC attachment**

The following ``create-vpc`` example creates a VPC as prerequisite. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE"
        }
    }

**Example 3: To create a subnet for the attachment**

The following ``create-subnet`` example creates a subnet. ::

    aws ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24

Output::

    {
        "Subnet": {
            "SubnetId": "subnet-0250c25a1fEXAMPLE"
        }
    }

**Example 4: To create a transit gateway VPC attachment**

The following ``create-transit-gateway-vpc-attachment`` example creates a VPC attachment for the connect. ::

    aws ec2 create-transit-gateway-vpc-attachment \
        --transit-gateway-id tgw-0262a0e521EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE --subnet-ids subnet-0250c25a1fEXAMPLE

Output::

    {
        "TransitGatewayVpcAttachment": {
            "TransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE",
            "TransitGatewayId": "tgw-0262a0e521EXAMPLE"
        }
    }

**Example 5: To create a transit gateway connect**

The following ``create-transit-gateway-connect`` example creates a Connect attachment using GRE. ::

    aws ec2 create-transit-gateway-connect \
        --transport-transit-gateway-attachment-id tgw-attach-0a89069f57EXAMPLE --options Protocol=gre

Output::

    {
        "TransitGatewayConnect": {
            "TransitGatewayAttachmentId": "tgw-attach-037012e5dcEXAMPLE",
            "TransportTransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE"
        }
    }

**Example 6: To describe the transit gateway connect**

The following ``describe-transit-gateway-connects`` example retrieves details about the connect. ::

    aws ec2 describe-transit-gateway-connects \
        --transit-gateway-attachment-ids tgw-attach-037012e5dcEXAMPLE

**Example 7: To delete the transit gateway connect**

The following ``delete-transit-gateway-connect`` example deletes the connect. ::

    aws ec2 delete-transit-gateway-connect \
        --transit-gateway-attachment-id tgw-attach-037012e5dcEXAMPLE

