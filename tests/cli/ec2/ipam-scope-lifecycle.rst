**Example 1: To create an IPAM for the scope**

The following ``create-ipam`` example creates an IPAM as prerequisite. ::

    aws ec2 create-ipam \
        --description 'Scope prerequisite' --operating-regions RegionName=us-east-1

Output::

    {
        "Ipam": {
            "IpamId": "ipam-08440e7a3aEXAMPLE"
        }
    }

**Example 2: To create an IPAM scope**

The following ``create-ipam-scope`` example creates an IPAM scope. ::

    aws ec2 create-ipam-scope \
        --ipam-id ipam-08440e7a3aEXAMPLE --description 'Lifecycle test scope'

Output::

    {
        "IpamScope": {
            "IpamScopeId": "ipam-scope-01c1ebab2bEXAMPLE",
            "IpamId": "ipam-08440e7a3aEXAMPLE",
            "Description": "Lifecycle test scope",
            "State": "create-complete"
        }
    }

**Example 3: To describe the IPAM scope**

The following ``describe-ipam-scopes`` example retrieves details about the scope. ::

    aws ec2 describe-ipam-scopes --ipam-scope-ids ipam-scope-01c1ebab2bEXAMPLE

**Example 4: To modify the IPAM scope**

The following ``modify-ipam-scope`` example updates the description. ::

    aws ec2 modify-ipam-scope \
        --ipam-scope-id ipam-scope-01c1ebab2bEXAMPLE --description 'Updated scope'

**Example 5: To delete the IPAM scope**

The following ``delete-ipam-scope`` example deletes the IPAM scope. ::

    aws ec2 delete-ipam-scope --ipam-scope-id ipam-scope-01c1ebab2bEXAMPLE

**Example 6: To delete the IPAM**

The following ``delete-ipam`` example cleans up the IPAM. ::

    aws ec2 delete-ipam --ipam-id ipam-08440e7a3aEXAMPLE

