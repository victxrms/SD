import argparse
from encodings import utf_8
import socket
import random
import struct


def main(host, port, n):
    # ...

    belowContador = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    num = str(n)

    s.sendto(num.encode("utf_8"), (host, port))

    for i in range (0, n):                                              #desde 0 a n 
        paquete = struct.pack("ff", random.random(), random.random())   #creamos un paquete con la tupla de dos numeros aleatorios entre 0 y 1 (gracias a randon.random())
        s.sendto(paquete, (host, port))                                 #enviamos el paquete
        abajo = s.recvfrom(1024)[0]                                     #recibimos el mensaje del servidor
        if (abajo.decode("utf_8") == "below"):                          #si es abajo, incrementamos el contador
            belowContador = belowContador + 1

    pi = 4.0 * float(belowContador/n)                                   #calculamos pi a través de la fórmula proporcionada

    print (pi)                                                          #hacemos un print del valor

    s.sendto("exit".encode("utf_8"), (host, port))                      #enviamos exit
    s.close()                                                           #cerramos conexion y salimos
    quit()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--number', default=100000, help="number of random points to be generated")
    args = parser.parse_args()

    main(args.host, args.port, args.number)
