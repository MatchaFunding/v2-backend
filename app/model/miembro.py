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

# Busca a todos los ID de los miembros de un ente beneficiario
# en base al ID de un beneficiario
def MiembrosDeBeneficiario(id_beneficiario: int, app):
    miembros = app.miembros.loc[app.miembros["Beneficiario"] == id_beneficiario]
    return miembros

# Extrae los IDs de las personas de una lista de miembros y los 
# devuelve en forma  de un arreglo de NumPy
def IDsDePersonasEnMiembros(miembros)
    id_personas = miembros["Persona"].to_numpy()
    return id_personas

# Toma las tablas de miembros y genera un arreglo de JSONs
def MiembrosEnJSON(miembros):
    miembros = miembros.to_dict('records')
    return miembros
