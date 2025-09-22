from pydantic import BaseModel
from model.sexo import *
from model.persona import *
from model.beneficiario import *
from model.postulacion import *
from model.propuesta import *
from model.proyecto import *
from model.usuario import *
from model.miembro import *
from model.idea import *
import pandas as pd

# Modelo que representa los datos de un usuario recien registrado
class Registro(BaseModel):
    Usuario: Usuario
    Persona: Persona
    Beneficiario: Beneficiario

# Modelo que representa la organizacion completa
class Organizacion(BaseModel):
    Usuario: Usuario
    Beneficiario: Beneficiario
    Proyectos: list[Proyecto]
    Postulaciones: list[Postulacion]
    Miembros: list[Persona]
    Ideas: list[Idea]
    Propuestas: list[Propuesta]
