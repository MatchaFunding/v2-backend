from pydantic import BaseModel
from typing import Optional
import pandas as pd

"""
Clase que representa a una persona natural, la cual puede ser miembro de una 
empresa o proyecto. Abajo de este estan las asociaciones entre persona y 
agrupacion.
https://www.nombrerutyfirma.com/nombre
https://www.nombrerutyfirma.com/rut
https://www.volanteomaleta.com/
"""
class Persona(BaseModel):
    Apellido: Optional[str] = None
    Ocupacion: Optional[str] = None
    Correo: Optional[str] = None
    Telefono: Optional[str] = None
    FechaDeNacimiento: str
    Nombre: str
    Sexo: str
    RUT: str

def CrearNuevaPersona(datos_de_persona, app):
    id_persona = len(app.personas)
    persona = dict(datos_de_persona)
    app.personas.loc[id_persona] = persona
    app.personas_json = app.personas.to_dict('records')
    return persona, id_persona