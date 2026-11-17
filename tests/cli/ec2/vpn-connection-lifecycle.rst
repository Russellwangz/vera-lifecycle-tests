**Example 1: To create a customer gateway**

The following ``create-customer-gateway`` example creates a customer gateway as prerequisite. ::

    aws ec2 create-customer-gateway \
        --type ipsec.1 --public-ip 203.0.113.12 --bgp-asn 65534

Output::

    {
        "CustomerGateway": {
            "CustomerGatewayId": "cgw-001122334455aabbc",
            "BgpAsn": "65534",
            "IpAddress": "203.0.113.12",
            "Type": "ipsec.1",
            "State": "available"
        }
    }

**Example 2: To create a virtual private gateway**

The following ``create-vpn-gateway`` example creates a VPN gateway as prerequisite. ::

    aws ec2 create-vpn-gateway --type ipsec.1

Output::

    {
        "VpnGateway": {
            "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2",
            "Type": "ipsec.1",
            "State": "available"
        }
    }

**Example 3: To create a VPN connection**

The following ``create-vpn-connection`` example creates a site-to-site VPN connection. ::

    aws ec2 create-vpn-connection \
        --type ipsec.1 --customer-gateway-id cgw-001122334455aabbc --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2

Output::

    {
        "VpnConnection": {
            "VpnConnectionId": "vpn-12345678901234567",
            "CustomerGatewayId": "cgw-001122334455aabbc",
            "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2",
            "State": "pending"
        }
    }

**Example 4: To describe the VPN connection**

The following ``describe-vpn-connections`` example retrieves details about the VPN connection. ::

    aws ec2 describe-vpn-connections --vpn-connection-ids vpn-12345678901234567

**Example 5: To modify the VPN connection**

The following ``modify-vpn-connection`` example changes the VPN gateway for the connection. ::

    aws ec2 modify-vpn-connection \
        --vpn-connection-id vpn-12345678901234567 --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2

**Example 6: To delete the VPN connection**

The following ``delete-vpn-connection`` example deletes the VPN connection. ::

    aws ec2 delete-vpn-connection --vpn-connection-id vpn-12345678901234567

