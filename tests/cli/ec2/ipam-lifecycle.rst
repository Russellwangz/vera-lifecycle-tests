**Example 1: To create an IPAM**

The following ``create-ipam`` example creates an IP Address Manager. ::

    aws ec2 create-ipam \
        --description 'Lifecycle test IPAM' --operating-regions RegionName=us-east-1 --tag-specifications 'ResourceType=ipam,Tags=[{Key=Name,Value=lifecycle-ipam}]'

Output::

    {
        "Ipam": {
            "IpamId": "ipam-08440e7a3aEXAMPLE",
            "Description": "Lifecycle test IPAM",
            "State": "create-complete"
        }
    }

**Example 2: To describe the IPAM**

The following ``describe-ipams`` example retrieves details about the IPAM. ::

    aws ec2 describe-ipams --ipam-ids ipam-08440e7a3aEXAMPLE

**Example 3: To modify the IPAM**

The following ``modify-ipam`` example adds an operating region to the IPAM. ::

    aws ec2 modify-ipam \
        --ipam-id ipam-08440e7a3aEXAMPLE --add-operating-regions RegionName=us-west-2

**Example 4: To describe the IPAM after modification**

The following ``describe-ipams`` example verifies the operating region was added. ::

    aws ec2 describe-ipams --ipam-ids ipam-08440e7a3aEXAMPLE

**Example 5: To delete the IPAM**

The following ``delete-ipam`` example deletes the IPAM. ::

    aws ec2 delete-ipam --ipam-id ipam-08440e7a3aEXAMPLE

