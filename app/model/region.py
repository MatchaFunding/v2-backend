from pydantic import BaseModel

"""
Regiones de Chile como su propia tabla para poder hacer la validacion correcta
Es un campo sumamanete comun en este contexto.
"""
class Region(BaseModel):
    Nombre: str
    Codigo: str
