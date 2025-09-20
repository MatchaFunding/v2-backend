from pydantic import BaseModel
from typing import Optional

# Modelo de los proyectos
class Proyecto(BaseModel):
    Beneficiario: Optional[int] = None
    Problema: Optional[str] = None
    Publico: Optional[str] = None
    Innovacion: Optional[str] = None
    Proposito: Optional[str] = None
    ObjetivoGeneral: Optional[str] = None
    ObjetivoEspecifico: Optional[str] = None
    ResultadoEsperado: Optional[str] = None
    Titulo: str
    Descripcion: str
    DuracionEnMesesMinimo: int
    DuracionEnMesesMaximo: int
    Alcance: str
    Area: str
