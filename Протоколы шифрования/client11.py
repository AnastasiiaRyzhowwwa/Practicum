import socket
import pickle
import os

HOST = '127.0.0.1'
PORT = 9090

sock = socket.socket()
sock.connect((HOST, PORT))
p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
K = 0
B = 0


def encrypt(s, private, public):
    return ''.join(map(chr, [(x+private+public) for x in map(ord, s)]))


def has_keys_in_storage():
    return os.path.isfile('client') and os.path.getsize('client') > 0


def send_public_key():
    sock.send(pickle.dumps((p, g, A)))


def generate_public_key():
    global K, B
    ser = sock.recv(1024)
    B = pickle.loads(ser)
    print("Получен открытый ключ сервера: ", B)
    print("Генерация закрытого ключа клиента...")
    K = B ** a % p
    with open('client', 'wb') as f:
        f.write(pickle.dumps((a, g, p, A, K)))


def start_messaging():
    sock.send(pickle.dumps(encrypt("server_check_keys", K, B)))

    msg = sock.recv(1024)
    port = encrypt(pickle.loads(msg), K, B)
    sock.close()
    print(f"Порт полученного сообщения: {port}. Направляясь в этот порт")

    s1 = socket.socket()
    s1.connect((HOST, int(port)))
    msg = ''
    while msg != 'close':
        msg = input('Ваше сообщение: ')
        s1.send(pickle.dumps(encrypt(msg, K, B)))
    s1.close()


if __name__ == '__main__':
    send_public_key()
    generate_public_key()
    start_messaging()
    sock.close()