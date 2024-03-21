# import socket

# server_ip = '127.0.0.1'
# server_port = 9090

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((server_ip, server_port))

# clients = {}

# print('Server is running...')

# while True:
#     # print("List of clients ", clients)
#     data, client_addr = server_socket.recvfrom(1024)
#     print(client_addr, "Адрес клиента 1")
#     message = data.decode('utf-8')
#     print(message)
#     if client_addr not in clients:
#         clients[client_addr] = server_socket

#     for address in clients:
#         if address != client_addr:
#             server_socket.sendto(message.encode('utf-8'), address)
#             print("отправлено")

import socket
from threading import Thread

# функция нужна для старта приёма сообщений
def accept_incoming_connections():
    global addresses
    while True:
        client, client_address = sock.accept()
        # выведите информацию о подключении
        print(f"Подключение от: {client_address}")
        # попросите ввести имя
        client.send("Введите ваше имя: ".encode('utf-8'))
        name = client.recv(1024).decode("utf-8")

        # добавьте адрес клиента в словарь addresses
        addresses[client] = client_address
        broadcast(f'{name} присоединился к чату!')
        clients[client] = name

        Thread(target=handle_client, args=[client]).start()

# функция обрабатывает сообщения одного клиента
def handle_client(client):
    global clients
    name = clients[client]
    # # получите сообщение с именем клиента и поприветсвуйте его
    # name = client.recv(1024).decode("utf-8")
    # broadcast(f'{name} присоединился к чату!')
    
    # # добавьте имя клиента в словарь clients (в качестве ключей - сокеты клиентов)
    # clients[client] = name

    # получайте сообщения от клиентов в чате
    while True:
        msg = client.recv(1024).decode("utf-8")
        print(msg)
        # используя функцию broadcast() отправляйте сообщения всем участникам чата
        broadcast(f'{name}: {msg}\n')

        # обработайте ситуацию выхода клиента из чата:
        if not msg:
            # предупредите, что участник вышел из чата
            broadcast(f'{name} покинул чат.\n')
            # закройте соединение
            client.close()
            # удалите участника из clients
            del clients[client]
            break


# функция отправляет сообщения всем клиентам
def broadcast(msg):
    global clients
    # отправляйте сообщения все клиентам из словаря clients
    for client in clients:
        client.send(msg.encode("utf-8"))

clients = {}
addresses = {}

sock = socket.socket()
sock.bind(("", 9090))
sock.listen(5)
print("Waiting for connection...")
accept_thread = Thread(target=accept_incoming_connections)
accept_thread.start()
accept_thread.join()
sock.close()