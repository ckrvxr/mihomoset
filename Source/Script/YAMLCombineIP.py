import socket
import sys

def resolve_domain(domain):
    try:
        addresses = socket.getaddrinfo(domain, None)
        ips = list(set(addr[4][0] for addr in addresses))
        return ips
    except socket.gaierror:
        return []

def process_input(input_data):
    lines = input_data.strip().split("\n")
    processed_domains = set()
    output_lines = []

    # 添加一个集合来存储需要移除的域名
    domains_to_remove = {
        "dns.alidns.com",
        "doh.pub",
        "dns.google",
        "cloudflare-dns.com"
    }

    for line in lines:
        if line.startswith("  - DOMAIN-SUFFIX"):
            _, domain = line.split(",", 1)
            domain = domain.strip()
            # 如果域名在需要移除的列表中，跳过处理
            if domain in domains_to_remove:
                continue
            if domain not in processed_domains:
                ips = resolve_domain(domain)
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
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, "r", encoding="utf-8") as file:
        input_data = file.read()
    if not input_data.strip().startswith("payload:"):
        output_data = "payload:\n" + process_input(input_data)
    else:
        output_data = process_input(input_data)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(output_data)

if __name__ == "__main__":
    main()
