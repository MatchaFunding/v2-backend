from pydantic import BaseModel
from model.proyecto import *
import pandas as pd

def UnProyecto(id: int, app):
    return app.proyectos_json[id]

def TodosLosProyectos(app):
    return app.proyectos_json
