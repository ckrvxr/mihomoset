import socket
import sys

DEFAULT_DNS_SERVERS = [
    "8.8.8.8",
    "1.1.1.1",
    "223.5.5.5",
    "1.12.12.12"
]

def resolve_domain_with_dns(domain, dns_server):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)

        query = f"GET /?name={domain} HTTP/1.1\r\nHost: {dns_server}\r\n\r\n"
        sock.sendto(query.encode(), (dns_server, 53))
        response, _ = sock.recvfrom(512)

        addresses = response.decode().split("\n")
        ips = [addr.strip() for addr in addresses if addr.strip()]
        return ips
    except Exception as e:
        return []
    finally:
        sock.close()

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