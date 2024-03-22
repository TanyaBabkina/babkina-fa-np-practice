import socket
import struct


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

