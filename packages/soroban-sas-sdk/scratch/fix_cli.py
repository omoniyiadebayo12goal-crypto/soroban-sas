import re
import os

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # The calls in CLI might be `client.register_schema(&env, ...)` 
    # Let's just find `\.([a-zA-Z0-9_]+)\(\s*&env,\s*` and replace it with `.\1(`
    # But wait, we should be careful to only replace for our SDK clients.
    # In the CLI, they are often called `client` or `sas_client` or `indexer_client`.
    
    # We can match `\b(sas_client|indexer_client|client|indexer)\s*\.\s*([a-zA-Z0-9_]+)\(\s*(?:&env|env),\s*`
    pattern = r'\b(sas_client|indexer_client|client|indexer)\s*\.\s*([a-zA-Z0-9_]+)\(\s*(?:&env|env),\s*'
    
    def repl(m):
        return f"{m.group(1)}.{m.group(2)}("
        
    new_content = re.sub(pattern, repl, content)
    
    # Also handle multiline calls:
    # client
    #    .method(
    #        &env,
    pattern_multiline = r'\b(sas_client|indexer_client|client|indexer)\s*\.\s*([a-zA-Z0-9_]+)\(\s*\n\s*(?:&env|env),\s*\n?'
    def repl_multi(m):
        return f"{m.group(1)}.{m.group(2)}(\n"
        
    new_content = re.sub(pattern_multiline, repl_multi, new_content)

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

def process_dir(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.rs'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    process_dir('packages/soroban-sas-cli/src')
    process_dir('packages/soroban-sas-cli/tests') if os.path.exists('packages/soroban-sas-cli/tests') else None
    process_dir('tests')
