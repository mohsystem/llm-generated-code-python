import socket
import sys

HOST = ''  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server listening on port {PORT}')
    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f'Received: {data}')
                conn.sendall(data.encode('utf-8'))