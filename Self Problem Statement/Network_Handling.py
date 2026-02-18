import subprocess
import socket
import time
import urllib.request

def check_latency(host="8.8.8.8"):
    print("\nChecking Latency...")
    host_info = socket.gethostbyaddr("8.8.8.8")
    print(f"The name of the host is {host_info}")

    try:
        result = subprocess.run(
            ["ping", "-n", "4", host],
            capture_output=True,
            text=True
        )

        for line in result.stdout.split("\n"):
            if "Average" in line:
                print("Latency:", line.strip())

    except:
        print("Latency check failed")

def check_port(port):
    print(f"\nChecking Port {port}...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect(("127.0.0.1", port))
        print(f"Port {port} is OPEN")
    except:
        print(f"Port {port} is CLOSED / NOT IN USE")
    finally:
        s.close()

def check_response(url="https://www.google.com"):
    print("\nChecking Response Time...")

    try:
        start = time.time()
        urllib.request.urlopen(url)
        end = time.time()

        print(f"Response Time: {(end-start):.3f} seconds")

    except:
        print("Response check failed")

def firewall_check():
    print("\nChecking Firewall Restrictions...")

    test_sites = [
        "https://www.google.com",
        "https://www.microsoft.com",
        "https://www.netflix.com"
    ]

    for site in test_sites:
        try:
            urllib.request.urlopen(site, timeout=3)
            print(f"{site} → Accessible")
        except:
            print(f"{site} → Blocked (Possible Firewall)")

print("# 1. LATENCY CHECK (PING)")
check_latency()
print()
print("# 2. PORT AVAILABILITY")
check_port(80)
check_port(3000)
print()
print("# 3. RESPONSE TIME")
check_response()
print()
print("# 4. FIREWALL CHECK")
firewall_check()