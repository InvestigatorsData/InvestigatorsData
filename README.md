# Red Nacional de Investigadores 
  Facultad de Ciencias UNAM
  
  Modelado y Programacion
## Autores
* Quintero Villeda Erik
* Soto Corderi Sandra del Mar
* Traschikoff García Nicole Romina
* Velasco Flores Marco Antonio
* Velázquez Cruz Rodrigo Fernando

## Dependencias
* Python3 version 3.0 en adelante
* Django version 2.1.3
* Gestor de paquetes pip3 
* psycopg2-binary
* postgresql version 10

## Instalar dependencias
* Django
```bash
$ sudo pip3 install Django==2.1.3
```
* psycopg2-binary
```bash
$ sudo pip3 install psycopg2-binary
```
* postgresql
```bash
$ sudo apt-get install postgresql postgresql-contrib
```
## Base de datos
Despues de instalar postgresql creamos un usuario y la base de datos de la siguiente manera
```bash
$ sudo su postgres
$ psql
$ CREATE USER admin WITH PASSWORD admin;
$ CREATE DATABASE researchnet WITH OWNER admin;
$ GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA PUBLIC TO admin;
```
## Migraciones a la base de datos
```bash
$ cd InvestigatorsData/research_network/
$ python3 manage.py makemigrations database
$ python3 manage.py migrate
```
## Poblar la base de datos
```bash
$ python3 manage.py loaddata initial.json
```
## Ejecutar la pagina
Antes, debemos crear un superusuario 
```bash
$ python3 manage.py createsuperuser
  Nombre de usuario: admin
  Dirección de correo electrónico: admin@example.com
  Password: admin1234
  Password(again): admin1234
```
Ejecutar el servidor
```bash 
$ python3 manage.py runserver localhost:8000
```