import socket, threading
 
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
            return sock, HOST, PORT
        except:
            print("Ошибка соединения!")
 
def user_name_input():
    while True:
        name = input ('Введите имя пользователя чата: ')

        if 1<len(name):
            return name
        else:
            print("Имя не подходит")
    

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock, host, port = connection(client)

while True:
    name = user_name_input()
    print('name input...')
    sock.send(name.encode())
    print("test name in dict")
    resp = sock.recv(5).decode()
    print(resp)
    if resp == "volid":
        break

print("Вы подключены к серверу")
 
 
def massage_send():
    while True:
        outdata = input('')
        if outdata=='enter':
            break
        client.send(f'{name}:{outdata}'.encode('utf-8'))
        print('%s:%s'% (name, outdata))
 
 
def message_recive():
 
    while True:
        indata = client.recv(1024)
        print(indata.decode('utf-8'))
 

t1 = threading.Thread(target=message_recive, name='input')
t2 = threading.Thread(target=massage_send, name='out')

t1.start()
t2.start()
 
 # Заблокировать поток, основной поток не может завершиться, пока не завершится выполнение дочернего потока.
# t1.join()
# t2.join()

# print ('-' * 5 + 'сервер отключен' + '-' * 5)
