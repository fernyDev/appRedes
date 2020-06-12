from app import db


class Administrador(db.Model):
    __tablename__ = 'administrador'
    idAdministrador = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    correo = db.Column(db.String())
    password = db.Column(db.String())

    def __repr__(self):
        return '<Administrador %r>' % self.nombre


class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'
    idDispositivo = db.Column(db.Integer, primary_key=True)
    direccionIp = db.Column(db.String())
    umbralMem = db.Column(db.Float())
    umbralCPU = db.Column(db.Float())
    umbralDisc = db.Column(db.Float())
    tipo = db.Column(db.Integer())
    registros = db.relationship('Registro')

    def __repr__(self):
        return '<Dispositivo %r>' % self.direccionIp


class RegistroInterfaz(db.Model):
    __tablename__ = 'registro_interfaz'
    idRegistroInterfaz = db.Column(db.Integer, primary_key=True)
    registroIdRegistro = db.Column(db.Integer,
                                   db.ForeignKey('registro.idRegistro'),
                                   nullable=False)
    interfazIdInterfaz = db.Column(db.Integer,
                                   db.ForeignKey('interfaz.idInterfaz'),
                                   nullable=False)
    anchoBanda = db.Column('anchoBanda', db.Float())
    db.PrimaryKeyConstraint('registroIdRegistro', 'interfazIdInterfaz')


class Registro(db.Model):
    __tablename__ = 'registro'
    idRegistro = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date())
    memoria = db.Column(db.Float())
    disco = db.Column(db.Float())
    cpu = db.Column(db.Float())
    interfaces = db.relationship('Interfaz',
                                 secondary='registro_interfaz',
                                 backref='registros')
    idDispositivo = db.Column(db.Integer,
                              db.ForeignKey('dispositivo.idDispositivo'))

    def __repr__(self):
        return '<Registro %r>' % self.idRegistro


class Interfaz(db.Model):
    __tablename__ = 'interfaz'
    idInterfaz = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    puerto = db.Column(db.Integer())
    umbralAnBan = db.Column(db.Float())

    def __repr__(self):
        return '<Interfaz %r>' % self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre