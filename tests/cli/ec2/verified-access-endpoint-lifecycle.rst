**Example 1: To create a Verified Access instance**

The following ``create-verified-access-instance`` example creates a VA instance. ::

    aws ec2 create-verified-access-instance --description 'Endpoint prerequisite'

Output::

    {
        "VerifiedAccessInstance": {
            "VerifiedAccessInstanceId": "vai-0ce000c0b7EXAMPLE"
        }
    }

**Example 2: To create a Verified Access group**

The following ``create-verified-access-group`` example creates a VA group. ::

    aws ec2 create-verified-access-group \
        --verified-access-instance-id vai-0ce000c0b7EXAMPLE

Output::

    {
        "VerifiedAccessGroup": {
            "VerifiedAccessGroupId": "vagr-0dbe967bafEXAMPLE"
        }
    }

**Example 3: To create a Verified Access endpoint**

The following ``create-verified-access-endpoint`` example creates a Verified Access endpoint. ::

    aws ec2 create-verified-access-endpoint \
        --verified-access-group-id vagr-0dbe967bafEXAMPLE --endpoint-type network-interface --attachment-type vpc --domain-certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/eb065ea0EXAMPLE --application-domain example.com --endpoint-domain-prefix my-app --security-group-ids sg-1234567890abcdef0 --network-interface-options NetworkInterfaceId=eni-070203f901EXAMPLE,Protocol=https,Port=443

Output::

    {
        "VerifiedAccessEndpoint": {
            "VerifiedAccessEndpointId": "vae-066fac616dEXAMPLE",
            "VerifiedAccessGroupId": "vagr-0dbe967bafEXAMPLE"
        }
    }

**Example 4: To describe the endpoint**

The following ``describe-verified-access-endpoints`` example retrieves details. ::

    aws ec2 describe-verified-access-endpoints \
        --verified-access-endpoint-ids vae-066fac616dEXAMPLE

**Example 5: To modify the endpoint**

The following ``modify-verified-access-endpoint`` example updates the description. ::

    aws ec2 modify-verified-access-endpoint \
        --verified-access-endpoint-id vae-066fac616dEXAMPLE --description 'Updated endpoint'

**Example 6: To delete the endpoint**

The following ``delete-verified-access-endpoint`` example deletes the endpoint. ::

    aws ec2 delete-verified-access-endpoint \
        --verified-access-endpoint-id vae-066fac616dEXAMPLE

