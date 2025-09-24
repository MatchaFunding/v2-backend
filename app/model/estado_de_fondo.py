from pydantic import BaseModel

"""
Estado en el que se encuentra un fondo o instrumento.
"""
class EstadoDeFondo(BaseModel):
    Nombre: str
    Codigo: str