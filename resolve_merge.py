import re

def fix(path, combined_func):
    with open(path, "r") as f:
        text = f.read()
    
    conflict_regex = re.compile(r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> main\n', re.DOTALL)
    
    def replacer(match):
        return combined_func(match.group(1), match.group(2))

    new_text = conflict_regex.sub(replacer, text)
    with open(path, "w") as f:
        f.write(new_text)

def cargo_combine(head, main):
    return head.strip() + ",\n    " + main.strip() + ",\n"

def readme_combine(head, main):
    return head + "\n" + main + "\n"

fix("Cargo.toml", cargo_combine)
fix("README.md", readme_combine)
