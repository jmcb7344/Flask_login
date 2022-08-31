from flask import Flask, flash, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_login import LoginManager, login_required
from flask_wtf.csrf import CSRFProtect
from config import Config
from models import db, User
from auth import bp

app = Flask(__name__)

#Contiene las configuraciones de inicio
#from config import Config
app.config.from_object(Config)

#Inicio la conescion de la Base de datos por SQLAlchemy 
#from models import db
db.init_app(app)

#blueprint nos permite crear Rutas (URL) en otro modulo#
#from auth import bp
app.register_blueprint(bp)

#Premite Crear las migraciones a la Base de datos
#from flask_migrate import Migrate
migrate = Migrate()
migrate.init_app(app, db)

#Nos permite crear un token de procesccion CSRF
#from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(app)

#Maneja parametros como recuperar el usuario logeado o cerrar sesion
#from flask_login import LoginManager
login_manager = LoginManager(app)

#Funcion de LoginManager que recupera el user logeado
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Genera una ruta comun
@app.route('/')
def home():
    return render_template('index.html')

# Genera una ruta protegida para ver la vista debe esta logeado
# login_required 
@app.route('/saludos')
@login_required
def saludos():
    return render_template('saludos.html')

# Se ejecuta si encuentra un error 401
def status_401(error):
    flash("Debe estar Logeado para Acceder")
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    #Envia a la funcion status_401 el error 401
    app.register_error_handler(401,status_401)
    app.run()