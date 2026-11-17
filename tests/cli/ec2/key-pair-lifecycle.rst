**Example 1: To create a key pair**

The following ``create-key-pair`` example creates a key pair. ::

    aws ec2 create-key-pair --key-name lifecycle-test-key --key-type rsa

Output::

    {
        "KeyFingerprint": "1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f",
        "KeyMaterial": "-----BEGIN RSA PRIVATE KEY-----\nEXAMPLE...\n-----END RSA PRIVATE KEY-----",
        "KeyName": "lifecycle-test-key",
        "KeyPairId": "key-0d4fb2e3caEXAMPLE"
    }

**Example 2: To describe the key pair**

The following ``describe-key-pairs`` example retrieves details about the key pair. ::

    aws ec2 describe-key-pairs --key-names lifecycle-test-key

**Example 3: To delete the key pair**

The following ``delete-key-pair`` example deletes the key pair. ::

    aws ec2 delete-key-pair --key-name lifecycle-test-key

