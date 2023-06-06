import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

def start_server():
    print('Запускаю сервер...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Подключился клиент', addr)
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                conn.sendall(data)
                print('Получены данные', repr(data.decode('utf-8')))
                print('Отправляю данные', repr(data.decode('utf-8')))
    print('Сервер остановлен.')

if __name__ == '__main__':
    start_server()