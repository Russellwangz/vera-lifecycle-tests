**Example 1: To register an AMI**

The following ``register-image`` example registers an AMI. ::

    aws ec2 register-image \
        --name lifecycle-image-v3 --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}

Output::

    {
        "ImageId": "ami-1234567890EXAMPLE"
    }

**Example 2: To describe the AMI**

The following ``describe-images`` example retrieves details about the AMI. ::

    aws ec2 describe-images --image-ids ami-1234567890EXAMPLE

**Example 3: To modify the AMI description**

The following ``modify-image-attribute`` example updates the AMI description. ::

    aws ec2 modify-image-attribute \
        --image-id ami-1234567890EXAMPLE --description "Edge case v3 description"

**Example 4: To describe the AMI after modification**

The following ``describe-images`` example verifies the description was updated. ::

    aws ec2 describe-images --image-ids ami-1234567890EXAMPLE

**Example 5: To deregister the AMI**

The following ``deregister-image`` example deregisters the AMI. ::

    aws ec2 deregister-image --image-id ami-1234567890EXAMPLE

