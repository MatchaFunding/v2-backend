from pydantic import BaseModel
from model.sexo import Sexo
from model.persona import Persona
from model.beneficiario import Beneficiario
from model.postulacion import Postulacion
from model.propuesta import Propuesta
from model.proyecto import Proyecto
from model.usuario import Usuario
from model.idea import Idea

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
