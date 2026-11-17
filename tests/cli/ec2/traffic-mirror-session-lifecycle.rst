**Example 1: To create a traffic mirror filter**

The following ``create-traffic-mirror-filter`` example creates a filter as prerequisite. ::

    aws ec2 create-traffic-mirror-filter --description 'Session filter'

Output::

    {
        "TrafficMirrorFilter": {
            "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE"
        }
    }

**Example 2: To create a traffic mirror target**

The following ``create-traffic-mirror-target`` example creates a target as prerequisite. ::

    aws ec2 create-traffic-mirror-target \
        --description 'Session target' --network-interface-id eni-070203f901EXAMPLE

Output::

    {
        "TrafficMirrorTarget": {
            "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",
            "NetworkInterfaceId": "eni-070203f901EXAMPLE"
        }
    }

**Example 3: To create a traffic mirror session**

The following ``create-traffic-mirror-session`` example creates a traffic mirror session. ::

    aws ec2 create-traffic-mirror-session \
        --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE --network-interface-id eni-070203f901EXAMPLE --session-number 1 --traffic-mirror-filter-id tmf-04812ff784EXAMPLE

Output::

    {
        "TrafficMirrorSession": {
            "TrafficMirrorSessionId": "tms-0af3141ce5EXAMPLE",
            "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE",
            "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE",
            "SessionNumber": 1
        }
    }

**Example 4: To describe the traffic mirror session**

The following ``describe-traffic-mirror-sessions`` example retrieves details about the session. ::

    aws ec2 describe-traffic-mirror-sessions \
        --traffic-mirror-session-ids tms-0af3141ce5EXAMPLE

**Example 5: To modify the traffic mirror session**

The following ``modify-traffic-mirror-session`` example changes the session description. ::

    aws ec2 modify-traffic-mirror-session \
        --traffic-mirror-session-id tms-0af3141ce5EXAMPLE --description "Updated session"

**Example 6: To delete the traffic mirror session**

The following ``delete-traffic-mirror-session`` example deletes the session. ::

    aws ec2 delete-traffic-mirror-session \
        --traffic-mirror-session-id tms-0af3141ce5EXAMPLE

**Example 7: To delete the traffic mirror target**

The following ``delete-traffic-mirror-target`` example cleans up the target. ::

    aws ec2 delete-traffic-mirror-target \
        --traffic-mirror-target-id tmt-07f75d8feeEXAMPLE

**Example 8: To delete the traffic mirror filter**

The following ``delete-traffic-mirror-filter`` example cleans up the filter. ::

    aws ec2 delete-traffic-mirror-filter \
        --traffic-mirror-filter-id tmf-04812ff784EXAMPLE

