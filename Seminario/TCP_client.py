import socket

REMOTE_PORT = 2001
REMOTE_HOST = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect ((REMOTE_HOST, REMOTE_PORT))

s.send ("Hola, mi nombre es Víctor".encode("utf-8"))

s.close()
