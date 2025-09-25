from pydantic import BaseModel
from typing import Optional
import pandas as pd

class Miembro(BaseModel):
    Persona: int
    Beneficiario: int

def CrearNuevoMiembro(datos_de_miembro, app):
    id_miembro = len(app.miembros)
    miembro = dict(datos_de_miembro)
    app.miembros.loc[id_miembro] = miembro
    app.miembros_json = app.miembros.to_dict('records')
    return miembro, id_miembro
