from pydantic import BaseModel
from typing import Optional
import pandas as pd

class Miembro(BaseModel):
    Persona: int
    Beneficiario: int

# Crea un nuevo miembro en base a los identificadores de la
# persona y beneficiario del cual esta es parte
def CrearMiembroDesdeIDs(id_persona, id_beneficiario, app):
    miembro = {
        "Persona": id_persona, 
        "Beneficiario": id_beneficiario
    }
    id_miembro = len(app.miembros)
    app.miembros.loc[id_miembro] = miembro
    app.miembros_json = app.miembros.to_dict('records')
    return miembro, id_miembro
