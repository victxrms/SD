import json
from multiprocessing.sharedctypes import Value
from bottle import run, request, response, get, post, put, delete

salas = dict()
usuarios = dict()
reservas = dict()

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
        
@post('/login')
def do_login(username, password):
    data = json.load()
    try:
        data = request.json()
    except:
        raise ValueError
    if data is None:
        raise ValueError

    for user in data:
        if 'userName' == username:
            if 'password' == password:       
                return "<p>Informacion correcta.<\p>"
            else:
                return "<p>Informacion incorrecta.<\p>"
        
@post('/addRoom')
def do_addRoom():
    data = request.json
    
    ID_room = data.get("ID_room")
    for id
