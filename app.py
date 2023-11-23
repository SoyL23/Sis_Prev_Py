from flask import Flask, send_from_directory
from config.config import ConfigDev
from controllers.user import user
from controllers.product import product
from controllers.demand import demand
from sqlalchemy import create_engine
from config.db import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(ConfigDev)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Configurar la ruta estática para archivos CSS
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

# Configurar la ruta estática para archivos de imágenes
@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

# Configurar la ruta estática para archivos Js
@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(demand)