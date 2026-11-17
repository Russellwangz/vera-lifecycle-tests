**Example 1: To create a VPC**

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

**Example 2: To create a route table**

The following ``create-route-table`` example creates a route table in the VPC. ::

    aws ec2 create-route-table --vpc-id vpc-0a60eb65b4EXAMPLE

Output::

    {
        "RouteTable": {
            "RouteTableId": "rtb-22574640EXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "Routes": [{"DestinationCidrBlock": "10.0.0.0/16", "GatewayId": "local", "State": "active"}]
        }
    }

**Example 3: To describe the route table**

The following ``describe-route-tables`` example retrieves details about the route table. ::

    aws ec2 describe-route-tables --route-table-ids rtb-22574640EXAMPLE

**Example 4: To delete the route table**

The following ``delete-route-table`` example deletes the route table. ::

    aws ec2 delete-route-table --route-table-id rtb-22574640EXAMPLE

**Example 5: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc --vpc-id vpc-0a60eb65b4EXAMPLE

