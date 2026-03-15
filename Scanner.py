import socket
from datetime import datetime

target = input("Enter target IP or domain: ")

print("-" * 50)
print("Scanning target:", target)
print("Scan started at:", datetime.now())
print("-" * 50)

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved")
    exit()

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is open")

    s.close()

print("Scan completed.")