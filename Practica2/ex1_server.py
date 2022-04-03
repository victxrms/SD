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

    n = s.recvfrom(1024)[0]
    n = n.decode("utf_8")
    num = int(n)
    

    for i in range (0, num):

        buffer, addr_c = s.recvfrom(1024)
        x,y = struct.unpack("ff", buffer)

        if y  <  sqrt(1-(pow (x, 2))):
            s.sendto("below".encode("utf-8"), addr_c)
            
        elif y >= sqrt(1-pow (x, 2)):
            s.sendto("above".encode("utf-8"), addr_c)
        elif y or x not in range (0,1):
            s.sendto("error".encode("utf-8"), addr_c)


    salida = s.recvfrom(1024)[0]

    if (salida.decode("utf_8") == "exit"):
        exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
