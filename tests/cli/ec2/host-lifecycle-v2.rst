**Example 1: To allocate a Dedicated Host**

The following ``allocate-hosts`` example allocates a Dedicated Host. ::

    aws ec2 allocate-hosts \
        --instance-type m5.large --availability-zone us-east-1a --quantity 1

Output::

    {
        "HostIds": ["h-0029d6e3cacf1b3da"]
    }

**Example 2: To describe the Dedicated Host**

The following ``describe-hosts`` example retrieves details about the Dedicated Host. ::

    aws ec2 describe-hosts --host-ids h-0029d6e3cacf1b3da

**Example 3: To enable host recovery**

The following ``modify-hosts`` example enables host recovery on the Dedicated Host. ::

    aws ec2 modify-hosts --host-ids h-0029d6e3cacf1b3da --host-recovery on

**Example 4: To describe the Dedicated Host after modification**

The following ``describe-hosts`` example verifies host recovery is enabled. ::

    aws ec2 describe-hosts --host-ids h-0029d6e3cacf1b3da

**Example 5: To release the Dedicated Host**

The following ``release-hosts`` example releases the Dedicated Host. ::

    aws ec2 release-hosts --host-ids h-0029d6e3cacf1b3da

