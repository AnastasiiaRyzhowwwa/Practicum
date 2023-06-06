import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

def start_client():
    print('Подключаюсь к серверу...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Подключен к серверу.')
        while True:
            data = input('Введите строку на русском языке (или "quit" для выхода): ').encode('utf-8')
            if data == b'quit':
                break
            s.sendall(data)
            data = s.recv(BUFFER_SIZE)
            print('Получены данные', repr(data.decode('utf-8')))
    print('Отключен от сервера.')

if __name__ == '__main__':
    start_client()