**Example 1: To create a traffic mirror target**

The following ``create-traffic-mirror-target`` example creates a traffic mirror target using a network interface. ::

    aws ec2 create-traffic-mirror-target \
        --description 'Lifecycle target' --network-interface-id eni-070203f901EXAMPLE

Output::

    {
        "TrafficMirrorTarget": {
            "TrafficMirrorTargetId": "tmt-060f48ce9EXAMPLE",
            "NetworkInterfaceId": "eni-070203f901EXAMPLE",
            "Description": "Lifecycle target"
        }
    }

**Example 2: To describe the traffic mirror target**

The following ``describe-traffic-mirror-targets`` example retrieves details about the target. ::

    aws ec2 describe-traffic-mirror-targets \
        --traffic-mirror-target-ids tmt-060f48ce9EXAMPLE

**Example 3: To delete the traffic mirror target**

The following ``delete-traffic-mirror-target`` example deletes the target. ::

    aws ec2 delete-traffic-mirror-target \
        --traffic-mirror-target-id tmt-060f48ce9EXAMPLE

