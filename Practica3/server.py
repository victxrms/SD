import json
import pickle
from bottle import run, request, response, get, post, put, delete
from types import SimpleNamespace
datos = dict()
class Sala:
    def __init__(self, roomId, capacity, resources):
        self.roomId = roomId
        self.capacity = capacity
        self.resources = resources

class Usuario:
    def __init__(self, DNI, userName, password):
        self.DNI = DNI
        self.userName = userName
        self.password = password
        
class Reserva:
    def __init__(self, salaId, bookingId, DNI, date, startTime, duration, endTime):
        self.salaId = salaId
        self.bookingId = bookingId
        self.DNI = DNI
        self.date = date
        self.startTime = startTime
        self.duration = duration
        self.endTime = endTime      


# carga de json en las diferentes clases 
def guardar(buffer):
    with open ('CommunicationJSON.json','w') as JS:
        json.dump(datos,JS,indent = 2)
        
def carga():

    with open ('CommunicationJSON.json') as JS:
        return json.loads(JS.read())

@get('/login')
def do_login():
        buffer = request.json
        for usuario in datos['users']:
            if usuario['userName']==buffer['userName']:
                if usuario['password']==buffer['password']:
                    return "true".encode("utf-8")
                else:
                    return "false"
        return "false"
        
@post('/addRoom')
def addRoom ():
    buffer = request.json
    idroom = buffer['roomId']
    cant = buffer['capacity']
    recurs = buffer['resources']
    datos['rooms'].append(Sala(idroom, cant, recurs).__dict__)
    return "<p>Sala correctamente añadida.<\p>"

@delete('/deleteBooking/<bookingId>') #!falla
def delBooking (bookingID):
    flag = False
    for book in datos['books']:
        if book['bookingId'] == int(bookingID):
            flag = True
            del book
            return json.dumps("Reserva eliminada.")
    if flag == False:
        return json.dumps("No existe el identificador de la reserva.")

            
@get('/showInformationRoom/<roomId>' )
def showInfo(roomId):
    encontrado = False
    for room_ in datos['rooms']:
        if(room_['roomId']==int(roomId)):
            encontrado = True
            return json.dumps(room_,indent = 2)
            
    if (encontrado==False):
        return json.dumps("Sala no encontrada")
@post('/addBooking')#!falla
#Pendiente de hacer uwu
# ef addBooking_():
#    data = request.json
#   bookId = data.get("bookId")
#    for reservas in :
#        if (reservas.bookingId==bookId):
#            return json.dumps("No se puede reservar sala ya reservada") 
@get('/showBookings/<userDNI>')
def showBooks(userDNI):
    books_list = []
    for books in datos['books']:
        if(books['DNI']==userDNI):
            books_list.append(books)
    if(len(books_list)==0):
        return json.dumps("El usuario no tiene ninguna reserva")
    else:
        return json.dumps(books_list,indent = 2)

if __name__ == '__main__':
    datos = carga()
    run(host='localhost',port=8080,debug=True)
    guardar(datos)
