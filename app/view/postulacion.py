from pydantic import BaseModel
from model.postulacion import *
import pandas as pd

def TodasLasPostulaciones(app):
    return app.postulaciones_json
