from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from phox import settings
from phox.core import setup_routing

# setup application
app = Flask('phox')
app.config.from_object(settings)

# setup database
db = SQLAlchemy(app)

# register application views and blueprints
from phox.urls import routes
setup_routing(app, routes)
