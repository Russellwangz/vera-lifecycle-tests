**Example 1: To create an IPAM resource discovery**

The following ``create-ipam-resource-discovery`` example creates an IPAM resource discovery. ::

    aws ec2 create-ipam-resource-discovery \
        --description 'Lifecycle test discovery' --operating-regions RegionName=us-east-1 --tag-specifications 'ResourceType=ipam-resource-discovery,Tags=[{Key=Name,Value=lifecycle-disc}]'

Output::

    {
        "IpamResourceDiscovery": {
            "IpamResourceDiscoveryId": "ipam-res-disco-0e39761475EXAMPLE",
            "Description": "Lifecycle test discovery",
            "State": "create-complete"
        }
    }

**Example 2: To describe the resource discovery**

The following ``describe-ipam-resource-discoveries`` example retrieves details about the discovery. ::

    aws ec2 describe-ipam-resource-discoveries \
        --ipam-resource-discovery-ids ipam-res-disco-0e39761475EXAMPLE

**Example 3: To modify the resource discovery**

The following ``modify-ipam-resource-discovery`` example adds an operating region. ::

    aws ec2 modify-ipam-resource-discovery \
        --ipam-resource-discovery-id ipam-res-disco-0e39761475EXAMPLE --add-operating-regions RegionName=us-west-1

**Example 4: To delete the resource discovery**

The following ``delete-ipam-resource-discovery`` example deletes the resource discovery. ::

    aws ec2 delete-ipam-resource-discovery \
        --ipam-resource-discovery-id ipam-res-disco-0e39761475EXAMPLE

