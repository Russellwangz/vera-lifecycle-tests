**Example 1: To create a transit gateway peering attachment**

The following ``create-transit-gateway-peering-attachment`` example creates a peering attachment. ::

    aws ec2 create-transit-gateway-peering-attachment \
        --transit-gateway-id tgw-123abc05e04123abc --peer-transit-gateway-id tgw-11223344aabbcc112 --peer-account-id 123456789012 --peer-region us-east-2

Output::

    {
        "TransitGatewayPeeringAttachment": {
            "TransitGatewayAttachmentId": "tgw-attach-4455667788EXAMPLE",
            "RequesterTgwInfo": {"TransitGatewayId": "tgw-123abc05e04123abc"},
            "AccepterTgwInfo": {"TransitGatewayId": "tgw-11223344aabbcc112"},
            "State": "pendingAcceptance"
        }
    }

**Example 2: To describe the peering attachment**

The following ``describe-transit-gateway-peering-attachments`` example retrieves details. ::

    aws ec2 describe-transit-gateway-peering-attachments \
        --transit-gateway-attachment-ids tgw-attach-4455667788EXAMPLE

**Example 3: To delete the peering attachment**

The following ``delete-transit-gateway-peering-attachment`` example deletes the peering attachment. ::

    aws ec2 delete-transit-gateway-peering-attachment \
        --transit-gateway-attachment-id tgw-attach-4455667788EXAMPLE

