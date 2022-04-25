import json
import requests
import time
from bottle import run, request, response, get, post, put, delete



def login():
    print ("Debes logearte para acceder a esta funcion.\n")
    username = input("Username: ")
    password = input("Password: ")
    response = requests.post('https://localhost:8080/login', json = {'userName': username, 'password': password})
    print(response.text)
    response =response.text.decode("utf-8")
    if response.text == 'true':
        return True
    else: return False


def menu():
    while True:
        print ("Elige una de las siguientes opciones.\n")
        menu = int(input(" 1.- Añadir sala. \n 2.- Mostrar información de sala. \n 3.- Añadir reserva. \n 4.- Listar reservas. \n 5.- Eliminar reserva \n 6.- Exit \n"))
        
        if menu == 1:

            recursos = []
            print ("Introduce la información de la sala que quieras añadir:\n")
            ID = int(input("ID: "))
            capacidad = int(input("Capacidad: "))
            recaux = input("Introduce un recurso\n")
            recursos.append(recaux)
            while True:
                recaux = input("¿Deseas introducir otro recurso? (Escribe 'No' para salir)\n")
                if recaux == 'No':
                    break
                else: recursos.append(recaux)
            requests.post('http://localhost:8080/addRoom', json={'roomId': ID, 'capacity':capacidad, 'resources':recursos})

            
        if menu == 2:
            
                print ("Introduce el ID de la sala cuya información quieras consultar.\n")
                ID = input("ID: ")
                response = requests.get('http://localhost:8080/showInformationRoom/' + ID)
                print (response.text)
               
            
        
        if menu == 3:
            
                print ("Introduce la información de reserva:\n")
                DNI = input("DNI: ")
                fecha = input("Fecha en formato dd/mm/aaaa: ")
                hora = input("Hora en formato: hh:mm")
                duracion = int(input("Duración en minutos: "))
                horasAux = duracion % 60                            #calcula y normaliza la hora final
                minutosAux = duracion - ((duracion % 60) * 60)
                minutosFinalAux = int(hora[4:]) + minutosAux
                minutosFinal = minutosFinalAux - ((minutosFinalAux % 60) * 60)
                horasFinal = int(hora[0:1]) + (horasAux + (minutosFinalAux % 60))
                requests.post('http://localhost:8080/addBooking', json={'DNI' : DNI, 'date': fecha, 'startTime': hora, 'duration': duracion, 'endTime': str(horasFinal) + ':' + str(minutosFinal)})
            
            
        if menu == 4:
            
                print ("Para acceder a tus reservas debes introducir tu DNI\n")
                DNI = input("DNI: ")
                response = requests.get('http://localhost:8080/showBookings/' + DNI)
                print (response.text)
            
            
        if menu == 5:
            
                print ("Para eliminar una reserva de debes introducir su ID\n")
                ID = input("ID de la reserva: ")
                response = requests.delete('http://localhost:8080/deleteBooking/{id}'.format(id = ID))
                print (response.text)
            
        
        if menu == 6:
            print ("Has salido del menú. ¡Hasta pronto!\n")
            break
        

if __name__ == '__main__':
    menu()
    
    