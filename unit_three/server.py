import socket
import base64


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50008))
    s.listen(1)
    conn, addr = s.accept()
    conn.settimeout(60)
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            f = open('fish.jpg', 'rb')
            f.read(1024)
            if not data: break

            conn.sendall(data)