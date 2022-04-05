import argparse
import socket
import struct
import pickle

def main(host, port):
    # ...

    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))    
    
    s.listen()                                          
    socket_c, addr_c = s.accept()

    fichero = socket_c.recv(2048)                           #guardamos en fichero la string recibida
    fichero = fichero.decode("utf-8")                       #la decodificamos para poder trabajar con ella

    
    contador = 0                                            #ponemos a 0 el contador
    listapalabras = []                                      #creamos una lista denominada "listapalabras" donde guardaremos las palabras

    palabra = fichero.split()                               #dividimos el fichero gracias a split y guardamos la division en "palabra"

    for i in range(0, len(palabra)):                        #recorremos la la longitud de palabra 
        if 'a' in palabra[i]:                               #si existe a en palabra[i] 
            listapalabras.append(palabra[i])                #guardamos en la lista
            contador = contador + 1                         #sumamos 1 al contador
            
    packpal = pickle.dumps(listapalabras)                   #creamos "packpal" que contendrá la lista en su formato y lista para enviarse gracias a pickle
    socket_c.send(packpal)                                  #enviamos packpal

    socket_c.close()                                        #cerramos conexion

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
