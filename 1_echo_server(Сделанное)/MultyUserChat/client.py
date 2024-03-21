
# import socket
# import threading

# server_ip = '127.0.0.1'
# server_port = 9090

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# def receive_message():
#     while True:
        
#         data, _= client_socket.recvfrom(1024)
#         print("qdwdqwd")
#         message = data.decode('utf-8')
#         print(message)

# receive_thread = threading.Thread(target=receive_message)
# receive_thread.start()

# while True:
#     message = input("Введите данные: ")
#     client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))


import socket
# создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# подключаемся к серверному сокету
client_socket.connect(('localhost', 9090))

while True:
    # читаем и выводим ответ от серверного сокета
    message = client_socket.recv(1024).decode()
    print(message)
    
    # просим ввести сообщение в чат
    msg_to_send = input("Type your message: ")
    
    # отправляем сообщение
    client_socket.send(bytes(msg_to_send, "utf-8"))
    
    # обрабатываем ситуацию выхода из чата
    if msg_to_send == "exit":
        break

# закрываем соединение
client_socket.close()