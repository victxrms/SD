import argparse
import socket
import struct
import pickle


def main(host, port, filein, fileout):
    # ...

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    fichero = open(f'{filein}', mode = 'rt')        #abrimos fichero en modo lectura
    completo = fichero.read()                       #guardamos el fichero completo en la variable completo que sera una string
    s.send(completo.encode("utf-8"))                #enviamos codificada la cadena completa 
    fichero.close()                                 #cerramos el fichero pues vamos a dejar de trabajar con el 


    lista = s.recv(2048)                            #recibimos la lista 
    lista = pickle.loads(lista)                     #cargamos la lista gracias a la funcion pickle en su respectivo formato

    f_output = open (fileout, 'wt')                 #abrimos el fichero destino en modo escritura

    for palabra in lista:                           #recorremos la lista y escribimos los distintos elementos en el fichero de salida
        f_output.write(palabra + '\n')
    

    f_output.close()                                #cerramos el fichero de salida
    s.close()                                       #cerramos el socket

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--filein', default='filein.txt', help="file to be read")
    parser.add_argument('--fileout', default='fileout.txt', help="file to be written")
    args = parser.parse_args()

    main(args.host, args.port, args.filein, args.fileout)
