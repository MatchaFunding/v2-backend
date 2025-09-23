from pydantic import BaseModel
from model.beneficiario import *
import pandas as pd

def UnBeneficiario(id: int, app):
    return app.beneficiarios_json[id]

def TodosLosBeneficiarios(app):
    return app.beneficiarios_json
