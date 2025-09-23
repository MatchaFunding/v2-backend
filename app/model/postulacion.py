from pydantic import BaseModel
from typing import Optional

"""
Clase que representa las postulaciones de un proyecto a un fondo
https://registros19862.gob.cl/
"""
class Postulacion(BaseModel):
    Beneficiario: Optional[int]
    Proyecto: Optional[int]
    Instrumento: Optional[int]
    FechaDePostulacion: Optional[int]
    FechaDeResultado: Optional[int]
    Resultado: str
    MontoObtenido: int
    Detalle: str

# Muestra las postulaciones de un ente beneficiario
def PostulacionesDeBeneficiario(id: int, app):
    postulaciones = app.postulaciones.loc[app.postulaciones["Beneficiario"] == id]
    postulaciones = postulaciones.to_dict('records')
    return postulaciones
