import socket
sock = socket.socket()
try:
  sock.bind(('', 80))
except OSError:
  sock.bind(('', 8080))
sock.listen(5)
conn, addr = sock.accept()
print("Connected", addr)
conn.close()

conn, addr = sock.accept()
print("Connected", addr)\

data = conn.recv(8192)
msg = data.decode()
print(msg)
resp = """HTTP/1.1 200 OK
Hello, webworld!"""
conn.send(resp.encode())
conn.close()