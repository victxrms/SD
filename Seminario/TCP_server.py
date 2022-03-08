import socket

PORT = 2001
HOST = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()
socket_c, addr_c = s.accept()

print ("Estoy a la espera de conexiones...")
buffer = socket_c.recv(1024)

print("Recibido el mensaje: " + buffer.decode("utf-8") + " de la dirección: " + str(addr_c))

s.close()
