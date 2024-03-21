import socket
import struct


# class MySocket(socket.socket):

#     def send_message(self, message):
#         message_len = len(message)
#         header = f"{message_len:<10}".encode("utf-8")
#         self.sendall(header + message.encode("utf-8"))

#     def receive_message(self):
#         header = self.recv(10)
#         message_len = int(header.decode().strip())
#         message = self.recv(message_len).decode()
#         return message
    
#     def accept(self):
#         client_socket, address = super().accept()
#         new_socket = MySocket(client_socket)
#         return new_socket, address
    
#     def str_to_bytes(self, string):
#         return string.encode("utf-8")
class MySocket(socket.socket):
    __slots__ = ()
    
    def send_message(self, message):
        message_bytes = message.encode()
        message_length = len(message_bytes)
        header = struct.pack('!I', message_length)
        self.sendall(header + message_bytes)

    def receive_message(self):
        header = self.recv(4)
        if not header:
            return None
        message_length = struct.unpack('!I', header)[0]
        message = self.recv(message_length).decode()
        return message

# class MySocket(socket.socket):
#     def send_message(self, message):
#         message_bytes = message.encode('utf-8')
#         message_length = len(message_bytes).to_bytes(4, byteorder='big')
#         self.sendall(message_length + message_bytes)

#     def receive_message(self):
#         message_length_bytes = self.recv(4)
#         message_length = int.from_bytes(message_length_bytes, byteorder='big')
#         message = self.recv(message_length).decode('utf-8')
#         return message
#     # def accept(self) :
#     #     return super().accept()
#     # def bind(self, __address):
#     #     return super().bind(__address)
#     # def listen(self, __backlog):
#     #     return super().listen(__backlog)
#     @staticmethod
#     def string_to_bytes(s):
#         return s.encode('utf-8')

#     @staticmethod
#     def bytes_to_string(b):
#         return b.decode('utf-8')