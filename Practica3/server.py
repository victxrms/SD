import json
from bottle import request, response, get, post, put, delete
from types import SimpleNamespace
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
        
listSala = []
listUsuario = []
listReserva = []


# carga de json en las diferentes clases 

def carga():

    with open ('CommunicationJSON.json') as JS:
        data = json.load(JS)
            
    dataRm = data['rooms']
    for room in dataRm:
        listSala.append(Sala(room['roomId'], room['capacity'], room['resources']))
        
    dataUs = data['users']
    for user in dataUs:
        listUsuario.append(Usuario(user['DNI'], user['userName'], user['password']))
        
    dataRv = data['books']
    for book in dataRv:
        listReserva.append(Reserva(book['salaId'], book['bookingId'], book['DNI'], book['date'], book['startTime'], book['duration'], book['endTime']))

#funciones
        
@get('/login')
def do_login():
    username = json.load(['userName'])
    password = json.load(['password'])
    for user in listUsuario:
        if user.userName == username:
            if user.password == password:       
                return "<p>Informacion correcta.<\p>"
            else:
                return "<p>Informacion incorrecta.<\p>"
            
@post('/addRoom')
def addRoom ():
    datos = request.json
    id = datos.get("roomId")
    cant = datos.get ("capacity")
    recurs = datos.get ("resources")
    
    listSala.append(Sala(id, cant, recurs))
    return "<p>Sala correctamente añadida.<\p>"

@delete('/deleteBooking/<bookingId>')
def delBooking (bookID):
    flag = False
    for book in listReserva:
        if book.bookingId == bookID:
            flag = True
            listReserva.remove(book)
            return json.dumps("Reserva eliminada.")
    if flag == False:
        return json.dumps("No existe el identificador de la reserva.")

            
if __name__ == '__main__':
    carga()
    
    