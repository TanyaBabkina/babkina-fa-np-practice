import socket, threading
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 9090

server.bind((host, port))

server.listen(5)
 
print('Enter для выхода с сервера')
clients = list()
 # Хранить клиентов, которые создали потоки
end = list()

def accept_client():
    while True:
        client, addr = server.accept()
        clients.append(client)


def recv_data(client):
    while True:
        try:
            indata = client.recv(1024)
        except Exception as e:
            clients.remove(client)
            end.remove(client)
            break
        print(indata.decode('utf-8'))
        for clien in clients:
            if clien != client:
                clien.send(indata)
 
 
def send_message():
    while True:
 
        # Введите информацию, которая будет предоставлена ​​клиенту
        print('')
        outdata = input('')
        print()
        if outdata=='enter':
            print ('Отправить всем:% s'% outdata)
            break
                 
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))
 
 
def recive_message():
    while True:
            for clien in clients:
                if clien in end:
                    continue
                index = threading.Thread(target = recv_data,args = (clien,))
                index.start()
                end.append(clien)
 

t1 = threading.Thread(target = recive_message,name = 'input')
t1.start()
 

 
t2 = threading.Thread(target = send_message, name= 'out')
t2.start()
 
t3 = threading.Thread(target = accept_client(),name = 'accept')
t3.start()
 
 # Блокировать округ, пока подпоток не будет завершен, и основной поток не может закончиться
# t1.join()
# t2.join()

for client in clients:
    client.close()
print('-' * 5 + 'сервер отключен' + '-' * 5)