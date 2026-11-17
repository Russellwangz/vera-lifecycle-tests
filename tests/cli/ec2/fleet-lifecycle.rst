**Example 1: To create a launch template for the fleet**

The following ``create-launch-template`` example creates a launch template as prerequisite. ::

    aws ec2 create-launch-template \
        --launch-template-name lifecycle-fleet-lt --launch-template-data '{"ImageId":"ami-0abcdef1234567890","InstanceType":"t2.micro"}'

Output::

    {
        "LaunchTemplate": {
            "LaunchTemplateId": "lt-0e8c754449EXAMPLE",
            "LaunchTemplateName": "lifecycle-fleet-lt",
            "LatestVersionNumber": 1
        }
    }

**Example 2: To create an EC2 Fleet**

The following ``create-fleet`` example creates an EC2 Fleet. ::

    aws ec2 create-fleet \
        --type instant --launch-template-configs 'LaunchTemplateSpecification={LaunchTemplateId=lt-0e8c754449EXAMPLE,Version=1}' --target-capacity-specification TotalTargetCapacity=1,DefaultTargetCapacityType=on-demand

Output::

    {
        "FleetId": "fleet-12a34b55EXAMPLE",
        "Instances": []
    }

**Example 3: To describe the fleet**

The following ``describe-fleets`` example retrieves details about the fleet. ::

    aws ec2 describe-fleets --fleet-ids fleet-12a34b55EXAMPLE

**Example 4: To modify the fleet target capacity**

The following ``modify-fleet`` example modifies the fleet target capacity. ::

    aws ec2 modify-fleet \
        --fleet-id fleet-12a34b55EXAMPLE --target-capacity-specification TotalTargetCapacity=2

**Example 5: To delete the fleet**

The following ``delete-fleets`` example deletes the fleet. ::

    aws ec2 delete-fleets --fleet-ids fleet-12a34b55EXAMPLE --terminate-instances

**Example 6: To delete the launch template**

The following ``delete-launch-template`` example cleans up the launch template. ::

    aws ec2 delete-launch-template --launch-template-id lt-0e8c754449EXAMPLE

