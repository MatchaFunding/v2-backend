from pydantic import BaseModel
from model.instrumento import *
from datetime import date
import pandas as pd

def UnInstrumento(id: int, app):
    return app.instrumentos_json[id]

def TodosLosInstrumentos(app):
    return app.instrumentos_json

def InstrumentosVigentes(app):
    hoy = date.today()
    instrumentos = app.instrumentos.loc[
        app.instrumentos["FechaDeCierre"] > hoy
    ]
    instrumentos = instrumentos.to_dict('records')
    return instrumentos

def InstrumentosHistoricos(app):
    hoy = date.today()
    instrumentos = app.instrumentos.loc[
        app.instrumentos["FechaDeCierre"] < hoy
    ]
    instrumentos = instrumentos.to_dict('records')
    return instrumentos