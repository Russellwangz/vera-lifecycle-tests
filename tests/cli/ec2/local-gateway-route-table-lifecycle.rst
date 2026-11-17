**Example 1: To create a local gateway route table**

The following ``create-local-gateway-route-table`` example creates a local gateway route table. ::

    aws ec2 create-local-gateway-route-table \
        --local-gateway-id lgw-1a2b3c4d5e6f7g8h9 --mode direct-vpc-routing

Output::

    {
        "LocalGatewayRouteTable": {
            "LocalGatewayRouteTableId": "lgw-rtb-abcdefg123EXAMPLE",
            "LocalGatewayId": "lgw-1a2b3c4d5e6f7g8h9",
            "Mode": "direct-vpc-routing"
        }
    }

**Example 2: To describe the local gateway route table**

The following ``describe-local-gateway-route-tables`` example retrieves details. ::

    aws ec2 describe-local-gateway-route-tables \
        --local-gateway-route-table-ids lgw-rtb-abcdefg123EXAMPLE

**Example 3: To delete the local gateway route table**

The following ``delete-local-gateway-route-table`` example deletes the route table. ::

    aws ec2 delete-local-gateway-route-table \
        --local-gateway-route-table-id lgw-rtb-abcdefg123EXAMPLE

