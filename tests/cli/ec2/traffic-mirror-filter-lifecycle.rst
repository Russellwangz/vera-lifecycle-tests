**Example 1: To create a traffic mirror filter**

The following ``create-traffic-mirror-filter`` example creates a traffic mirror filter. ::

    aws ec2 create-traffic-mirror-filter --description 'Lifecycle TCP Filter'

Output::

    {
        "TrafficMirrorFilter": {
            "TrafficMirrorFilterId": "tmf-0be0b25fcdEXAMPLE",
            "Description": "Lifecycle TCP Filter"
        }
    }

**Example 2: To describe the traffic mirror filter**

The following ``describe-traffic-mirror-filters`` example retrieves details about the filter. ::

    aws ec2 describe-traffic-mirror-filters \
        --traffic-mirror-filter-ids tmf-0be0b25fcdEXAMPLE

**Example 3: To delete the traffic mirror filter**

The following ``delete-traffic-mirror-filter`` example deletes the filter. ::

    aws ec2 delete-traffic-mirror-filter \
        --traffic-mirror-filter-id tmf-0be0b25fcdEXAMPLE

