import re

filepath = 'packages/soroban-sas-sdk/src/test.rs'
with open(filepath, 'r') as f:
    content = f.read()

# Replace .set_fee(&env,
content = re.sub(r'\.set_fee\(\s*&env,\s*', '.set_fee(', content)
content = re.sub(r'\.clear_fee\(\s*&env,\s*', '.clear_fee(', content)
content = re.sub(r'\.withdraw_schema_fees\(\s*&env,\s*', '.withdraw_schema_fees(', content)
content = re.sub(r'\.register_schema\(\s*&env,\s*', '.register_schema(', content)
content = re.sub(r'\.attest\(\s*&env,\s*', '.attest(', content)
content = re.sub(r'\.revoke\(\s*&env,\s*', '.revoke(', content)

with open(filepath, 'w') as f:
    f.write(content)
