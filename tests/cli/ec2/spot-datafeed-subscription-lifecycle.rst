**Example 1: To create a Spot datafeed subscription**

The following ``create-spot-datafeed-subscription`` example creates a Spot datafeed subscription. ::

    aws ec2 create-spot-datafeed-subscription \
        --bucket amzn-s3-demo-bucket --prefix spot-data-feed

Output::

    {
        "SpotDatafeedSubscription": {
            "Bucket": "amzn-s3-demo-bucket",
            "OwnerId": "123456789012",
            "Prefix": "spot-data-feed",
            "State": "Active"
        }
    }

**Example 2: To describe the Spot datafeed subscription**

The following ``describe-spot-datafeed-subscription`` example retrieves details about the subscription. ::

    aws ec2 describe-spot-datafeed-subscription

**Example 3: To delete the Spot datafeed subscription**

The following ``delete-spot-datafeed-subscription`` example deletes the subscription. ::

    aws ec2 delete-spot-datafeed-subscription

