from pydantic import BaseModel

"""
Tipo de beneficio que otorga cierto fondo o instrumento.
"""
class TipoDeBeneficio(BaseModel):
    Nombre: str
    Codigo: str
