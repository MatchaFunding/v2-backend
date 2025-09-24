from pydantic import BaseModel
from model.tipo_de_empresa import *

def TiposDeEmpresa(app):
    return app.tipos_de_empresa