from pydantic import BaseModel
from typing import Optional
import pandas as pd

"""
Clase que representa las entes financieras que ofrecen los fondos.
En muchos sentidos operan de la misma forma que las entes benficiarias,
lo unico que cambia en rigor son sus relaciones con las otras clases.
https://www.registrodeempresasysociedades.cl/MarcaDominio.aspx
https://www.rutificador.co/empresas/buscar
https://registros19862.gob.cl/
https://dequienes.cl/
"""
class Financiador(BaseModel):
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
