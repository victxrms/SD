import argparse
import socket
import numpy as np


def main(host, port):
    # ...
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind ((host, port))

    n1, add_1 = s.recvfrom(1024)
    n1 = n1.decode("utf-8")
    board1 = s.recvfrom(1024)[0]
    board1 = board1.decode("utf-8")
    board1 = np.matrix(board1)
    
    n2, add_2 = s.recvfrom(1024)
    n2 = n2.decode("utf-8")
    board2 = s.recvfrom(1024)[0]
    board2 = board2.decode("utf-8")
    board2 = np.matrix(board2)
    
    again1 = True # el primer again true para que comience el primer jugador
    again2 = False 
    fin = False
    

    id = 1

    while True:
        while again1 == True and fin == False:
            
            s.sendto(f"Turn {id}".encode("utf-8"), add_1)
            
            if np.count_nonzero(board2 == 1) == 0:
                fin = True
            else: fin = False
            
            if fin == True:
                s.sendto("You win".encode("utf-8"), add_2)
                s.sendto("You lost".encode("utf-8"), add_1)
                s.close()
            
            coord = s.recvfrom(1024)[0]
            coord = coord.decode("utf-8")
            letra = ord(coord[0]) - 65
            num = int(coord[1:]) - 1
            
            if board2[letra, num] == 1:
                s.sendto("Hit".encode("utf-8"), add_1)
                board2[letra, num] = 0
                again1 = True
                again2 = False
                id = id + 1
            else:
                s.sendto("Fail".encode("utf-8"), add_1)
                again1 = False
                again2 = True
                id = id + 1
        
        while again2 == True and fin == False:
            
            s.sendto(f"Turn {id}".encode("utf-8"), add_2)
            
            
            if np.count_nonzero(board1 == 1) == 0:
                fin = True
            else: fin = False
            
            if fin == True:
                s.sendto("You win".encode("utf-8"), add_2)
                s.sendto("You lost".encode("utf-8"), add_1)
                s.close()
                    
            
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
