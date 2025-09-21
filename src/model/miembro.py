from pydantic import BaseModel
from typing import Optional
from .database import db_connection
import pandas as pd

# Lee todos los miembros y los guarda en un dataframe
miembros = pd.read_sql('SELECT * FROM VerMiembros', con=db_connection)
miembros_json = miembros.to_dict('records')
