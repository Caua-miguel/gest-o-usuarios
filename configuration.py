from routes.home import home_route
from routes.client import client_route
from database.database import db
from database.models.cliente import Cliente
import psycopg

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(client_route, url_prefix='/clientes')

def configure_db():
    db
    # db.create_tables([Cliente])
