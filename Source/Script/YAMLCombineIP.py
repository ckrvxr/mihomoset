import dns.resolver
import sys

DEFAULT_DNS_SERVERS = [
    "8.8.8.8",
    "223.5.5.5"
]

def resolve_domain_with_dns(domain, dns_server):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]
        answers = resolver.resolve(domain, "A")  # 查询 A 记录
        return [answer.to_text() for answer in answers]
    except Exception as e:
        print(f"Error resolving {domain} with {dns_server}: {e}")
        return []

def resolve_domain(domain, dns_servers):
    all_ips = set()
    for dns_server in dns_servers:
        ips = resolve_domain_with_dns(domain, dns_server)
        all_ips.update(ips)
    return list(all_ips)

def process_input(input_data, dns_servers):
    lines = input_data.strip().split("\n")
    processed_domains = set()
    output_lines = []

    for line in lines:
        if line.startswith("  - DOMAIN-SUFFIX"):
            _, domain = line.split(",", 1)
            domain = domain.strip()
            if domain not in processed_domains:
                ips = resolve_domain(domain, dns_servers)
                if ips:
                    output_lines.append(line)
                    for ip in ips:
                        if ":" in ip:
                            output_lines.append(f"  - IP-CIDR,{ip}/128,no-resolve")
                        else:
                            output_lines.append(f"  - IP-CIDR,{ip}/32,no-resolve")
                    processed_domains.add(domain)
        else:
            output_lines.append(line)

    return "\n".join(output_lines)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r", encoding="utf-8") as file:
        input_data = file.read()

    if not input_data.strip().startswith("payload:"):
        output_data = "payload:\n" + process_input(input_data, DEFAULT_DNS_SERVERS)
    else:
        output_data = process_input(input_data, DEFAULT_DNS_SERVERS)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(output_data)

if __name__ == "__main__":
    main()
