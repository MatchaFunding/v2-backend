from pydantic import BaseModel
from typing import Optional

"""
Clase que representa las postulaciones de un proyecto a un fondo
https://registros19862.gob.cl/
"""
class Propuesta(BaseModel):
    Idea: Optional[int] = None
    Resumen: str
