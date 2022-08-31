# Flask Login
> Esta aplicación usa el framework web Flask.
Este es un proyecto de practica que sirve conocer
- SQLAlchemy
- Flask-Login
- Flask-Migrate
- Flask-SQLAlchemy
- Flask-WTF

------------

------------
#### Descarga e instalación de la practica
1. - Descargar: 
`$ git clone https://github.com/jmcb7344/flask_login.git`
2. - Crea el entorno virtual: 
`$ python -m venv .venv`
3. - Activa el entorno virtual: 
Win `$ .venv\Scripts\activate`
Otros `$ .venv/bin/activate`
4. - Instalación de dependencias: 
`$ pip install -r requirements.txt`
5. - Acceder a la carpeta
`cd src`
6. - Crear la migracion
`$ flask db init`
`$ flask db migrate -m "Primera migracion`
`$ flask db upgrade`
7. - Ejecución: 
`$ flask run`
