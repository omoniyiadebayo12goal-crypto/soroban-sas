import re
import os

filepath = 'packages/soroban-sas-sdk/src/client.rs'
with open(filepath, 'r') as f:
    content = f.read()

# Methods we changed that we need to remove &env, from:
methods = [
    r'get_attestations_by_recipient_paginated',
    r'get_attestations_by_schema_paginated',
    r'get_attestations_by_attester_paginated',
    r'register_schema',
    r'register_schema_dry_run',
    r'set_fee_dry_run',
    r'SASClient::compute_schema_uid'
]

for method in methods:
    if "compute_schema_uid" in method:
        content = re.sub(r'SASClient::compute_schema_uid\(\s*&env,\s*', 'SASClient::compute_schema_uid(', content)
    else:
        # single line
        content = re.sub(r'\.' + method + r'\(\s*&env,\s*', f'.{method}(', content)
        # multi line
        content = re.sub(r'\.' + method + r'\(\s*\n\s*&env,\s*\n?', f'.{method}(\n', content)

with open(filepath, 'w') as f:
    f.write(content)

print(f"Fixed {filepath}")
