**Example 1: To create an IPAM for the pool**

The following ``create-ipam`` example creates an IPAM as prerequisite. ::

    aws ec2 create-ipam \
        --description 'Pool prerequisite' --operating-regions RegionName=us-east-1

Output::

    {
        "Ipam": {
            "IpamId": "ipam-08440e7a3aEXAMPLE",
            "PublicDefaultScopeId": "ipam-scope-02fc38cd4cEXAMPLE",
            "PrivateDefaultScopeId": "ipam-scope-02fc38cd4cEXAMPLE"
        }
    }

**Example 2: To create an IPAM pool**

The following ``create-ipam-pool`` example creates an IPAM pool under the default scope. ::

    aws ec2 create-ipam-pool \
        --ipam-scope-id ipam-scope-02fc38cd4cEXAMPLE --address-family ipv4 --allocation-min-netmask-length 16 --allocation-max-netmask-length 26

Output::

    {
        "IpamPool": {
            "IpamPoolId": "ipam-pool-0533048da7EXAMPLE",
            "IpamScopeId": "ipam-scope-02fc38cd4cEXAMPLE",
            "AddressFamily": "ipv4",
            "State": "create-complete"
        }
    }

**Example 3: To describe the IPAM pool**

The following ``describe-ipam-pools`` example retrieves details about the IPAM pool. ::

    aws ec2 describe-ipam-pools --ipam-pool-ids ipam-pool-0533048da7EXAMPLE

**Example 4: To modify the IPAM pool**

The following ``modify-ipam-pool`` example modifies allocation settings on the pool. ::

    aws ec2 modify-ipam-pool \
        --ipam-pool-id ipam-pool-0533048da7EXAMPLE --allocation-min-netmask-length 14

**Example 5: To delete the IPAM pool**

The following ``delete-ipam-pool`` example deletes the IPAM pool. ::

    aws ec2 delete-ipam-pool --ipam-pool-id ipam-pool-0533048da7EXAMPLE

**Example 6: To delete the IPAM**

The following ``delete-ipam`` example cleans up the IPAM. ::

    aws ec2 delete-ipam --ipam-id ipam-08440e7a3aEXAMPLE

