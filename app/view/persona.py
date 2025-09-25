from pydantic import BaseModel
from model.persona import *
import pandas as pd

def UnaPersona(id: int, app):
    return app.persona_json[id]

def TodasLasPersonas(app):
    return app.personas_json

def TodosLosHombres(app):
    hombres = app.personas.loc[app.personas["Sexo"] == "Hombre"]
    hombres = hombres.to_dict('records')
    return hombres

def TodasLasMujeres(app):
    mujeres = app.personas.loc[app.personas["Sexo"] == "Mujer"]
    mujeres = mujeres.to_dict('records')
    return mujeres