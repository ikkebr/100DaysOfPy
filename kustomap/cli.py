import argparse
import sys
from kustomap.core import Kustomap

def parse_data(data_str):
    """Parses a query string into a dictionary."""
    if not data_str:
        return {}
    data = {}
    for item in data_str.split("&"):
        if "=" in item:
            key, value = item.split("=", 1)
            data[key] = value
    return data

def parse_headers(headers_list):
    """Parses a list of header strings into a dictionary."""
    headers = {}
    if not headers_list:
        return headers
    for header in headers_list:
        if ":" in header:
            key, value = header.split(":", 1)
            headers[key.strip()] = value.strip()
    return headers

def main():
    parser = argparse.ArgumentParser(description="Kustomap: KQL Injection Scanner")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--method", default="GET", choices=["GET", "POST"], help="HTTP Method")
    parser.add_argument("--data", help="POST data (e.g., 'param1=value1&param2=value2')")
    parser.add_argument("--headers", action="append", help="Custom headers (e.g., 'Authorization: Bearer token')")

    args = parser.parse_args()

    data = parse_data(args.data) if args.data else {}
    headers = parse_headers(args.headers)

    print(f"Scanning {args.url} with method {args.method}...")

    scanner = Kustomap(args.url, method=args.method, headers=headers, data=data)
    vulnerabilities = scanner.scan()

    if vulnerabilities:
        print("\n[+] Vulnerabilities found:")
        for vuln in vulnerabilities:
            print(f"  - Parameter: {vuln['param']}")
            print(f"    Payload: {vuln['payload']}")
            print(f"    Method: {vuln['method']}")
            print("-" * 20)
    else:
        print("\n[-] No vulnerabilities found.")

if __name__ == "__main__":  # pragma: no cover
    main()
