import argparse
from encodings import utf_8
import socket
import random
import struct


def main(host, port, n):
    # ...

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    num = str(n)

    s.sendto(num.encode("utf_8"), (host, port))

    for i in range (0, n):
        paquete = struct.pack("ff", random.random(), random.random())
        s.sendto(paquete, (host, port))
    s.sendto("exit".encode("utf_8"), (host, port))
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--number', default=100000, help="number of random points to be generated")
    args = parser.parse_args()

    main(args.host, args.port, args.number)
