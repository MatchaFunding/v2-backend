from pydantic import BaseModel
from model.region import *

def TodasLasRegiones(app):
    return app.regiones