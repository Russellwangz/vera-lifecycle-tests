**Example 1: To create an instance event window**

The following ``create-instance-event-window`` example creates an instance event window. ::

    aws ec2 create-instance-event-window \
        --time-range StartWeekDay=monday,StartHour=2,EndWeekDay=wednesday,EndHour=8 --tag-specifications 'ResourceType=instance-event-window,Tags=[{Key=Name,Value=lifecycle-test}]' --name lifecycle-event-window

Output::

    {
        "InstanceEventWindow": {
            "InstanceEventWindowId": "iew-0abcdef1234567890",
            "Name": "lifecycle-event-window",
            "TimeRanges": [{"StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8}],
            "State": "active"
        }
    }

**Example 2: To describe the instance event window**

The following ``describe-instance-event-windows`` example retrieves details about the event window. ::

    aws ec2 describe-instance-event-windows \
        --instance-event-window-ids iew-0abcdef1234567890

**Example 3: To modify the instance event window**

The following ``modify-instance-event-window`` example changes the time range. ::

    aws ec2 modify-instance-event-window \
        --instance-event-window-id iew-0abcdef1234567890 --time-range StartWeekDay=tuesday,StartHour=4,EndWeekDay=thursday,EndHour=10

**Example 4: To describe the instance event window after modification**

The following ``describe-instance-event-windows`` example verifies the time range was updated. ::

    aws ec2 describe-instance-event-windows \
        --instance-event-window-ids iew-0abcdef1234567890

**Example 5: To delete the instance event window**

The following ``delete-instance-event-window`` example deletes the event window. ::

    aws ec2 delete-instance-event-window \
        --instance-event-window-id iew-0abcdef1234567890

