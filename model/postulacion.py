from pydantic import BaseModel
from typing import Optional

# Modelo de las postulaciones
class Postulacion(BaseModel):
    Beneficiario: Optional[int]
    Proyecto: Optional[int]
    Instrumento: Optional[int]
    FechaDePostulacion: Optional[int]
    FechaDeResultado: Optional[int]
    Resultado: str
    MontoObtenido: int
    Detalle: str
