from pydantic import BaseModel
from model.instrumento import *
import pandas as pd

def UnInstrumento(id: int, app):
    return app.instrumentos_json[id]

def TodosLosInstrumentos(app):
    return app.instrumentos_json
