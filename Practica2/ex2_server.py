import argparse
import socket
import struct

def main(host, port):
    # ...

    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))    
    
    s.listen()
    socket_c, addr_c = s.accept()

    fichero = socket_c.recv(2048)
    fichero = fichero.decode("utf-8")

    listapalabras = ''
    contador = 0


    palabra = fichero.split()

    for i in range(0, len(palabra)): 
        if 'a' in palabra[i]:
            print (palabra[i])
            listapalabras = listapalabras + palabra[i] + ' '
            contador = contador + 1
    
    socket_c.send(listapalabras.encode("utf-8"))
    socket_c.send(str(contador).encode("utf-8"))

    socket_c.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
