from pydantic import BaseModel

"""
Tipo de empresa que representa una agrupacion en el contexto legal.
https://ipp.cl/general/tipos-de-empresas-en-chile/
"""
class TipoDePerfil(BaseModel):
    Nombre: str
    Codigo: str
