**Example 1: To create a VPC and internet gateway**

The following ``create-vpc`` example creates a VPC as prerequisite. ::

    aws ec2 create-vpc --cidr-block 10.0.0.0/16

Output::

    {
        "Vpc": {
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "State": "available"
        }
    }

**Example 2: To create an internet gateway**

The following ``create-internet-gateway`` example creates an IGW as prerequisite. ::

    aws ec2 create-internet-gateway

Output::

    {
        "InternetGateway": {
            "InternetGatewayId": "igw-0d0fb496b3EXAMPLE"
        }
    }

**Example 3: To create a network insights path**

The following ``create-network-insights-path`` example creates a path from IGW to VPC. ::

    aws ec2 create-network-insights-path \
        --source igw-0d0fb496b3EXAMPLE --destination vpc-0a60eb65b4EXAMPLE --protocol TCP

Output::

    {
        "NetworkInsightsPath": {
            "NetworkInsightsPathId": "nip-0b26f224f1EXAMPLE",
            "Source": "igw-0d0fb496b3EXAMPLE",
            "Destination": "vpc-0a60eb65b4EXAMPLE",
            "Protocol": "tcp"
        }
    }

**Example 4: To describe the network insights path**

The following ``describe-network-insights-paths`` example retrieves details about the path. ::

    aws ec2 describe-network-insights-paths \
        --network-insights-path-ids nip-0b26f224f1EXAMPLE

**Example 5: To delete the network insights path**

The following ``delete-network-insights-path`` example deletes the path. ::

    aws ec2 delete-network-insights-path \
        --network-insights-path-id nip-0b26f224f1EXAMPLE

