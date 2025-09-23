from pydantic import BaseModel
from model.sexo import *
import pandas as pd

def TodosLosSexos(app):
    return app.sexos_json
