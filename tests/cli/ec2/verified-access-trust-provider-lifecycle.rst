**Example 1: To create a Verified Access trust provider**

The following ``create-verified-access-trust-provider`` example creates a trust provider. ::

    aws ec2 create-verified-access-trust-provider \
        --trust-provider-type user --user-trust-provider-type iam-identity-center --policy-reference-name idc --tag-specifications 'ResourceType=verified-access-trust-provider,Tags=[{Key=Name,Value=lifecycle-tp}]'

Output::

    {
        "VerifiedAccessTrustProvider": {
            "VerifiedAccessTrustProviderId": "vatp-0bb32de759EXAMPLE",
            "TrustProviderType": "user",
            "UserTrustProviderType": "iam-identity-center",
            "PolicyReferenceName": "idc"
        }
    }

**Example 2: To describe the trust provider**

The following ``describe-verified-access-trust-providers`` example retrieves details. ::

    aws ec2 describe-verified-access-trust-providers \
        --verified-access-trust-provider-ids vatp-0bb32de759EXAMPLE

**Example 3: To modify the trust provider**

The following ``modify-verified-access-trust-provider`` example updates the description. ::

    aws ec2 modify-verified-access-trust-provider \
        --verified-access-trust-provider-id vatp-0bb32de759EXAMPLE --description 'Updated trust provider'

**Example 4: To delete the trust provider**

The following ``delete-verified-access-trust-provider`` example deletes the trust provider. ::

    aws ec2 delete-verified-access-trust-provider \
        --verified-access-trust-provider-id vatp-0bb32de759EXAMPLE

