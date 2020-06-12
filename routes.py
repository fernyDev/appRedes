from flask import jsonify, request
from controllers import *
from entities import *
from app import app
from api import Formatter


@app.route("/create")
def generarResgistrosDB():
    regIntController = RegistroInterfazController()
    for i in range(4):
        registroInterfaz = RegistroInterfaz(interfazIdInterfaz=i + 1,
                                            registroIdRegistro=1,
                                            anchoBanda=32.5)
        regIntController.save(registroInterfaz)
    return "Registro Creado Exitosamente"


@app.route("/create/<id>", methods=['GET'])
def getRegistro(id):
    dispController = DispositivoController()
    disp = dispController.get(id)
    disp = {
        "ip": disp.direccionIp,
        "umbralMem": disp.umbralMem,
        "umbralDisc": disp.umbralDisc,
        "umbralCPU": disp.umbralCPU,
        "tipo": disp.tipo
    }
    return jsonify(disp)


@app.route("/registro", methods=['GET'])
def getRegistros():
    lista = []
    formatter = Formatter()
    regController = RegistroController()
    registros = regController.getAll()
    regIntController = RegistroInterfazController()
    for registro in registros:
        lista.append({
            "id": registro.idRegistro,
            "fecha": formatter.formatterDateToString(registro.fecha),
            "memoria": registro.memoria,
            "disco": registro.disco,
            "cpu": registro.cpu,
        })
    return jsonify(lista)


@app.route("/dispositivo", methods=['GET'])
def getDispositivos():
    lista = []
    dispController = DispositivoController()
    dispositivos = dispController.getAll()
    for dispositivo in dispositivos:
        lista.append({
            "id": dispositivo.idDispositivo,
            "direccionIp": dispositivo.direccionIp,
            "umbralMem": dispositivo.umbralMem,
            "umbralCPU": dispositivo.umbralCPU
        })
    return jsonify(lista)


@app.route("/interfaz", methods=['GET'])
def getInterfaces():
    lista = []
    dispController = DispositivoController()
    dispositivo_interfaces = dispController.getInterfacesDispositivos()
    lista = [{
        "nombre": interfaz.nombre,
        "puerto": interfaz.puerto,
        "umbralAnBan": interfaz.umbralAnBan,
        "dispositivo": dispositivo.direccionIp
    } for interfaz, dispositivo in dispositivo_interfaces]
    return jsonify(lista)


@app.route("/login", methods=['POST'])
def login():
    contenido = request.json
    adminController = AdministradorController()
    result = adminController.find(contenido["correo"], contenido["password"])
    msj = {
        "msj": "OK"
    } if result is not None else {
        "msj": "Registro no existente"
    }
    return jsonify(msj)


@app.route("/admin", methods=['POST'])
def createAdministrador():
    contenido = request.json
    admin = Administrador(nombre=contenido['nombre'] + " " +
                          contenido['apellidos'],
                          correo=contenido['correo'],
                          password=contenido['password'])
    adminController = AdministradorController()
    adminController.save(admin)
    return jsonify({"msj": "OK"})


@app.route("/dispositivo", methods=['POST'])
def createDispositivo():
    contenido = request.json
    dispController = DispositivoController()
    intController = InterfazController()
    dispositivo = Dispositivo(direccionIp=contenido["ip"],
                              umbralMem=contenido["umbralMem"],
                              umbralCPU=contenido["umbralCPU"],
                              umbralDisc=contenido["umbralDisc"],
                              tipo=contenido["tipo"],
                              registros=[])
    for interfazJSON in contenido["interfaces"]:
        interfaz = Interfaz(nombre=interfazJSON["nombre"],
                            puerto=interfazJSON["puerto"],
                            umbralAnBan=interfazJSON["umbralAnBan"])
        intController.save(interfaz)
    dispController.save(dispositivo)
    return jsonify({"msj": "OK"})