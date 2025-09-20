from pydantic import BaseModel
from typing import Optional

# Modelo de los beneficiarios
class Beneficiario(BaseModel):
    Mision: Optional[str] = None
    Vision: Optional[str] = None
    Valores: Optional[str] = None
    Nombre: str
    FechaDeCreacion: str
    RegionDeCreacion: str
    Direccion: str
    TipoDePersona: str
    TipoDeEmpresa: str
    Perfil: str
    RUTdeEmpresa: str
    RUTdeRepresentante: str
