from pydantic import BaseModel
from model.financiador import *
import pandas as pd

def TodosLosFinanciadores(app):
    return app.financiadores_json
