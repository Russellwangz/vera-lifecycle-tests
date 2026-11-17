**Example 1: To create a network insights access scope**

The following ``create-network-insights-access-scope`` example creates an access scope for network analysis. ::

    aws ec2 create-network-insights-access-scope \
        --match-paths 'Source={ResourceStatement={ResourceTypes=[AWS::EC2::NetworkInterface]}}'

Output::

    {
        "NetworkInsightsAccessScope": {
            "NetworkInsightsAccessScopeId": "nis-123456789aEXAMPLE"
        },
        "NetworkInsightsAccessScopeContent": {
            "NetworkInsightsAccessScopeId": "nis-123456789aEXAMPLE"
        }
    }

**Example 2: To describe the access scope**

The following ``describe-network-insights-access-scopes`` example retrieves details about the access scope. ::

    aws ec2 describe-network-insights-access-scopes \
        --network-insights-access-scope-ids nis-123456789aEXAMPLE

**Example 3: To delete the access scope**

The following ``delete-network-insights-access-scope`` example deletes the access scope. ::

    aws ec2 delete-network-insights-access-scope \
        --network-insights-access-scope-id nis-123456789aEXAMPLE

