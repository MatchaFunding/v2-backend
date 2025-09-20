from pydantic import BaseModel

# Modelo de los sexos
class Sexo(BaseModel):
    Nombre: str
    Codigo: str
