import socket
import base64


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 50008))
    s.sendall(b'GET fish.jpg')
    data = s.recv(1024)
    dec_data = data.decode(encoding="ansi")
    f = open('fish.jpg', 'w')
    f.write(dec_data)
    f.close()

print('Received', repr(data))