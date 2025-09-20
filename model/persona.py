from pydantic import BaseModel
from typing import Optional

# Modelo de las personas
class Persona(BaseModel):
    Apellido: Optional[str] = None
    Ocupacion: Optional[str] = None
    Correo: Optional[str] = None
    Telefono: Optional[str] = None
    FechaDeNacimiento: str
    Nombre: str
    Sexo: str
    RUT: str
