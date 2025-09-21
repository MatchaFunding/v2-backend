from pydantic import BaseModel
from typing import Optional

"""
Clase que representa la idea para un proyecto
"""
class Idea(BaseModel):
    Usuario: Optional[int] = None
    Campo: str
    Problema: str
    Publico: str
    Innovacion: str
    Oculta: bool
    FechaDeCreacion: str
    UltimaFechaDeModificacion: str
