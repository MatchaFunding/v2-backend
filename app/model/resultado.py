from pydantic import BaseModel

"""
Clase que representa los estados en los que se puede encontrar una postulacion.
Los resultados solo pueden caer dentro de las tres categorias.
"""
class Resultado(BaseModel):
    Nombre: str
    Codigo: str
