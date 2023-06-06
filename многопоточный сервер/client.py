import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Connected to', (HOST, PORT))
    while True:
        data = input('Enter text: ')
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024)
        print('Received', repr(data.decode('utf-8')))
    print('Disconnected from', (HOST, PORT))