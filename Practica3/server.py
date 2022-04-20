import json
from multiprocessing.sharedctypes import Value
from bottle import run, request, response, get, post, put, delete
from types import SimpleNamespace
class Sala:
    def __init__(self, roomId, capacity, resources):
        self.roomId
        self.capacity
        self.resources

class Usuario:
    def __init__(self, DNI, userName, password):
        self.DNI = DNI
        self.userName = userName
        self.password = password
        
class Reserva:
    def __init__(self, bookingId, DNI, date, startTime, duration, endTime):
        self.bookingId = bookingId
        self.DNI = DNI
        self.date = date
        self.startTime = startTime
        self.duration = duration
        self.endTime = endTime

# carga de json en las diferentes clases 
        
listSala = []
dataRm = json.load(['rooms'])
for room in dataRm:
    listSala[room] = json.loads(dataRm, object_hook=lambda d: SimpleNamespace(**d))
    
listUsuario = []
dataUs = json.load(['users'])
for user in dataUs:
    listUsuario[user] = json.loads(dataUs, object_hook=lambda d: SimpleNamespace(**d))
    
listReserva = []
dataRv = json.load(['bookings'])
for book in dataUs:
    listUsuario[book] = json.loads(dataRv, object_hook=lambda d: SimpleNamespace(**d))

#funciones
        
@post('/login')
def do_login(username, password):

    for user in listUsuario:
        if user.userName == username:
            if user.password == password:       
                return "<p>Informacion correcta.<\p>"
            else:
                return "<p>Informacion incorrecta.<\p>"
            
@post('/addRoom')
def addRoom (ID, capacidad, recursos):
    listSala.append(Sala(ID, capacidad, recursos))
    return "<p>Sala correctamente añadida.<\p>"

@delete('/deleteBooking/bookingId')
def delBooking (bookID):
    for book in listReserva:
        if book.bookingId == bookID:
            listReserva.remove(book)
            return "<p>Reserva eliminada correctamente.<\p>"
            
    