from flask import Flask

from flask_pony import Pony
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('configmodule.Config')

pony = Pony(app)
CSRFProtect(app)

from . import views, models

pony.connect(models)
