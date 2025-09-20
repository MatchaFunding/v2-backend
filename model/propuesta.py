from pydantic import BaseModel
from typing import Optional

# Modelo que representa la ideas propuestas por la IA
class Propuesta(BaseModel):
    Idea: Optional[int] = None
    Resumen: str
