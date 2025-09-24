from pydantic import BaseModel
from model.tipo_de_beneficio import *

def TiposDeBeneficio(app):
    return app.tipos_de_beneficio