**Example 1: To create the placement group**

The following ``create-placement-group`` example creates a placement group resource. ::

    aws ec2 create-placement-group --group-name my-cluster --strategy cluster

Output::

    {
        "PlacementGroup": {
            "GroupName": "my-cluster",
            "State": "pending",
            "Strategy": "cluster",
            "GroupId": "pg-01234567890abcdef"
        }
    }

**Example 2: To describe the placement group**

The following ``describe-placement-groups`` example retrieves details about the placement group to confirm it was created successfully. ::

    aws ec2 describe-placement-groups --group-names my-cluster

Output::

    {
        "PlacementGroups": [
            {
                "GroupName": "my-cluster",
                "State": "available",
                "Strategy": "cluster",
                "GroupId": "pg-01234567890abcdef"
            }
        ]
    }

**Example 3: To delete the placement group**

The following ``delete-placement-group`` example deletes the placement group after validation. ::

    aws ec2 delete-placement-group --group-name my-cluster
