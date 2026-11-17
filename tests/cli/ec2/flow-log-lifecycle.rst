**Example 1: To create a VPC for flow logs**

The following ``create-vpc`` example creates a VPC as prerequisite. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create a flow log for the VPC**

The following ``create-flow-logs`` example creates a flow log that captures all traffic for the VPC. ::

    aws ec2 create-flow-logs \
        --resource-type VPC --resource-ids vpc-0a60eb65b4EXAMPLE --traffic-type ALL --log-destination-type cloud-watch-logs --log-group-name my-flow-logs

Output::

    {
        "ClientToken": "abc123",
        "FlowLogIds": ["fl-11223344556677889"],
        "Unsuccessful": []
    }

**Example 3: To describe the flow log**

The following ``describe-flow-logs`` example retrieves details about the flow log. ::

    aws ec2 describe-flow-logs --flow-log-ids fl-11223344556677889

**Example 4: To delete the flow log**

The following ``delete-flow-logs`` example deletes the flow log. ::

    aws ec2 delete-flow-logs --flow-log-ids fl-11223344556677889

**Example 5: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

