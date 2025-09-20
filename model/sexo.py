from pydantic import BaseModel

"""
Genero u orientacion con la cual una persona se identifica.
Preferi hacerlo una tabla para realizar las validaciones de
fondos con enfoque de genero.
"""
class Sexo(BaseModel):
    Nombre: str
    Codigo: str
