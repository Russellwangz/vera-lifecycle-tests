**Example 1: To create a managed prefix list**

The following ``create-managed-prefix-list`` example creates a managed prefix list. ::

    aws ec2 create-managed-prefix-list \
        --address-family IPv4 --max-entries 10 --entries Cidr=10.0.0.0/16,Description=vpc-a --prefix-list-name lifecycle-prefix-list

Output::

    {
        "PrefixList": {
            "PrefixListId": "pl-0123456abcEXAMPLE",
            "AddressFamily": "IPv4",
            "State": "create-complete",
            "PrefixListName": "lifecycle-prefix-list",
            "MaxEntries": 10,
            "Version": 1
        }
    }

**Example 2: To describe the prefix list**

The following ``describe-managed-prefix-lists`` example retrieves details about the prefix list. ::

    aws ec2 describe-managed-prefix-lists --prefix-list-ids pl-0123456abcEXAMPLE

**Example 3: To modify the prefix list**

The following ``modify-managed-prefix-list`` example adds an entry to the prefix list. ::

    aws ec2 modify-managed-prefix-list \
        --prefix-list-id pl-0123456abcEXAMPLE --add-entries Cidr=10.2.0.0/16,Description=vpc-b --current-version 1

**Example 4: To describe the prefix list after modification**

The following ``describe-managed-prefix-lists`` example verifies the entry was added. ::

    aws ec2 describe-managed-prefix-lists --prefix-list-ids pl-0123456abcEXAMPLE

**Example 5: To delete the prefix list**

The following ``delete-managed-prefix-list`` example deletes the prefix list. ::

    aws ec2 delete-managed-prefix-list --prefix-list-id pl-0123456abcEXAMPLE

