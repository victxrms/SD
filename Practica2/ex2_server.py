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
    
    tam = int(socket_c.recv(1048).decode("utf-8"))          #recibimos el tamaño del fichero y enviamos un mensaje de confirmación
    socket_c.send("El servidor ha recibido el tamaño".encode("utf-8"))

    fichero = socket_c.recv(tam)                            #guardamos en fichero la string recibida
    fichero = fichero.decode("utf-8")                       #la decodificamos para poder trabajar con ella

    if len(fichero) == tam:                                 #si el tamaño de "fichero" es igual al recibido se ha recibido correctamente
        socket_c.send("El archivo se ha enviado correctamente".encode("utf-8"))
    else:
        socket_c.send("El archivo no se ha enviado correctamente".encode("utf-8"))

    
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
    s.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
