from flask import Flask
from config.config import ConfigDev
from controllers.user import user
from controllers.product import product
from controllers.offer import offer
from controllers.role import role
from controllers.point_sell import point_sell
from controllers.home import home
from sqlalchemy import create_engine
from config.db import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(ConfigDev)


db.init_app(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
migrate = Migrate(app, db)

app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(offer)
app.register_blueprint(role)
app.register_blueprint(point_sell)
app.register_blueprint(home)