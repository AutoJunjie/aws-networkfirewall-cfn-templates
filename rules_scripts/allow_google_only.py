import boto3

#替换你的region到region_name
client = boto3.client('network-firewall', region_name='us-west-2')

# Create the SSH rule group
response = client.create_rule_group(
    RuleGroupName='AllowSSH100',
    Type='STATEFUL',
    Capacity=100,
    Description='Allow SSH traffic',
    RuleGroup={
        'RulesSource': {
            'RulesString': 'pass tcp any any -> any 22 (msg:"Allow SSH traffic"; sid:1;)'
        },
        'StatefulRuleOptions': {
            'RuleOrder': 'STRICT_ORDER'
        }
    }
)

# Get the SSH rule group ARN
ssh_rule_group_arn = response['RuleGroupResponse']['RuleGroupArn']

# Create the rule group for Google domain traffic
response = client.create_rule_group(
    RuleGroupName='AllowGoogleDomain100',
    Type='STATEFUL',
    Capacity=100,
    Description='Allow traffic to .google.com',
    RuleGroup={
        'RulesSource': {
            'RulesSourceList': {
                'GeneratedRulesType': 'ALLOWLIST',
                'Targets': ['.google.com'],
                'TargetTypes': ['TLS_SNI', 'HTTP_HOST']
            }
        },
        'StatefulRuleOptions': {
            'RuleOrder': 'STRICT_ORDER'
        }
    }
)

# Get the Google domain rule group ARN
google_domain_rule_group_arn = response['RuleGroupResponse']['RuleGroupArn']

# Create the ICMP rule group
response = client.create_rule_group(
    RuleGroupName='AllowICMP100',
    Type='STATEFUL',
    Capacity=100,
    Description='Allow ICMP traffic',
    RuleGroup={
        'RulesSource': {
            'RulesString': 'pass ip any any -> any any (ip_proto:1; msg:"Allow ICMP traffic"; sid:2;)'
        },
        'StatefulRuleOptions': {
            'RuleOrder': 'STRICT_ORDER'
        }
    }
)

# Get the ICMP rule group ARN
icmp_rule_group_arn = response['RuleGroupResponse']['RuleGroupArn']

# Create the firewall policy
response = client.create_firewall_policy(
    FirewallPolicyName='MyPolicy100',
    FirewallPolicy={
        'StatelessDefaultActions': ['aws:forward_to_sfe'],
        'StatelessFragmentDefaultActions': ['aws:forward_to_sfe'],
        'StatefulRuleGroupReferences': [
            {
                'ResourceArn': ssh_rule_group_arn,
                'Priority': 1
            },
            {
                'ResourceArn': google_domain_rule_group_arn,
                'Priority': 2
            },
            {
                'ResourceArn': icmp_rule_group_arn,
                'Priority': 3
            }
        ],
        'StatefulDefaultActions': ['aws:drop_established'],
        'StatefulEngineOptions': {
            'RuleOrder': 'STRICT_ORDER'
        }
    }
)

print(response)
