import socket

REMOTE_PORT = 2000
REMOTE_HOST = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Hola, mi nombre es Víctor".encode("utf-8"), (REMOTE_HOST, REMOTE_PORT))

s.close()
