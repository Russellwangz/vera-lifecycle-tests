**Example 1: To create a transit gateway**

The following ``create-transit-gateway`` example creates a TGW with multicast enabled. ::

    aws ec2 create-transit-gateway \
        --description MulticastTGW --options MulticastSupport=enable

Output::

    {
        "TransitGateway": {
            "TransitGatewayId": "tgw-0bf0bffefaEXAMPLE"
        }
    }

**Example 2: To create a transit gateway multicast domain**

The following ``create-transit-gateway-multicast-domain`` example creates a multicast domain. ::

    aws ec2 create-transit-gateway-multicast-domain \
        --transit-gateway-id tgw-0bf0bffefaEXAMPLE --options StaticSourcesSupport=disable,Igmpv2Support=enable

Output::

    {
        "TransitGatewayMulticastDomain": {
            "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef7EXAMPLE",
            "TransitGatewayId": "tgw-0bf0bffefaEXAMPLE"
        }
    }

**Example 3: To describe the multicast domain**

The following ``describe-transit-gateway-multicast-domains`` example retrieves details. ::

    aws ec2 describe-transit-gateway-multicast-domains \
        --transit-gateway-multicast-domain-ids tgw-mcast-domain-0c4905cef7EXAMPLE

**Example 4: To delete the multicast domain**

The following ``delete-transit-gateway-multicast-domain`` example deletes the multicast domain. ::

    aws ec2 delete-transit-gateway-multicast-domain \
        --transit-gateway-multicast-domain-id tgw-mcast-domain-0c4905cef7EXAMPLE

**Example 5: To delete the transit gateway**

The following ``delete-transit-gateway`` example cleans up the TGW. ::

    aws ec2 delete-transit-gateway --transit-gateway-id tgw-0bf0bffefaEXAMPLE

