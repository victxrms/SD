import argparse
import socket
import numpy as np


def main(host, port):
    # ...
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind ((host, port))

    n1, add_1 = s.recvfrom(1024)                                        #recibimos el nombre del primer jugador y su direccion
    n1 = n1.decode("utf-8")                                             #decodificamos el nombre del jugador
    board1 = s.recvfrom(1024)[0]                                        #recibimos el tablero del jugador 
    board1 = board1.decode("utf-8")                                     #lo decodificamos 
    board1 = np.matrix(board1)                                          #lo convertimos a una matriz
    
    n2, add_2 = s.recvfrom(1024)
    n2 = n2.decode("utf-8")
    board2 = s.recvfrom(1024)[0]
    board2 = board2.decode("utf-8")
    board2 = np.matrix(board2)
    
    again1 = True                                                       #again1 a true para que comience el primer jugador
    again2 = False                                                      #again2 a false ya que comienza el primer jugador
    fin = False                                                         #fin a false ya que será la flag que se empleará cuando el juego haya acabado
    

    id = 1

    while True:                                                         
        while again1 == True and fin == False:                          #mientras que se repita el turno del j1 y no sea el fin del juego
            
            s.sendto(f"Turn {id}".encode("utf-8"), add_1)               #enviamos el turno en el que nos encontramos
            
            if np.count_nonzero(board2 == 1) == 0:                      #si no hay 1s en el tablero siginificara que habremos acabado
                fin = True
            else: fin = False
            
            if fin == True:                                             #si ha acabado durante la ejecución del primer jugador este habra ganado
                s.sendto("You win".encode("utf-8"), add_1)              #se envia mensaje ganado a j1
                s.sendto("You lost".encode("utf-8"), add_2)             #se envia mensaje perdido a j2
                s.close()
                quit()
            
            coord = s.recvfrom(1024)[0]                                 #si no ha finalizado se recibe la coordenada y se decodifica
            coord = coord.decode("utf-8")                   
            letra = ord(coord[0]) - 65                                  #calculamos la posicion con respecto a la letra a través de ord que nos da el valor del codigo ascii
            num = int(coord[1:]) - 1                                    #como la primera es la A que es 65 en ascii, le restaremos 65 a cada letra y nos dará la posición de la matriz
                                                                        #con el numero cogeremos desde la posicion 1 de la string hasta el final por si hubiera numeros de mas de un digito y lo convertimos a int
            if board2[letra, num] == 1:                                 #si la coordenada coincide con un 1 habrá dado hit
                s.sendto("Hit".encode("utf-8"), add_1)                  #envia el mensaje hit de ser asi
                board2[letra, num] = 0                                  #coloca a 0 la posicion
                again1 = True                                           #vuelve a tocarle al jugador 1
                again2 = False
                id = id + 1                                             #suma 1 al turno
            else:
                s.sendto("Fail".encode("utf-8"), add_1)                 #si no, ha fallado y envia el mensaje respectivo
                again1 = False
                again2 = True
                id = id + 1             
                
        
        while again2 == True and fin == False:                          #mismo procedimiento que en el bloque anterior pero para el segundo jugador
            
            s.sendto(f"Turn {id}".encode("utf-8"), add_2)
            
            
            if np.count_nonzero(board1 == 1) == 0:
                fin = True
            else: fin = False
            
            if fin == True:
                s.sendto("You win".encode("utf-8"), add_2)
                s.sendto("You lost".encode("utf-8"), add_1)
                s.close()
                quit()
                    
            
            coord = s.recvfrom(1024)[0]
            coord = coord.decode("utf-8")
            letra = ord(coord[0]) - 65
            num = int(coord[1:]) - 1
            
            if board1[letra, num] == 1:
                s.sendto("Hit".encode("utf-8"), add_2)
                board1[letra, num] = 0
                again2 = True
                again1 = False
                id = id + 1
            else:
                s.sendto("Fail".encode("utf-8"), add_2)
                again2 = False
                again1 = True
                id = id + 1
                


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
