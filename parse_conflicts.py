import re
def p(path):
    with open(path, "r") as f:
        text = f.read()
    conflicts = re.findall(r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> main\n', text, re.DOTALL)
    for i, c in enumerate(conflicts):
        print(f"=== {path} CONFLICT {i} ===")
        print("HEAD:\n", c[0])
        print("=======\nMAIN:\n", c[1])
        print("======================\n")

p("Cargo.toml")
p("README.md")
