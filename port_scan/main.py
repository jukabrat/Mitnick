import socket
import concurrent.futures
import threading
import http.client
import socks
import pyfiglet
import os

ascii_banner = pyfiglet.figlet_format("port scan")
os.system("cls")
print(ascii_banner)

print("koristenje: bez https ili http, samo domain name sa .com ili drugi zavrsetkom")
# Create a lock for synchronizing output
output_lock = threading.Lock()

def is_port_open(host, port, proxy=None):
    try:
        with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            if proxy:
                proxy_host, proxy_port = proxy
                sock.set_proxy(socks.SOCKS5, proxy_host, proxy_port)
                sock.connect((host, port))
            else:
                sock.connect((host, port))

            print("otvoren port " + str(port))
            file = open("info.txt", "a")
            file.write("otvoren port "+ str(port) + "\n")
            return port
    except socket.timeout:
        pass
    except (socket.error, OSError):
        pass

def identify_server_info(host, port, proxy=None):
    try:
        with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            if proxy:
                proxy_host, proxy_port = proxy
                sock.set_proxy(socks.HTTP, proxy_host, proxy_port)
                sock.connect((host, port))
            else:
                sock.connect((host, port))

            if port == 80:  # HTTP
                conn = http.client.HTTPConnection(host, port, timeout=10)
                conn.sock = sock
                conn.request("GET", "/")
                response = conn.getresponse()
                server_info = response.getheader("Server", "Unknown Server")
            else:  # For other ports, send an empty request
                sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
                data = sock.recv(4096).decode("utf-8")
                server_info = data.split('\n')[0]

        with output_lock:
            file = open("info.txt", "a")
            if proxy:
                file.write(f"Host: {host}, Port: {port}, Proxy: {proxy} - Server: {server_info}"+ "\n")
                print(f"Host: {host}, Port: {port}, Proxy: {proxy} - Server: {server_info}")
            else:
                file.write(f"Host: {host}, Port: {port} - Server: {server_info}" +"\n")
                print(f"Host: {host}, Port: {port} - Server: {server_info}")
    except (socket.error, OSError):
        pass


def get_ports_from_user():
    while True:
        try:
            choice = input("'L' za listu portova ili 'R' za range portova: ").upper()

            if choice == 'L':
                ports_input = input("unesi listu portova odvojenu zarezima (e.g., 80, 443, 8080): ")
                ports = [int(p.strip()) for p in ports_input.split(',')]
                return ports
            elif choice == 'R':
                start_port = int(input("Od porta: "))
                end_port = int(input("Do porta: "))
                return list(range(start_port, end_port + 1))
            else:
                print("pogresan unos, unesi 'L' ili 'R'.")
        except ValueError:
            print("unesi brojeve.")

def get_max_workers_from_user():
    while True:
        try:
            max_workers = int(input("broj radnika: "))
            if max_workers > 0:
                return max_workers
            else:
                print("unesi pozitivian broj.")
        except ValueError:
            print("unesi validan broj.")

def get_proxy_from_user():
    use_proxy = input("koristis li proxy? (da/ne): ").lower()
    if use_proxy == 'da':
        os.chdir("../penetrateDir")
        os.system("start /wait cmd /k python checkproxy.py")
        os.chdir("../port_scan")
        proxy_host = input("proxy host (HTTP): ")
        proxy_port = int(input("proxy port: "))
        return (proxy_host, proxy_port)
    else:
        return None

def scan_ports(host, ports_to_check, max_workers, proxy=None):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for port in ports_to_check:
            future = executor.submit(is_port_open, host, port)
            future.add_done_callback(lambda f: identify_server_info(host, f.result(), proxy) if f.result() is not None else None)

# Example usage
file = open("info.txt", "w")
host_to_check = input("Host (0): ")
if host_to_check == "0":
    os.chdir("..")
    os.system("python main.py")
ports_to_check = get_ports_from_user()
max_workers = get_max_workers_from_user()
proxy_settings = get_proxy_from_user()

scan_ports(host_to_check, ports_to_check, max_workers, proxy=proxy_settings)