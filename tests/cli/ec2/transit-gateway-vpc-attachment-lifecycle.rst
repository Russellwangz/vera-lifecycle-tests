**Example 1: To create a transit gateway**

The following ``create-transit-gateway`` example creates a TGW as prerequisite. ::

    aws ec2 create-transit-gateway --description VpcAttachTGW

Output::

    {
        "TransitGateway": {
            "TransitGatewayId": "tgw-0262a0e521EXAMPLE"
        }
    }

**Example 2: To create a VPC**

The following ``create-vpc`` example creates a VPC. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE"
        }
    }

**Example 3: To create a subnet**

The following ``create-subnet`` example creates a subnet. ::

    aws ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24

Output::

    {
        "Subnet": {
            "SubnetId": "subnet-0250c25a1fEXAMPLE"
        }
    }

**Example 4: To create a transit gateway VPC attachment**

The following ``create-transit-gateway-vpc-attachment`` example creates a VPC attachment. ::

    aws ec2 create-transit-gateway-vpc-attachment \
        --transit-gateway-id tgw-0262a0e521EXAMPLE --vpc-id vpc-0a60eb65b4EXAMPLE --subnet-ids subnet-0250c25a1fEXAMPLE

Output::

    {
        "TransitGatewayVpcAttachment": {
            "TransitGatewayAttachmentId": "tgw-attach-0d2c54bdbEXAMPLE",
            "TransitGatewayId": "tgw-0262a0e521EXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE"
        }
    }

**Example 5: To describe the VPC attachment**

The following ``describe-transit-gateway-vpc-attachments`` example retrieves details. ::

    aws ec2 describe-transit-gateway-vpc-attachments \
        --transit-gateway-attachment-ids tgw-attach-0d2c54bdbEXAMPLE

**Example 6: To delete the VPC attachment**

The following ``delete-transit-gateway-vpc-attachment`` example deletes the attachment. ::

    aws ec2 delete-transit-gateway-vpc-attachment \
        --transit-gateway-attachment-id tgw-attach-0d2c54bdbEXAMPLE

