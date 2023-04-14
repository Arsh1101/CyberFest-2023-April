#localhost
#port 1 to 10

import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
    except:
        pass
    finally:
        s.close()

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            open_ports.append(port)
            print(f"Port {port} is open")
        except:
            pass
        finally:
            s.close()
    if len(open_ports) == 0:
        print("No open ports found")


if __name__ == '__main__':
    host = input("Enter the host to scan: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    scan_ports(host, start_port, end_port)
