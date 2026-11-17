**Example 1: To create a gp3 EBS volume**

The following ``create-volume`` example creates a 100 GiB gp3 volume. ::

    aws ec2 create-volume \
        --volume-type gp3 \
        --size 100 \
        --availability-zone us-east-1a

Output::

    {
        "AvailabilityZone": "us-east-1a",
        "Encrypted": false,
        "VolumeType": "gp3",
        "VolumeId": "vol-1234567890abcdef0",
        "State": "creating",
        "Iops": 3000,
        "Size": 100
    }

**Example 2: To describe the volume**

The following ``describe-volumes`` example retrieves details about the volume. ::

    aws ec2 describe-volumes \
        --volume-ids vol-1234567890abcdef0

**Example 3: To check the volume status**

The following ``describe-volume-status`` example checks the health status. ::

    aws ec2 describe-volume-status \
        --volume-ids vol-1234567890abcdef0

**Example 4: To modify the volume size and type**

The following ``modify-volume`` example increases the volume to 200 GiB io1. ::

    aws ec2 modify-volume \
        --volume-id vol-1234567890abcdef0 \
        --volume-type io1 \
        --iops 4000 \
        --size 200

**Example 5: To delete the volume**

The following ``delete-volume`` example deletes the volume. ::

    aws ec2 delete-volume \
        --volume-id vol-1234567890abcdef0
