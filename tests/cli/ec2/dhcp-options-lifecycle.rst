**Example 1: To create DHCP options**

The following ``create-dhcp-options`` example creates a DHCP options set. ::

    aws ec2 create-dhcp-options \
        --dhcp-configuration "Key=domain-name-servers,Values=10.2.5.1,10.2.5.2" "Key=domain-name,Values=example.com"

Output::

    {
        "DhcpOptions": {
            "DhcpOptionsId": "dopt-0a1b2c3d4eEXAMPLE",
            "DhcpConfigurations": [
                {"Key": "domain-name-servers", "Values": [{"Value": "10.2.5.1"}, {"Value": "10.2.5.2"}]},
                {"Key": "domain-name", "Values": [{"Value": "example.com"}]}
            ]
        }
    }

**Example 2: To describe the DHCP options**

The following ``describe-dhcp-options`` example retrieves details about the DHCP options. ::

    aws ec2 describe-dhcp-options --dhcp-options-ids dopt-0a1b2c3d4eEXAMPLE

**Example 3: To delete the DHCP options**

The following ``delete-dhcp-options`` example deletes the DHCP options set. ::

    aws ec2 delete-dhcp-options --dhcp-options-id dopt-0a1b2c3d4eEXAMPLE

