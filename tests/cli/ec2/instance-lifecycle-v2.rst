**Example 1: To register an AMI for the instance**

The following ``register-image`` example registers a minimal AMI as prerequisite. ::

    aws ec2 register-image \
        --name lifecycle-instance-v2-ami --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={VolumeSize=8}

Output::

    {
        "ImageId": "ami-1234567890EXAMPLE"
    }

**Example 2: To launch an instance**

The following ``run-instances`` example launches an EC2 instance. ::

    aws ec2 run-instances \
        --image-id ami-1234567890EXAMPLE --instance-type t2.micro --count 1

Output::

    {
        "Instances": [
            {
                "InstanceId": "i-1234567890abcdef0",
                "InstanceType": "t2.micro",
                "State": {"Name": "pending", "Code": 0},
                "ImageId": "ami-1234567890EXAMPLE"
            }
        ]
    }

**Example 3: To describe the instance**

The following ``describe-instances`` example retrieves details about the launched instance. ::

    aws ec2 describe-instances --instance-ids i-1234567890abcdef0

**Example 4: To disable source/dest check on the instance**

The following ``modify-instance-attribute`` example disables the source/destination check. ::

    aws ec2 modify-instance-attribute \
        --instance-id i-1234567890abcdef0 --source-dest-check "{\"Value\": false}"

**Example 5: To describe the instance after modification**

The following ``describe-instances`` example verifies the source/dest check was disabled. ::

    aws ec2 describe-instances --instance-ids i-1234567890abcdef0

**Example 6: To terminate the instance**

The following ``terminate-instances`` example terminates the instance. ::

    aws ec2 terminate-instances --instance-ids i-1234567890abcdef0

