# App Redes

El proyecto es directamente para quienes lleven la materia de Administración de Servicios en Red en la Escuela Superior de Cómputo

## Comenzando

Hay que tener en cuentr

### Prerequisitos

Este proyecto ha sido desarrollado con las siguientes herramientas:

```
Python 3.7.x
PostgreSQL 12

```

### Installing

Primero debemos asegurarnos que se encuentra instalado PostgreSQL

```bash
sudo psql
```

Crear una base de datos con el nombre redesapp

```bash
create database redesapp;
\c redesapp
```

Notificará de que se esta usando la base de datos redesapp;
También hay que asegurar que el se encuentre instalado correctamente Python y su módulo de paquetes Pip.

```bash
python3 --version
pip3 --version
```

Posteriormente realizar clone del repositorio en un directorio que cumpla con ser accesible facilmente.

```bash
git clone https://github.com/Ferny036/appRedes.git
```

Instalar las dependencias de python para el proyecto

```bash
cd appRedes
pip3 install -r  requirements.txt

```

Crear y actualizar las migraciones para la base de datos.

```bash
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade

```

Ya se encontrará instalado el proyecto correctamente.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
- [Maven](https://maven.apache.org/) - Dependency Management
- [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Authors

- **Billie Thompson** - _Initial work_ - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
