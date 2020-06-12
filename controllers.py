from entities import *
from interface import implements, Interface


class API(Interface):
    def get(self, id):
        pass

    def getAll(self):
        pass

    def save(self, T):
        pass

    def edit(self, id, T):
        pass

    def delete(self, id):
        pass


class RegistroController(implements(API)):
    def get(self, id):
        return Registro.query.get(id)

    def getAll(self):
        return Registro.query.order_by(Registro.idRegistro).all()

    def save(self, T):
        db.session.add(T)
        db.session.commit()

    def edit(self, id, T):
        registro = self.get(id)
        registro.memoria = T.memoria
        registro.disco = T.disco
        registro.cpu = T.cpu
        db.session.commit()

    def delete(self, id):
        registro = self.get(id)
        db.session.delete(registro)
        db.session.commit()


class InterfazController(implements(API)):
    def get(self, id):
        return Interfaz.query.get(id)

    def getAll(self):
        return Interfaz.query.order_by(Interfaz.idInterfaz).all()

    def save(self, T):
        db.session.add(T)
        db.session.commit()

    def edit(self, id, T):
        interfaz = self.get(id)
        interfaz.nombre = T.nombre
        interfaz.puerto = T.puerto
        interfaz.umbralAnBan = T.umbralAnBan
        db.session.commit()

    def delete(self, id):
        interfaz = self.get(id)
        db.session.delete(interfaz)
        db.session.commit()


class DispositivoController(implements(API)):
    def get(self, id):
        return Dispositivo.query.get(id)

    def getAll(self):
        return Dispositivo.query.order_by(Dispositivo.idDispositivo).all()

    def save(self, T):
        db.session.add(T)
        db.session.commit()

    def edit(self, id, T):
        dispositivo = self.get(id)
        dispositivo.direccionIp = T.direccionIp
        dispositivo.umbralMem = T.umbralMem
        dispositivo.umbralCPU = T.umbralCPU
        dispositivo.umbralDisc = T.umbralDisc
        dispositivo.tipo = T.tipo
        db.session.commit()

    def delete(self, id):
        dispositivo = self.get(id)
        db.session.delete(dispositivo)
        db.session.commit()

    def getInterfacesDispositivos(self):
        return db.session.query(Interfaz, Dispositivo).join(
            RegistroInterfaz).join(Registro).join(Dispositivo).all()

    def getInterfacesDispositivo(self, dispositivo):
        return db.session.query(Interfaz, Dispositivo).join(
            RegistroInterfaz).join(Registro).join(Dispositivo).filter(
                Dispositivo.idDispositivo == dispositivo.idDispositivo).all()


class AdministradorController(implements(API)):
    def get(self, id):
        return Administrador.query.get(id)

    def getAll(self):
        return Administrador.query.order_by(
            Administrador.idAdministrador).all()

    def save(self, T):
        db.session.add(T)
        db.session.commit()

    def edit(self, id, T):
        admin = self.get(id)
        admin.nombre = T.nombre
        admin.correo = T.correo
        admin.password = T.password
        db.session.commit()

    def delete(self, id):
        admin = self.get(id)
        db.session.delete(admin)
        db.session.comiit()

    def find(self, correo, password):
        return Administrador.query.filter(
            Administrador.correo == correo).filter(
                Administrador.password == password).first()


class RegistroInterfazController(implements(API)):
    def get(self, id):
        return RegistroInterfaz.query.get(id)

    def getAll(self):
        return RegistroInterfaz.query.order_by(
            Administrador.idAdministrador).all()

    def save(self, T):
        db.session.add(T)
        db.session.commit()

    def edit(self, id, T):
        registroInterfaz = self.get(id)
        registroInterfaz.interfazIdInterfaz = T.interfazIdInterfaz
        registroInterfaz.registroIdRegistro = T.registroIdRegistro
        registroInterfaz.anchoBanda = T.anchoBanda
        db.session.commit()

    def delete(self, id):
        registroInterfaz = self.get(id)
        db.session.delete(registroInterfaz)
        db.session.comiit()