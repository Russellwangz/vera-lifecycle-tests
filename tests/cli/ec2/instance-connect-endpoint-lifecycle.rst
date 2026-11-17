**Example 1: To create a VPC and subnet**

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

**Example 2: To create a subnet**

The following ``create-subnet`` example creates a subnet as prerequisite. ::

    aws ec2 create-subnet --vpc-id vpc-0a60eb65b4EXAMPLE --cidr-block 10.0.1.0/24

Output::

    {
        "Subnet": {
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "CidrBlock": "10.0.1.0/24"
        }
    }

**Example 3: To create an Instance Connect Endpoint**

The following ``create-instance-connect-endpoint`` example creates an Instance Connect Endpoint in the subnet. ::

    aws ec2 create-instance-connect-endpoint --subnet-id subnet-0250c25a1fEXAMPLE

Output::

    {
        "InstanceConnectEndpoint": {
            "InstanceConnectEndpointId": "eice-03f5e49b83EXAMPLE",
            "SubnetId": "subnet-0250c25a1fEXAMPLE",
            "VpcId": "vpc-0a60eb65b4EXAMPLE",
            "State": "create-complete"
        }
    }

**Example 4: To describe the Instance Connect Endpoint**

The following ``describe-instance-connect-endpoints`` example retrieves details about the endpoint. ::

    aws ec2 describe-instance-connect-endpoints \
        --instance-connect-endpoint-ids eice-03f5e49b83EXAMPLE

**Example 5: To delete the Instance Connect Endpoint**

The following ``delete-instance-connect-endpoint`` example deletes the endpoint. ::

    aws ec2 delete-instance-connect-endpoint \
        --instance-connect-endpoint-id eice-03f5e49b83EXAMPLE

