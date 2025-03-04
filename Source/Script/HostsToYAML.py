import re
import sys

def convert_hosts_to_yaml(hosts_file, output_file):
    with open(hosts_file, 'r') as f:
        lines = f.readlines()

    filter_entries = {
        ('127.0.0.1', 'localhost'),
        ('127.0.0.1', 'localhost.localdomain'),
        ('127.0.0.1', 'local'),
        ('255.255.255.255', 'broadcasthost'),
        ('::1', 'localhost'),
        ('::1', 'ip6-localhost'),
        ('::1', 'ip6-loopback'),
        ('fe80::1%lo0', 'localhost'),
        ('ff00::0', 'ip6-localnet'),
        ('ff00::0', 'ip6-mcastprefix'),
        ('ff02::1', 'ip6-allnodes'),
        ('ff02::2', 'ip6-allrouters'),
        ('ff02::3', 'ip6-allhosts'),
        ('0.0.0.0', '0.0.0.0')
    }

    rules = set()
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        line = re.sub(r'\s*#.*', '', line)
        match = re.match(r'^(\d{1,3}(?:\.\d{1,3}){3}|[a-fA-F0-9:]+)\s+(.+)$', line)
        if match:
            ip, domain = match.groups()
            if (ip, domain) not in filter_entries:
                rules.add(f"DOMAIN-SUFFIX,{domain}")

    with open(output_file, 'w') as f:
        f.write("payload:\n")
        f.writelines(f"  - {rule}\n" for rule in sorted(rules))
        f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 HostsToYAML.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_hosts_to_yaml(input_file, output_file)