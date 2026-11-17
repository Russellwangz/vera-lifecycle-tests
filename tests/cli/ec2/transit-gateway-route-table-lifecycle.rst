**Example 1: To create a transit gateway**

The following ``create-transit-gateway`` example creates a TGW as prerequisite. ::

    aws ec2 create-transit-gateway --description RouteTGW

Output::

    {
        "TransitGateway": {
            "TransitGatewayId": "tgw-0262a0e521EXAMPLE"
        }
    }

**Example 2: To create a transit gateway route table**

The following ``create-transit-gateway-route-table`` example creates a route table. ::

    aws ec2 create-transit-gateway-route-table \
        --transit-gateway-id tgw-0262a0e521EXAMPLE

Output::

    {
        "TransitGatewayRouteTable": {
            "TransitGatewayRouteTableId": "tgw-rtb-0b6f6aaa01EXAMPLE",
            "TransitGatewayId": "tgw-0262a0e521EXAMPLE"
        }
    }

**Example 3: To describe the route table**

The following ``describe-transit-gateway-route-tables`` example retrieves details. ::

    aws ec2 describe-transit-gateway-route-tables \
        --transit-gateway-route-table-ids tgw-rtb-0b6f6aaa01EXAMPLE

**Example 4: To delete the route table**

The following ``delete-transit-gateway-route-table`` example deletes the route table. ::

    aws ec2 delete-transit-gateway-route-table \
        --transit-gateway-route-table-id tgw-rtb-0b6f6aaa01EXAMPLE

**Example 5: To delete the transit gateway**

The following ``delete-transit-gateway`` example cleans up the TGW. ::

    aws ec2 delete-transit-gateway --transit-gateway-id tgw-0262a0e521EXAMPLE

