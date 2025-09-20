from pydantic import BaseModel

# Modelo que representa los datos de un usuario recien registrado
class Registro(BaseModel):
    Usuario: Usuario
    Persona: Persona
    Beneficiario: Beneficiario
