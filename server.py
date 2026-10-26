#!/usr/bin/env python3
import http.server
import socketserver
import socket

PORT = 8080

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[*] Traffic Transmission: {args[0]}")

def run_server():
    my_ip = get_local_ip()
    handler = QuietHandler
    socketserver.TCPServer.allow_reuse_address = True
    
    print("====================================================")
    print("       GAMERHATMEOS APT DEPLOYMENT NETWORK SERVICE  ")
    print("====================================================")
    print(f"[+] NETWORK TARGET ADDRESS: http://{my_ip}:{PORT}")
    print("[*] Status: Server actively listening for incoming clients...")
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[-] Network distribution service safely terminated.")

if __name__ == "__main__":
    run_server()
