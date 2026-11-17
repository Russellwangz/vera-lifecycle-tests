**Example 1: To create a VPC endpoint service without acceptance**

The following ``create-vpc-endpoint-service-configuration`` example creates a VPC endpoint service without acceptance required. ::

    aws ec2 create-vpc-endpoint-service-configuration \
        --network-load-balancer-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532 --no-acceptance-required

Output::

    {
        "ServiceConfiguration": {
            "ServiceId": "vpce-svc-03d5ebb7d9EXAMPLE",
            "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-03d5ebb7d9EXAMPLE",
            "AcceptanceRequired": false
        }
    }

**Example 2: To describe the service configuration**

The following ``describe-vpc-endpoint-service-configurations`` example retrieves details. ::

    aws ec2 describe-vpc-endpoint-service-configurations \
        --service-ids vpce-svc-03d5ebb7d9EXAMPLE

**Example 3: To enable acceptance requirement**

The following ``modify-vpc-endpoint-service-configuration`` example enables acceptance requirement. ::

    aws ec2 modify-vpc-endpoint-service-configuration \
        --service-id vpce-svc-03d5ebb7d9EXAMPLE --acceptance-required

**Example 4: To describe after modification**

The following ``describe-vpc-endpoint-service-configurations`` example verifies acceptance is now required. ::

    aws ec2 describe-vpc-endpoint-service-configurations \
        --service-ids vpce-svc-03d5ebb7d9EXAMPLE

**Example 5: To delete the service configuration**

The following ``delete-vpc-endpoint-service-configurations`` example deletes the service. ::

    aws ec2 delete-vpc-endpoint-service-configurations \
        --service-ids vpce-svc-03d5ebb7d9EXAMPLE

