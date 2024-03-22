import socket
from funcs import *
from datetime import datetime
import logging
import json
import hashlib
import os
from FuncsForManager.FileManager import *
from FuncsForManager.FileManagerSetings import *

def encrypt_password(password):
    salt = b'salt'  # добавляем соль для усиления защиты
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return hashed_password

def check_pass(address, input_password):
    with open("C:\\Users\\1\\Desktop\\babkina-fa-np-practice\\5_FTP_server(Сделанное)\\clientIdentifier.json") as file:
        data = json.load(file)
        stored_password = data[address]["password"]
    input_hashed_password = encrypt_password(input_password)
    return input_hashed_password == stored_password


def add_client(address, name, passwd):
    with open("C:\\Users\\1\\Desktop\\babkina-fa-np-practice\\5_FTP_server(Сделанное)\\clientIdentifier.json") as file:
        data = json.load(file)
    data[address] = {"name":name, "password":encrypt_password(passwd)}
    with open("C:\\Users\\1\\Desktop\\babkina-fa-np-practice\\5_FTP_server(Сделанное)\\clientIdentifier.json", "+w") as file:
        print(data)
        json.dump(data, file)


def clientName(address):
    with open("C:\\Users\\1\\Desktop\\babkina-fa-np-practice\\5_FTP_server(Сделанное)\\clientIdentifier.json") as file:
        data = json.load(file)
    return data[address]["name"]
        

def accauntExists(address):
    with open("C:\\Users\\1\\Desktop\\babkina-fa-np-practice\\5_FTP_server(Сделанное)\\clientIdentifier.json") as file:
        data = json.load(file)
        if address in data:
            return True
        else:
            return False

def clientRegistration(address,connection):
    global root
    if accauntExists(address):
        print("User registed")
        connection.send("Yes".encode())
        connection.send(f"Здравствуйте, {clientName(address)}\nВведите пароль: ".encode())
        if address != "root":
            root = root+clientName(address)
        password = connection.recv(1024).decode()
        while True:
            if check_pass(address, password):
                connection.send(f"Yes".encode())
                break
            else:
                connection.send(f"Введите пароль: ".encode())
                password = connection.recv(1024).decode()
    else:
        print("User not exists")
        connection.send("No".encode())
        connection.send("Введите имя пользователя: ".encode())
        new_client = connection.recv(1024).decode()
        connection.send("Введите пароль: ".encode())
        new_password = connection.recv(1024).decode()
        add_client(address, new_client, new_password)
        root = root+clientName(address)
        os.makedirs(root) 
    


PORT = 9090
 

# logging.basicConfig(filename="logfile.txt",
#                     filemode='a',
#                     level=logging.INFO)



sock = socket.socket()
sock.bind(('', PORT))
logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Starting the server on port {PORT}')
sock.listen()
logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Start listening to the port {PORT}')
print("Слушаем порт", PORT)
conn, addr = sock.accept()
clientRegistration(addr[0],conn)
logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Connecting the client {addr}')
print(addr)


manager = FileManager(root)
while True:  
    request = conn.recv(1024).decode()
    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Reading data')
    print(request)
    if request == "exit":
        sock.close()
        logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] The connection with the client is broken')
        break
    elif request == "su":
        if os.name == "nt":
            root = "C:\\Users\\1\\Desktop\\FileManagerFolder"
        else:
            root = "//home//tanya//Desktop//FileManagerFolder"
        manager = FileManager(root)
        clientRegistration("root",conn)


    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Perform some func')
    response = process(request, root, manager)
    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Sending response to the client')
    conn.send(response.encode())

 
