import socket
import MySocket
def input_connection_data():
    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 9090
    
    HOST = input("Введите хост или нажмите \\n : ")
    if HOST == "":
        HOST = DEFAULT_HOST

    PORT = input("Введите номер порта или \\n : ")
    if PORT == "":
        PORT = DEFAULT_PORT
    else:
        PORT = int(PORT)

    return HOST, PORT

def connection(sock):
    while True:
        try:
            HOST, PORT = input_connection_data()
            sock.connect((HOST, PORT))
            break
        except:
            print("Ошибка соединения!")

def authorize(sock):
    reg = sock.receive_message()
    if reg == "No":
        # Ввод имени
        print(sock.receive_message())
        sock.send_message(input())
        # Ввод пароля
        print(sock.receive_message())
        sock.send_message(input())
        
            
    else:
        print(sock.receive_message())
        # Ввод пароля
        sock.send_message(input())
        while True:
            resp = sock.receive_message()
            print(resp)
            if resp == "Yes":
                break
            else:
                sock.send_message(input())


sock = MySocket.MySocket()
connection(sock)
authorize(sock)
while True:
    data = input("Введите данные: ")
    sock.send_message(data)
    if data == 'exit':
        break
    data_back = sock.receive_message()
    print(data_back)
sock.close()
