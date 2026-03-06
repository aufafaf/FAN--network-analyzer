import socket


def scan_port(host, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    result = sock.connect_ex((host, port))

    sock.close()
    return result == 0


host = "aufan.vercel"
for port in [22, 80, 443, 8080]:
    status = "OPEN" if scan_port(host, port) else "CLOSED"
    print(f" target : {host}")
    print(f"port {port} : {status}")
