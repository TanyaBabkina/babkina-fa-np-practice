import socket

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
            print(resp)
            if resp == "Yes":
                break
            else:
                sock.send(input().encode())

sock = socket.socket()
sock.connect((HOST, PORT))
authorize(sock)
while True:

    
    request = input('myftp@shell$ ')
    if request == "exit":
        sock.close()
        break
    elif request=="su":
        sock.send(request.encode())
        authorize(sock)
        response = sock.recv(1024).decode()
        print(response)
        
    else:
        sock.send(request.encode())
    
        response = sock.recv(1024).decode()
        print(response)
    
