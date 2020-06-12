from app import app, db
from controllers import *
from pysnmp.hlapi import *
from pysnmp.smi import builder, view, compiler
from multiprocessing import Process

mibBuilder = builder.MibBuilder()
mibViewController = view.MibViewController(mibBuilder)
compiler.addMibCompiler(mibBuilder, sources=['file:///usr/share/snmp/mibs'])
mibBuilder.loadModules('SNMPv2-MIB', 'RFC1213-MIB', 'IF-MIB')


class DispositivoSNMP:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo
        self._ip = dispositivo.ip
        self.deltaTime = 600
        dispController = DispositivoController()
        self.interfaces = [
            InterfazSNMP(interfaz) for interfaz in
            dispController.getInterfacesDispositivo(dispositivo)
        ]


class InterfazSNMP:
    def __init__(self, iface):
        self.number = iface.puerto
        self.name = iface.nombre
        self.deltaTime = 600
        self._ifIn = 0
        self._ifOut = 0
        self._speed = 0
        self._bandWidth = 0
        self._data = []

    def getBandWidth(self):
        return self._bandWidth

    def setValues(self, ifIn, ifOut):
        self._ifIn = ifIn
        self._ifOut = ifOut

    def setSpeed(self, speed):
        self._speed = speed

    def calculateBandwidth(self, ifIn, ifOut):
        self._bandWidth = (
            (ifIn - self._ifIn) +
            (ifOut - self._ifOut) * 800) / (self.deltaTime * self._speed)
        self.setValues(ifIn, ifOut)

    def setName(self, nombre):
        self.name = nombre


class VarBind:
    def __init__(self, lista=[]):
        self.lista = lista

    def agregarElemento(self, elemento):
        self.lista.append(elemento)

    def getLista(self):
        return self.lista

    def clear(self):
        self.lista = []


class Monitor:
    def getSpeedComand(self, ip, iface):
        var = VarBind()
        var.clear()
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(), CommunityData("public"),
                   UdpTransportTarget((ip, 161)), ContextData(),
                   ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5.' + iface))))
        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' %
                  (errorStatus.prettyPrint(),
                   errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for oid, val in varBinds:
                var.agregarElemento({str(oid): str(val)})
        return var

    def getBandwidthComand(self, ip, iface):
        var = VarBind()
        var.clear()
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(), CommunityData("public"),
                   UdpTransportTarget((ip, 161)), ContextData(),
                   ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.' + iface)),
                   ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.16.' +
                                             iface))))
        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' %
                  (errorStatus.prettyPrint(),
                   errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for oid, val in varBinds:
                var.agregarElemento({str(oid): str(val)})
        return var


def main():
    pass
