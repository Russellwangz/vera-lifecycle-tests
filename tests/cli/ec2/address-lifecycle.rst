**Example 1: To allocate an Elastic IP address**

The following ``allocate-address`` example allocates an Elastic IP address. ::

    aws ec2 allocate-address

Output::

    {
        "PublicIp": "70.224.234.241",
        "AllocationId": "eipalloc-01435ba59eEXAMPLE",
        "PublicIpv4Pool": "amazon",
        "NetworkBorderGroup": "us-east-1",
        "Domain": "vpc"
    }

**Example 2: To describe the Elastic IP address**

The following ``describe-addresses`` example retrieves details about the allocated Elastic IP address. ::

    aws ec2 describe-addresses --allocation-ids eipalloc-01435ba59eEXAMPLE

**Example 3: To release the Elastic IP address**

The following ``release-address`` example releases the Elastic IP address. ::

    aws ec2 release-address --allocation-id eipalloc-01435ba59eEXAMPLE

