**Example 1: To create the customer gateway**

The following ``create-customer-gateway`` example creates a customer gateway resource. ::

    aws ec2 create-customer-gateway --type ipsec.1 --public-ip 12.1.2.3 --bgp-asn 65534

Output::

    {
        "CustomerGateway": {
            "CustomerGatewayId": "cgw-0e11f167",
            "State": "pending",
            "Type": "ipsec.1",
            "BgpAsn": "65534",
            "IpAddress": "12.1.2.3",
            "Tags": []
        }
    }

**Example 2: To describe the customer gateway**

The following ``describe-customer-gateways`` example retrieves details about the customer gateway to confirm it was created successfully. ::

    aws ec2 describe-customer-gateways

Output::

    {
        "CustomerGateways": [
            {
                "CustomerGatewayId": "cgw-0e11f167",
                "State": "available",
                "Type": "ipsec.1",
                "BgpAsn": "65534",
                "IpAddress": "12.1.2.3",
                "Tags": []
            }
        ]
    }

**Example 3: To delete the customer gateway**

The following ``delete-customer-gateway`` example deletes the customer gateway after validation. ::

    aws ec2 delete-customer-gateway --customer-gateway-id cgw-0e11f167
