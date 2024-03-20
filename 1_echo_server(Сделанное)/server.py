import socket
from datetime import datetime
import logging

HOST = ""
PORT = 9090
MAX_CONNECTION = 1

logging.basicConfig(filename="logfile.txt",
                    filemode='a',
                    level=logging.INFO)


def check_port(socket, host, port):
    while True:
        try:
            socket.bind((host, port))
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Starting the server on port {port}')
            socket.listen( MAX_CONNECTION )
            break
        except OSError:
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Port {port} is bussy, try to connect another one')
            port += 1
        
    return socket, host, port

def connectClient(sock, host, port):
    
    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Start listening to the port {port}')
    conn, addr = sock.accept()
    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Connecting the client {addr}')
    return conn, addr
    

def GetAndChangeData(sock, conn):
    
    while True:
        try:
            data = conn.recv(1024)
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Reading data')
            conn.send(data.upper())
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Sending data to the client')
            
        except:
            conn.close()
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] The connection with the client is broken')
            
            print("close")
            break



while True:
    sock = socket.socket()
    sock, HOST, PORT = check_port(sock, HOST, PORT)
    conn, addr = connectClient(sock, HOST, PORT)
    GetAndChangeData(sock, conn)
    print("fghjkl;")
    sock.close()
    
    