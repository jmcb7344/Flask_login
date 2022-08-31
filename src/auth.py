import functools
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user

from models import db, User

#crea la conexion para generar rutas (URL) desde este modulo
#from flask import Blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username = request.form['username']).first()
        error = None

        if user is None:
            error = 'Incorrect username.'
            print('Incorrect username.')
        #Chequea una password_hash con la password ingresada
        #from werkzeug.security import check_password_hash
        elif not check_password_hash(user.password, request.form['password']):
            error = 'Incorrect password.'
            print('Incorrect password.')

        if error is None:
            #Regista el usuaria logeado y se lo envia a user_loader
            #from flask_login import login_user
            login_user(user)
            return render_template('index.html')
        flash(error)
        return render_template('auth/login.html')   
    else:
        return render_template('auth/login.html')


@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        emaill = User.query.filter_by(email=request.form['email']).first()
        error = None

        if user is not None:
            error = 'El usuario Ya existe'
        if emaill is not None:
            error = 'El email Ya existe'
        elif request.form['password1'] != request.form['password2']:
            error = 'El Clave no coincide'

        if error is None:
            new_user = User(
                nombre = request.form['nombre'], email = request.form['email'],                
                username = request.form['username'], password = generate_password_hash(request.form['password1'])
                )
            db.session.add(new_user)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
            return redirect(url_for('auth.login'))
        return render_template('auth/register.html')
    else:
        return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    # Funcion logout_user() cierra la secion de un usuario
    # from flask_login import logout_user
    logout_user()
    return redirect(url_for('auth.login'))
    