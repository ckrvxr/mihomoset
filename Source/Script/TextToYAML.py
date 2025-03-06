import re
import sys

def convert_text_to_yaml(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    rules = set()
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        line = re.sub(r'\s*#.*', '', line)
        match = re.match(r'^\+\.(.+)$', line)
        if match:
            domain = match.group(1)
            rules.add(f"DOMAIN-SUFFIX,{domain}")

    with open(output_file, 'w') as f:
        f.write("payload:\n")
        f.writelines(f"  - {rule}\n" for rule in sorted(rules))
        f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 TextToYAML.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_text_to_yaml(input_file, output_file)
