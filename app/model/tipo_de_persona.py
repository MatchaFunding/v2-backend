from pydantic import BaseModel

"""
Tipo de persona que representa a una empresa en terminos juridicos. 
En este contexto los beneficiarios y financiadores
pueden ser empresas formales.
https://www.sii.cl/mipyme/emprendedor/documentos/fac_Datos_Comenzar_2.htm
"""
class TipoDePersona(BaseModel):
    Nombre: str
    Codigo: str
