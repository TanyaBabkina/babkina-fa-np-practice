import socket
import os

HOST = 'localhost'
PORT = 9090

def authorize(sock):
    reg = sock.recv(1024).decode()
    if reg == "No":
        # Ввод имени
        print(sock.recv(1024).decode())
        sock.send(input().encode())
        # Ввод пароля
        print(sock.recv(1024).decode())
        sock.send(input().encode())
        
            
    else:
        print(sock.recv(1024).decode())
        # Ввод пароля
        sock.send(input().encode())
        while True:
            resp = sock.recv(1024).decode()
            if resp == "Yes":
                print("You are signed in")
                break
            else:
                print("Wrong pass")
                sock.send(input().encode())

sock = socket.socket()
sock.connect((HOST, PORT))
authorize(sock)
while True:

    
    request = input('myftp@shell$ ')
    print(request)
    if request == "exit":
        sock.close()
        break
    elif request=="su":
        sock.send(request.encode())
        authorize(sock)
        response = sock.recv(1024).decode()
    elif "copyFileToClient" in request:
        sock.send(request.encode())
        print("Start write to file")
        listRequest = request.split(" ")
        try:
            with open(listRequest[2].replace("\\", "\\\\"), "w") as f:
                data = sock.recv(1024).decode()
                f.write(data)
                while not data:
                    data = sock.recv(1024).decode()
                    f.write(data)
            response = sock.recv(1024).decode()
            print(response)
        except Exception:
            print("Директории клиента не существует")
    
    elif "copyFileToServer" in request:
        sock.send(request.encode())
        print("Start send file")
        listRequest = request.split(" ")
        print(listRequest[1].replace("\\", "\\\\"))
        try:

            with open(listRequest[1].replace("\\", "\\\\"), "r") as f:
                packet = f.read(1024)
                print(packet)
                sock.send(packet.encode())

                while not packet:
                    packet = f.read(1024)
                    sock.send(packet.encode())
                print("Stop sending the file")
            response = sock.recv(1024).decode()
            print(response)
        except Exception:
            print("Директории клиента не существует")

    else:
        sock.send(request.encode())
    
        response = sock.recv(1024).decode()
        print(response)
    
