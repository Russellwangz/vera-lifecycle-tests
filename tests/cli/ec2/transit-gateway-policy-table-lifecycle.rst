**Example 1: To create a transit gateway**

The following ``create-transit-gateway`` example creates a TGW as prerequisite. ::

    aws ec2 create-transit-gateway --description PolicyTGW

Output::

    {
        "TransitGateway": {
            "TransitGatewayId": "tgw-067f8505c18f0bd6e"
        }
    }

**Example 2: To create a transit gateway policy table**

The following ``create-transit-gateway-policy-table`` example creates a policy table. ::

    aws ec2 create-transit-gateway-policy-table \
        --transit-gateway-id tgw-067f8505c18f0bd6e

Output::

    {
        "TransitGatewayPolicyTable": {
            "TransitGatewayPolicyTableId": "tgw-ptb-0a16f134b7EXAMPLE",
            "TransitGatewayId": "tgw-067f8505c18f0bd6e"
        }
    }

**Example 3: To describe the policy table**

The following ``describe-transit-gateway-policy-tables`` example retrieves details. ::

    aws ec2 describe-transit-gateway-policy-tables \
        --transit-gateway-policy-table-ids tgw-ptb-0a16f134b7EXAMPLE

**Example 4: To delete the policy table**

The following ``delete-transit-gateway-policy-table`` example deletes the policy table. ::

    aws ec2 delete-transit-gateway-policy-table \
        --transit-gateway-policy-table-id tgw-ptb-0a16f134b7EXAMPLE

**Example 5: To delete the transit gateway**

The following ``delete-transit-gateway`` example cleans up the TGW. ::

    aws ec2 delete-transit-gateway --transit-gateway-id tgw-067f8505c18f0bd6e

