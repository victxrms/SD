import json
import requests
import time


def login():
    print ("Debes logearte para acceder a esta funcion.\n")
    username = input("Username: ")
    password = input("Password: ")
    response = requests.post(('https://localhost:8080/login'), json = {'userName': username, 'password': password})
    if response == 'true':
        return True
    else: return False


def menu():
    print ("Elige una de las siguientes opciones.\n")
    menu = int(input(" 1.- Añadir sala. \n 2.- Mostrar información de sala. \n 3.- Añadir reserva. \n 4.- Listar reservas. \n 5.- Eliminar reserva \n 6.- Exit \n"))
    
    while True:
        
        if menu == 1:
            if login() == True:
                recursos = []
                print ("Introduce la información de la sala que quieras añadir:\n")
                ID = int(input("ID: "))
                capacidad = int(input("Capacidad: "))
                while True:
                    recaux = input("¿Deseas introducir un recurso? (Escribe 'No' para salir)\n")
                    if recaux == 'No':
                        break
                    else: recursos.append(recaux)
                requests.post(('http://localhost:8080/addRoom'), json={'roomId': ID, 'capacity':capacidad, 'resources':recursos})
            else: print ("Login incorrecto")
            
        if menu == 2:
            if login() == True:
                print ("Introduce el ID de la sala cuya información quieas consultar.\n")
                ID = input("ID: ")
                response = requests.get('http://localhost:8080/showInformationRoom/' + ID)
                print (response)
            
            else: print ("Login incorrecto")
            
        
        if menu == 3:
            if login() == True:
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
                requests.post(('http://localhost:8080/addBooking'), json={'DNI' : DNI, 'date': fecha, 'startTime': hora, 'duration': duracion, 'endTime': str(horasFinal) + ':' + str(minutosFinal)})
            
            else: print ("Login incorrecto")
            
        if menu == 4:
            if login() == True:
                print ("Para acceder a tus reservas debes introducir tu DNI\n")
                DNI = input("DNI: ")
                response = requests.get('http://localhost:8080/showBooking/' + DNI)
                print (response)
            else: print ("Login incorrecto")
            
        if menu == 5:
            if login() == True:
                print ("Para eliminar una reserva de debes introducir su ID\n")
                ID = input("ID de la reserva: ")
                response = requests.delete('http://localhost:8080/deleteBooking/' + ID)
                print (response)
        else: print ("Login incorrecto")
        
        if menu == 6:
            print ("Has salido del menú. ¡Hasta pronto!\n")
            break
        

    
menu()
    
    