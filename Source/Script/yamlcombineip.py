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
    processed_domains = set()  # 用于记录已处理的域名
    output_lines = []

    for line in lines:
        if line.startswith("  - DOMAIN-SUFFIX"):
            _, domain = line.split(",", 1)
            domain = domain.strip()
            if domain not in processed_domains:
                ips = resolve_domain(domain)
                if ips:
                    output_lines.append(line)  # 添加原始域名规则
                    for ip in ips:
                        if ":" in ip:  # IPv6地址
                            output_lines.append(f"  - IP-CIDR,{ip}/128,no-resolve")
                        else:  # IPv4地址
                            output_lines.append(f"  - IP-CIDR,{ip}/32,no-resolve")
                    processed_domains.add(domain)
        else:
            output_lines.append(line)  # 保留其他原始行

    return "\n".join(output_lines)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, "r", encoding="utf-8") as file:
        input_data = file.read()
    output_data = process_input(input_data)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("payload:\n")
        file.write(output_data)

if __name__ == "__main__":
    main()
