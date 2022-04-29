import json
from bottle import run, request, response, get, post, put, delete
from datetime import datetime
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


# guardado de json 
def guardar(buffer):
    with open ('CommunicationJSON.json','w') as JS:
        json.dump(datos,JS,indent = 2)
        
# carga de json        
def carga():
    with open ('CommunicationJSON.json') as JS:
        return json.loads(JS.read())

#funcion login
@get('/login')
def login():
        encontrado = False
        buffer = request.json
        userpuser = Usuario(buffer['DNI'], buffer['userName'], buffer['password'])
        for usuario in datos['users']:                      # recorre los usuarios
            if usuario['userName']==userpuser.userName:     # si existe 
                if usuario['password']!=userpuser.password: # y la contraseña es igual a la guardada
                    encontrado = True
                    return json.dumps(0)              #si no es la misma contraseña, devuelve false
        if encontrado == False:    
            return json.dumps(0)                                      #si no existe el user devuelve false

#funcion añadir sala
@post('/addRoom')
def addRoom ():
    buffer = request.json
    idroom = buffer['roomId']
    cant = buffer['capacity']
    recurs = buffer['resources']
    datos['rooms'].append(Sala(idroom, cant, recurs).__dict__) # guarda en el json el objeto de la clase sala inicializado con los valores introducidos
    return "<p>Sala correctamente añadida.<\p>"

#funcion borrar reserva
@delete('/deleteBooking/<bookingId>') #!falla
def delBooking (bookingId):
    encontrado = False
    ind = 0
    for book in datos['books']:                                         #recorre las entradas de las reservas
        if (book['bookingId'] == int(bookingId)):                       #si coincide entonces
            encontrado = True                                           #encontrado a True
            del datos['books'][ind]                                     #borramos la entrada que se corresponde con el id de la reserva
            return json.dumps("Reserva eliminada.")                     #devolvemos el mensaje satisfactorio
        ind = ind + 1
    if encontrado == False:                                             #si encontrado es False, no se ha encontrado
        return json.dumps("No existe el identificador de la reserva.")  #devolvemos mensaje de que no existe idenficador de reserva

#funcion mostrar informacion de sala
@get('/showInformationRoom/<roomId>' )
def showInfo(roomId):
    encontrado = False
    for room_ in datos['rooms']:                #recorre las salas 
        if(room_['roomId']==int(roomId)):       #si el id introducido coincide con el de la sala en la que nos encontramos
            encontrado = True                   #encontrado a true
            return json.dumps(room_,indent = 2) #devuelve la informacion de la sala en formato json 
            
    if (encontrado==False):                     #si encontrado sigue a false, es decir, no se ha encontrado
        return json.dumps("Sala no encontrada") #se devuelve que no se ha encontrado

#funcion mostrar reservas de un usuario a través de su dni
@get('/showBookings/<userDNI>')
def showBooks(userDNI):
    books_list = []
    for books in datos['books']:                                    #recorre las reservas en busca de una cuyo DNI coincida con el introducido
        if(books['DNI']==userDNI):
            books_list.append(books)                                #si es asi, lo guarda en una lista
    if(len(books_list)==0):                                         #si la longitud de la lista es 0, es decir no hay
        return json.dumps("El usuario no tiene ninguna reserva")    #devuelve el error correspondiente
    else:
        return json.dumps(books_list,indent = 2)                    #si no, es decir, longitud lista > 0, devuelve la lista con las entradas
    
#funcion añadir reserva
@post('/addBooking')
def addBooking_():
    data = request.json
    listaDisp = []
    encontrado = False
    format= '%H:%M'
    reservon = Reserva(data.get('salaId'),0,data.get('DNI'),data.get('date'),data.get('startTime'),data.get('duration'),data.get('endTime'))    #construimos un objeto de la clase reserva a través de los datos introducidos por el cliente, inicializando a 0 el id de la reserva 
    salaId = reservon.salaId
    hourInit = datetime.strptime(reservon.startTime,format)                                                         #guardamos los valores que utilizaremos en las comparaciones en otras variables
    hourEnd = datetime.strptime(reservon.endTime,format)                                                            #de esta forma evitamos tener que usar nombres tan largos
    bookDate = reservon.date
    for reservas in datos['books'] :                                                                                #recorremos las reservas y buscamos si existe una con mismo tramo horario y en la misma sala que propone el cliente
        hhInit = datetime.strptime(reservas['startTime'],format)
        hhEnd = datetime.strptime(reservas['endTime'],format)
        if (reservas['salaId']==salaId and reservas['date']==bookDate and ((hhEnd>=hourInit and hourInit>=hhInit) or (hhEnd>=hourEnd and hourEnd>=hhInit))):
            encontrado = True                                                                                       #si es asi, colocamos el flag de encontrado a True
            break
    if encontrado == True:                                                                                          #si lo hemos encontrado quiere decir que debemos mostrar al cliente las salas que estan disponibles en el tramo horario elegido 
        for salas in datos['rooms']:                                                                                #recorremos las salas
            if salas['roomId']!=salaId:                                                                             #buscamos salas diferentes a la que quiere el usuario pues conocemos que esta ocupada
                idDeSala = salas['roomId']
                for reservas in datos['books']:                                                                     #recorremos las reservas para poder comparar los horarios en los que estan ocupadas las salas
                    if (reservas['salaId'] ==idDeSala and reservas['date']==bookDate and ((hhEnd>=hourInit and hourInit>=hhInit) or (hhEnd>=hourEnd and hourEnd>=hhInit))):
                        listaDisp.append(salas)
        return json.dumps({'error': "La sala que desea reservar está ocupada", 'listaDisp': listaDisp}, indent=2)   #devolvemos el error y la lista de salas disponibles para que el cliente elija de nuevo
    else:                                                                                                           #si no lo hemos encontrado, siginifica que esta libre esa sala en ese horario
        proxID = int(datos['books'][-1]['bookingId'])+1                                                             #calculamos el id de la reserva en base al anterior
        reservon.bookingId = proxID                                                                                 #lo asignamos al objeto
        datos['books'].append(reservon.__dict__)                                                                    #guardamos en el json
        
if __name__ == '__main__':
    datos = carga()
    run(host='localhost',port=8080,debug=True)
    guardar(datos)