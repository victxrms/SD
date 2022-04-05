import argparse
from encodings import utf_8
from math import sqrt
import socket
import struct
import time


def main(host, port):
    # ...
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    n = s.recvfrom(1024)[0]                                 #recibimos el numero de veces que vamos a ejecutar el cuerpo del bucle
    n = n.decode("utf_8")                                   #decodificamos
    num = int(n)                                            #convertimos a int
    

    for i in range (0, num):

        buffer, addr_c = s.recvfrom(1024)                   #recibimos en el buffer la tupla
        x,y = struct.unpack("ff", buffer)                   #despaquetamos la tupla y la guardamos en x e y 

        if y  <  sqrt(1-(pow (x, 2))):                      #hacemos la comprobaciones necesarias para comprobar si esta por debajo o no
            s.sendto("below".encode("utf-8"), addr_c)       #enviamos los respectivos mensajes
            
        elif y >= sqrt(1-pow (x, 2)):
            s.sendto("above".encode("utf-8"), addr_c)
        elif y or x not in range (0,1):
            s.sendto("error".encode("utf-8"), addr_c)


    salida = s.recvfrom(1024)[0]                            #recibimos el mensaje que esperamos sea de salida

    if (salida.decode("utf_8") == "exit"):                  #si efectivamente es salida
        s.close()                                           #cerramos conexion y salimos
        quit()                                  


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
