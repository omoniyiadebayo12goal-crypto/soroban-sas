import re

filepath = 'packages/soroban-sas-sdk/src/client.rs'
with open(filepath, 'r') as f:
    content = f.read()

# Replace .method(&env, &rpc
content = re.sub(r'\.([a-zA-Z0-9_]+)\(\s*&env,\s*&rpc', r'.\1(&rpc', content)
# Replace .method(&env, rpc
content = re.sub(r'\.([a-zA-Z0-9_]+)\(\s*&env,\s*rpc', r'.\1(rpc', content)
# Replace .method(&env, &rpc2
content = re.sub(r'\.([a-zA-Z0-9_]+)\(\s*&env,\s*&rpc2', r'.\1(&rpc2', content)
# Replace SASClient::compute_schema_uid(&env,
content = re.sub(r'SASClient::compute_schema_uid\(\s*&env,\s*', r'SASClient::compute_schema_uid(', content)

with open(filepath, 'w') as f:
    f.write(content)
