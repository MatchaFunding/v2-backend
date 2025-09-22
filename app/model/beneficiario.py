from pydantic import BaseModel
from typing import Optional
import pandas as pd

"""
Clase que representa la empresa, emprendimiento, grupo de investigacion, etc.
que desea postular al fondo. La informacion debe regirse por la descripcion
legal de la empresa.
https://www.registrodeempresasysociedades.cl/MarcaDominio.aspx
https://www.rutificador.co/empresas/buscar
https://www.boletaofactura.com/
https://registros19862.gob.cl/
https://dequienes.cl/
"""
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

# Crea un nuevo beneficiario en el sistema er base a los datos
# Devuelve al beneficiario recien creada y su identificador
def CrearNuevoBeneficiario(datos_de_beneficiario, app):
    id_beneficiario = len(app.beneficiarios)
    beneficiario = dict(datos_de_beneficiario)
    app.beneficiarios.loc[id_beneficiario] = beneficiario
    app.beneficiarios_json = app.beneficiarios.to_dict('records')
    return beneficiario, id_beneficiario
