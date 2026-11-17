**Example 1: To create a transit gateway connect peer**

The following ``create-transit-gateway-connect-peer`` example creates a Connect peer. ::

    aws ec2 create-transit-gateway-connect-peer \
        --transit-gateway-attachment-id tgw-attach-0f0927767cEXAMPLE --peer-address 172.31.1.11 --inside-cidr-blocks 169.254.6.0/29

Output::

    {
        "TransitGatewayConnectPeer": {
            "TransitGatewayConnectPeerId": "tgw-connect-peer-0666adbac4EXAMPLE",
            "TransitGatewayAttachmentId": "tgw-attach-0f0927767cEXAMPLE"
        }
    }

**Example 2: To describe the connect peer**

The following ``describe-transit-gateway-connect-peers`` example retrieves details about the peer. ::

    aws ec2 describe-transit-gateway-connect-peers \
        --transit-gateway-connect-peer-ids tgw-connect-peer-0666adbac4EXAMPLE

**Example 3: To delete the connect peer**

The following ``delete-transit-gateway-connect-peer`` example deletes the peer. ::

    aws ec2 delete-transit-gateway-connect-peer \
        --transit-gateway-connect-peer-id tgw-connect-peer-0666adbac4EXAMPLE

