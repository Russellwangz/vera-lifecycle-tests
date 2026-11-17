**Example 1: To create a VPC for the endpoint**

The following ``create-vpc`` example creates a VPC as prerequisite. ::

    aws ec2 create-vpc \
        --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.0.0/16",
            "State": "available"
        }
    }

**Example 2: To create a route table for the gateway endpoint**

The following ``create-route-table`` example creates a route table. ::

    aws ec2 create-route-table \
        --vpc-id vpc-0a60eb65b4EXAMPLE

Output::

    {
        "RouteTable": {
            "RouteTableId": "rtb-22574640EXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "Routes": [
                {
                    "DestinationCidrBlock": "10.0.0.0/16",
                    "GatewayId": "local",
                    "State": "active"
                }
            ]
        }
    }

**Example 3: To create a gateway VPC endpoint for S3**

The following ``create-vpc-endpoint`` example creates a gateway endpoint. ::

    aws ec2 create-vpc-endpoint \
        --vpc-id vpc-0a60eb65b4EXAMPLE \
        --service-name com.amazonaws.us-east-1.s3 \
        --route-table-ids rtb-22574640EXAMPLE

Output::

    {
        "VpcEndpoint": {
            "VpcEndpointId": "vpce-032a826aEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "ServiceName": "com.amazonaws.us-east-1.s3",
            "State": "available",
            "VpcEndpointType": "Gateway"
        }
    }

**Example 4: To describe the VPC endpoint**

The following ``describe-vpc-endpoints`` example retrieves details. ::

    aws ec2 describe-vpc-endpoints \
        --vpc-endpoint-ids vpce-032a826aEXAMPLE

**Example 5: To delete the VPC endpoint**

The following ``delete-vpc-endpoints`` example deletes the endpoint. ::

    aws ec2 delete-vpc-endpoints \
        --vpc-endpoint-ids vpce-032a826aEXAMPLE

**Example 6: To delete the route table**

The following ``delete-route-table`` example cleans up. ::

    aws ec2 delete-route-table \
        --route-table-id rtb-22574640EXAMPLE

**Example 7: To delete the VPC**

The following ``delete-vpc`` example cleans up the VPC. ::

    aws ec2 delete-vpc \
        --vpc-id vpc-0a60eb65b4EXAMPLE
