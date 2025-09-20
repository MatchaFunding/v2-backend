from pydantic import BaseModel
from typing import Optional

"""
Clase que representa a un usuario de MatchaFunding.
"""
class Usuario(BaseModel):
    Persona: Optional[int] = None
    NombreDeUsuario: str
    Contrasena: str
    Correo: str

