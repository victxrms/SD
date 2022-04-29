import json
import requests
import time
import datetime


#funcion login
def login():
    print ("Debes logearte para acceder a esta funcion.\n")                         #pide al cliente usuario y contraseña
    dni = input("DNI: ")
    username = input("Username: ")
    password = input("Password: ")
    response = requests.get('http://localhost:8080/login', 
                             json = {'DNI': dni, 'userName': username, 'password': password})   #imprime la respuesta del servidor tras solicitar el login
    print(response.text)
    if response.text != str(0):                                                     #si la respuesta es true, siginfica que el login ha sido correcto y devuelve true
        return True 
    else: 
        return False                                                              #si no devuelve false


def menu():
    while True:
        print ("Elige una de las siguientes opciones.\n") #muestra menu
        menu = int(input(" 1.- Añadir sala. \n 2.- Mostrar información de sala. \n 3.- Añadir reserva. \n 4.- Listar reservas. \n 5.- Eliminar reserva \n 6.- Exit \n"))
        
        if menu == 1:   #si es 1
            if login() == True:
                print ("Login correcto.\n")
                recursos = []                                                                       #crea una lista para los recursos
                print ("Introduce la información de la sala que quieras añadir:\n")
                ID = int(input("ID: "))
                capacidad = int(input("Capacidad: "))
                recaux = input("Introduce un recurso\n")                                            #introduce minimo 1
                recursos.append(recaux)
                while True:                                                                         #introduce tantos recursos como desee hasta que escriba no
                    recaux = input("¿Deseas introducir otro recurso? (Escribe 'No' para salir)\n")  
                    if recaux == 'No':
                        break
                    else: recursos.append(recaux)
                requests.post('http://localhost:8080/addRoom', 
                            json={'roomId': ID, 'capacity':capacidad, 'resources':recursos})      #envia la informacion al servidor
            else:
                print ("Login fallido.\n")
            
        if menu == 2:   #si es 2
            if login() == True:
                print ("Login correcto.\n")
                print ("Introduce el ID de la sala cuya información quieras consultar.\n")  #solicita el id de la sala a consultar
                ID = input("ID: ")  
                response = requests.get('http://localhost:8080/showInformationRoom/' + ID)  #guarda en response la respuesta que recibe del del servidor al enviar la peticion
                print (response.text)                                                       #la imprime
            else:
                print ("Login fallido.\n") 
            
        
        if menu == 3:   #si es 3
            if login() == True:
                print ("Login correcto.\n")
                addBook() #llama a la funcion addBook
            else:
                print ("Login fallido.\n")
            
        if menu == 4:   #si es 4
            if login() == True:
                print ("Login correcto.\n")
                print ("Para acceder a tus reservas debes introducir tu DNI\n")         #solicita al cliente el DNI
                DNI = input("DNI: ")
                response = requests.get('http://localhost:8080/showBookings/' + DNI)    #guarda en response la respuesta que recibe del del servidor al enviar la peticion
                print (response.text)                                                   #la imprime
            else:
                print ("Login fallido.\n")
            
        if menu == 5:   #si es 5
            if login() == True:
                print ("Login correcto.\n")
                print ("Para eliminar una reserva de debes introducir su ID\n")          #solicita al cliente el id de la reserva que quiere eliminar
                ID = input("ID de la reserva: ")
                response = requests.delete('http://localhost:8080/deleteBooking/' + ID)  #guarda en response la respuesta que recibe del del servidor al enviar la peticion
                print (response.text)                                                    #la imprime
            else:
                print ("Login fallido.\n")
        
        if menu == 6:   #si es 6
            print ("Has salido del menú. ¡Hasta pronto!\n") #imprime mensaje de despedida
            break                                           #sale del while True
        
        
def addBook():
    print ("Introduce la información de reserva:\n")                                                                                                    #solicita la informacion de la reserva
    DNI = input("DNI: ")
    salaId = int(input("Introduce el ID de la sala a reservar: "))
    fecha = input("Fecha en formato dd/mm/aaaa: ")
    hora = input("Hora en formato: hh:mm ")
    duracion = int(input("Duración en minutos: "))
    t1 = datetime.datetime.strptime(hora, '%H:%M')                                                                                                      #crea un objeto datetime con la hora
    t2 = datetime.timedelta(minutes = duracion)                                                                                                         #crea otro objeto datetime a partir de los minutos
    time_zero = datetime.datetime.strptime('00:00', '%H:%M')                                                                                            #crea otro objeto 0 pues así he leido en documentación que se debe de hacer para sumar correctamente horas
    horaFin = ((t1 - time_zero) + t2)                                                                                                                   #calcula la hora fin con la suma de la hora inicio y los minutos
    response = requests.post('http://localhost:8080/addBooking', 
                             json={'DNI' : DNI, 'salaId':salaId ,'date': fecha, 'startTime': hora, 'duration': duracion, 'endTime': str(horaFin)[0:5]}) #guarda en response la respuesta que recibe del del servidor al enviar la peticion
    if response.text != 0:                                                                                                                              #si es distinto de 0, es decir, hemos recibido algun dato, esperando que sea el de error y la lista
        print (response.text)                                                                                                                           #imprimos la respuesta
        addBook()                                                                                                                                       #llamamos de nuevo al a funcion addBook para que el ususario tras haber visto la lista de salas libres en su horario decida una nueva 



if __name__ == '__main__':
    menu()
    

    
    