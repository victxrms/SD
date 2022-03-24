import argparse
import socket
import struct


def main(host, port, filein, fileout):
    # ...

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    fichero = open(f'{filein}', mode = 'rt')
    completo = fichero.read()
    s.send(completo.encode("utf-8"))
    fichero.close()


    lista = s.recv(2048).decode("utf-8")

    numpal = s.recv(2048).decode("utf-8")


    f_output = open (fileout, 'wt')

    palabra = lista.split()
    for i in range(0, len(palabra)):
        f_output.write(palabra[i])
        f_output.write('\n')

    f_output.close()
    s.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--filein', default='filein.txt', help="file to be read")
    parser.add_argument('--fileout', default='fileout.txt', help="file to be written")
    args = parser.parse_args()

    main(args.host, args.port, args.filein, args.fileout)
