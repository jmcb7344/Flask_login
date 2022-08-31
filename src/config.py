class Config():
    SECRET_KEY = 'clave_secreta'
    DEBUG = True
    #Se puede realizar con Postgresql
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:7344@localhost/flask_login'
    #Se puede realizar con SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///base_datos/flask_db.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    