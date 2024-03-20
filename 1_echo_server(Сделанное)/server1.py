import socket
from datetime import datetime
import logging
import json
import hashlib

import MySocket



HOST = ""
PORT = 9090
MAX_CONNECTION = 5

logging.basicConfig(filename="logfile.txt",
                    filemode='a',
                    level=logging.INFO)

def encrypt_password(password):
    salt = b'salt'  # добавляем соль для усиления защиты
    hashed_password = hashlib.sha256(salt + password).hexdigest()
    return hashed_password

def check_pass(address, input_password):
    with open("clientIdentifier.json") as file:
        data = json.load(file)
        stored_password = data[address]["password"]
    input_hashed_password = encrypt_password(input_password)
    return input_hashed_password == stored_password


def add_client(address, name, passwd):
    with open("clientIdentifier.json") as file:
        data = json.load(file)
    data[address] = {"name":name, "password":encrypt_password(passwd)}
    with open("clientIdentifier.json", "+w") as file:
        print(data)
        json.dump(data, file)


def clientName(address):
    with open("clientIdentifier.json") as file:
        data = json.load(file)
    return data[address]["name"]
        

def accauntExists(address):
    with open("clientIdentifier.json") as file:
        data = json.load(file)
        if address in data:
            return True
        else:
            return False

def clientRegistration(address,connection):
    if accauntExists(address):
        print("Yes")
        connection.send_message("Yes")
        connection.send_message(f"Здравствуйте, {clientName(address)}\nВведите пароль: ")
        password = connection.receive_message()
        while True:
            if check_pass(address, password):
                connection.send_message(f"Yes")
                break
            else:
                connection.send_message(f"Введите пароль: ")
                password = connection.receive_message()
    else:
        print("No")
        print(type(connection))
        connection.send_message("No")
        connection.send_message("Введите имя пользователя: ")
        new_client = connection.receive_message()
        connection.send_message("Введите пароль: ")
        new_password = connection.receive_message()
        add_client(address, new_client, new_password)


def check_port(sock, host, port):
    while True:
        try:
            sock.bind((host, port))
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Starting the server on port {port}')
            sock.listen( MAX_CONNECTION )
            break
        except OSError:
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Port {port} is bussy, try to connect another one')
            port += 1
        
    return sock, host, port

def connectClient(sock, host, port):
    
    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Start listening to the port {port}')
    conn, addr = sock.accept()
    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Connecting the client {addr}')
    return conn, addr
    

def GetAndChangeData(sock, conn):
    
    while True:
        try:
            data = conn.receive_message()
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Reading data')
            conn.send_message(data.upper())
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Sending data to the client')
            
        except:
            conn.close()
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] The connection with the client is broken')
            
            print("close")
            break



while True:
    sock = MySocket.MySocket(socket.AF_INET, socket.SOCK_STREAM)
    print(type(sock))
    sock, HOST, PORT = check_port(sock, HOST, PORT)
    print(HOST, PORT)
    print(type(sock))
    conn, addr = connectClient(sock, HOST, PORT)
    print(type(sock), "gv",type(conn) )
    clientRegistration(addr[0],conn)
    GetAndChangeData(sock, conn)
    sock.close()
    
    