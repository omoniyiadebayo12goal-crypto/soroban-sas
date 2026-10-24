import re
import os

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # match any variable dot method: `\b([a-zA-Z0-9_]+)\s*\.\s*([a-zA-Z0-9_]+)\(\s*(?:&env|env),\s*`
    pattern = r'\b([a-zA-Z0-9_]+)\s*\.\s*([a-zA-Z0-9_]+)\(\s*(?:&env|env),\s*'
    def repl(m):
        return f"{m.group(1)}.{m.group(2)}("
    new_content = re.sub(pattern, repl, content)

    # multi-line version
    pattern_multiline = r'\b([a-zA-Z0-9_]+)\s*\.\s*([a-zA-Z0-9_]+)\(\s*\n\s*(?:&env|env),\s*\n?'
    def repl_multi(m):
        return f"{m.group(1)}.{m.group(2)}(\n"
    new_content = re.sub(pattern_multiline, repl_multi, new_content)

    # SASClient::compute_schema_uid(&env,
    new_content = re.sub(r'SASClient::compute_schema_uid\(\s*(?:&env|env),\s*', 'SASClient::compute_schema_uid(', new_content)

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

if __name__ == '__main__':
    process_file('packages/soroban-sas-sdk/src/client.rs')
    process_file('packages/soroban-sas-sdk/src/test.rs')
