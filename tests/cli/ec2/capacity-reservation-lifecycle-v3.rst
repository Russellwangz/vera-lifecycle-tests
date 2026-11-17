**Example 1: To create a Capacity Reservation**

The following ``create-capacity-reservation`` example creates a Capacity Reservation. ::

    aws ec2 create-capacity-reservation \
        --availability-zone us-east-1a --instance-type t2.medium --instance-platform Linux/UNIX --instance-count 3

Output::

    {
        "CapacityReservation": {
            "CapacityReservationId": "cr-1234abcd56EXAMPLE",
            "InstanceType": "t2.medium",
            "InstancePlatform": "Linux/UNIX",
            "AvailabilityZone": "us-east-1a",
            "TotalInstanceCount": 3,
            "AvailableInstanceCount": 3,
            "State": "active"
        }
    }

**Example 2: To describe the Capacity Reservation**

The following ``describe-capacity-reservations`` example retrieves details about the Capacity Reservation. ::

    aws ec2 describe-capacity-reservations \
        --capacity-reservation-ids cr-1234abcd56EXAMPLE

**Example 3: To modify the Capacity Reservation match criteria**

The following ``modify-capacity-reservation`` example changes the instance match criteria to open. ::

    aws ec2 modify-capacity-reservation \
        --capacity-reservation-id cr-1234abcd56EXAMPLE --instance-match-criteria open

**Example 4: To describe the Capacity Reservation after modification**

The following ``describe-capacity-reservations`` example verifies the match criteria was changed. ::

    aws ec2 describe-capacity-reservations \
        --capacity-reservation-ids cr-1234abcd56EXAMPLE

**Example 5: To cancel the Capacity Reservation**

The following ``cancel-capacity-reservation`` example cancels the Capacity Reservation. ::

    aws ec2 cancel-capacity-reservation \
        --capacity-reservation-id cr-1234abcd56EXAMPLE

