from pydantic import BaseModel
from typing import Optional

"""
Clase que representa los fondos concursables a los que los proyectos pueden postular.
Esta clase contiene todos los parametros y requisitos que dictan la posterior evaluacion.
Representa tanto los fondos actuales como los historicos, en donde la fecha de cierre
indica a cual de los dos corresponde.
Recursos de fondos historicos:
http://wapp.corfo.cl/transparencia/home/Subsidios.aspx
https://github.com/ANID-GITHUB?tab=repositories
https://datainnovacion.cl/api
"""
class Instrumento(BaseModel):
    ObjetivoGeneral: Optional[str]
    ObjetivoEspecifico: Optional[str]
    ResultadoEsperado: Optional[str]
    EnlaceDelDetalle: Optional[str]
    EnlaceDeLaFoto: Optional[str]
    FechaDeResultado: Optional[str]
    Beneficios: Optional[str]
    Requisitos: Optional[str]
    Titulo: str
    Financiador: int
    Alcance: str
    Descripcion: str
    FechaDeApertura: str
    FechaDeCierre: str
    DuracionEnMeses: int
    MontoMinimo: int
    MontoMaximo: int
    Estado: str
    TipoDeBeneficio: str
    TipoDePerfil: str