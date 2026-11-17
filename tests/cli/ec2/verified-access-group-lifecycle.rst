**Example 1: To create a Verified Access instance for the group**

The following ``create-verified-access-instance`` example creates a VA instance as prerequisite. ::

    aws ec2 create-verified-access-instance --description 'Group prerequisite'

Output::

    {
        "VerifiedAccessInstance": {
            "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE"
        }
    }

**Example 2: To create a Verified Access group**

The following ``create-verified-access-group`` example creates a Verified Access group. ::

    aws ec2 create-verified-access-group \
        --verified-access-instance-id vai-0ce000c0b7EXAMPLE --tag-specifications 'ResourceType=verified-access-group,Tags=[{Key=Name,Value=lifecycle-va-group}]'

Output::

    {
        "VerifiedAccessGroup": {
            "VerifiedAccessGroupId": "vagr-0dbe967bafEXAMPLE",
            "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE"
        }
    }

**Example 3: To describe the Verified Access group**

The following ``describe-verified-access-groups`` example retrieves details. ::

    aws ec2 describe-verified-access-groups \
        --verified-access-group-ids vagr-0dbe967bafEXAMPLE

**Example 4: To modify the Verified Access group**

The following ``modify-verified-access-group`` example updates the description. ::

    aws ec2 modify-verified-access-group \
        --verified-access-group-id vagr-0dbe967bafEXAMPLE --description 'Updated group'

**Example 5: To delete the Verified Access group**

The following ``delete-verified-access-group`` example deletes the group. ::

    aws ec2 delete-verified-access-group \
        --verified-access-group-id vagr-0dbe967bafEXAMPLE

**Example 6: To delete the Verified Access instance**

The following ``delete-verified-access-instance`` example cleans up the VA instance. ::

    aws ec2 delete-verified-access-instance \
        --verified-access-instance-id vai-0ce000c0b7EXAMPLE

