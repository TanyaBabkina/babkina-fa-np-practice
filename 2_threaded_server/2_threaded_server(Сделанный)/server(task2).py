import socket
import threading


def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        client_socket.send(request)


sock = socket.socket()
sock.bind(("", 9090))
sock.listen(0)

print("Сервер запущен...")

while True:
    conn, addr = sock.accept()
    print(f"Получено соединение с {addr[0]}:{addr[1]}")

    client_thread = threading.Thread(target=handle_client, args=(conn,))
    client_thread.start()