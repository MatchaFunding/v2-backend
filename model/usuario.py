from pydantic import BaseModel
from typing import Optional

# Modelo de los usuarios
class Usuario(BaseModel):
    Persona: Optional[int] = None
    NombreDeUsuario: str
    Contrasena: str
    Correo: str

