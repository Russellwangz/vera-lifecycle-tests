**Example 1: To create a transit gateway**

The following ``create-transit-gateway`` example creates a transit gateway. ::

    aws ec2 create-transit-gateway \
        --description MyTGW --options AmazonSideAsn=64516,AutoAcceptSharedAttachments=enable,DefaultRouteTableAssociation=enable,DefaultRouteTablePropagation=enable,VpnEcmpSupport=enable,DnsSupport=enable

Output::

    {
        "TransitGateway": {
            "TransitGatewayId": "tgw-0262a0e521EXAMPLE",
            "State": "available",
            "Description": "MyTGW",
            "Options": {
                "AmazonSideAsn": 64516,
                "AutoAcceptSharedAttachments": "enable",
                "DnsSupport": "enable"
            }
        }
    }

**Example 2: To describe the transit gateway**

The following ``describe-transit-gateways`` example retrieves details about the transit gateway. ::

    aws ec2 describe-transit-gateways --transit-gateway-ids tgw-0262a0e521EXAMPLE

**Example 3: To modify the transit gateway**

The following ``modify-transit-gateway`` example disables VPN ECMP support. ::

    aws ec2 modify-transit-gateway \
        --transit-gateway-id tgw-0262a0e521EXAMPLE --options VpnEcmpSupport=disable

**Example 4: To describe the transit gateway after modification**

The following ``describe-transit-gateways`` example verifies the modification. ::

    aws ec2 describe-transit-gateways --transit-gateway-ids tgw-0262a0e521EXAMPLE

**Example 5: To delete the transit gateway**

The following ``delete-transit-gateway`` example deletes the transit gateway. ::

    aws ec2 delete-transit-gateway --transit-gateway-id tgw-0262a0e521EXAMPLE

