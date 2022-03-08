import socket

PORT = 2000
HOST = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print ("Estoy a la espera de conexiones...")
buffer, addr_c = s.recvfrom(1024)

print("Recibido el mensaje: " + buffer.decode("utf-8") + " de la dirección: " + str(addr_c))

s.close()
