from pydantic import BaseModel
from typing import Optional

"""
Clase que representa las postulaciones de un proyecto a un fondo
https://registros19862.gob.cl/
"""
class Postulacion(BaseModel):
    Beneficiario: Optional[int]
    Proyecto: Optional[int]
    Instrumento: Optional[int]
    FechaDePostulacion: Optional[int]
    FechaDeResultado: Optional[int]
    Detalle: Optional[str]
    Resultado: str
    MontoObtenido: int