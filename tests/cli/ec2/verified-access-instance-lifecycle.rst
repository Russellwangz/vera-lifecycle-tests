**Example 1: To create a Verified Access instance**

The following ``create-verified-access-instance`` example creates a Verified Access instance. ::

    aws ec2 create-verified-access-instance \
        --tag-specifications 'ResourceType=verified-access-instance,Tags=[{Key=Name,Value=lifecycle-va-instance}]'

Output::

    {
        "VerifiedAccessInstance": {
            "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE",
            "CreationTime": "2023-01-01T00:00:00",
            "LastUpdatedTime": "2023-01-01T00:00:00"
        }
    }

**Example 2: To describe the Verified Access instance**

The following ``describe-verified-access-instances`` example retrieves details. ::

    aws ec2 describe-verified-access-instances \
        --verified-access-instance-ids vai-0ce000c0b7EXAMPLE

**Example 3: To modify the Verified Access instance**

The following ``modify-verified-access-instance`` example updates the description. ::

    aws ec2 modify-verified-access-instance \
        --verified-access-instance-id vai-0ce000c0b7EXAMPLE --description 'Updated lifecycle instance'

**Example 4: To describe after modification**

The following ``describe-verified-access-instances`` example verifies the update. ::

    aws ec2 describe-verified-access-instances \
        --verified-access-instance-ids vai-0ce000c0b7EXAMPLE

**Example 5: To delete the Verified Access instance**

The following ``delete-verified-access-instance`` example deletes the instance. ::

    aws ec2 delete-verified-access-instance \
        --verified-access-instance-id vai-0ce000c0b7EXAMPLE

