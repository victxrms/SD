import json
import requests

seguir = True

def menu():
    print ("Elige una de las siguientes opciones.\n")
    menu = int(input("1.- Añadir sala. \n 2.- Mostrar información de sala. \n 3.- Añadir reserva. \n 4.- Listar reservas. \n 5.- Eliminar reserva \n 6.- Exit"))
    
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
                response = requests.post('http://localhost:8080/addRoom'), json={'roomId': ID, 'capacity':capacidad, 'resources':recursos}
            else: print ("Login incorrecto")
            
        if menu == 2:
            if login() == True:
                print ("Introduce el ID de la sala cuya información quieas consultar.\n")
                ID = int(input("ID: "))
                response = requests.get('http://localhost:8080/showInformationRoom/' + str(ID))
                print (response)
            
            else: print ("Login incorrecto")
            
        
        if menu == 3:   #dudas en esta
            if login() == True:
                print ("Introduce la información de reserva:\n")
                fecha = input("Fecha en formato dd/mm/aaaa: ")
                hora = input("Hora en formato: hh:mm")
                duracion = int(input("Duración en minutos: "))
                response = requests.post('http://localhost:8080/addBooking'), json={'DNI'}
            
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
                response = requests.get('http://localhost:8080/deleteBooking/' + ID)
                print (response)
        else: print ("Login incorrecto")
        
        if menu == 6:
            print ("Has salido del menú. ¡Hasta pronto!\n")
            break
        
def login():
    print ("Debes logearte para acceder a esta funcion.\n")
    username = input("Username: ")
    password = input("Password: ")
    users = requests.get('https://localhost:8080/addBooking')
    if 2+2 == 4:
        return True
    else: return False
    
    