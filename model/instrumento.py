from pydantic import BaseModel
from typing import Optional
from .database import db_connection
import pandas as pd

# Lee todos los instrumentos y los guarda en un dataframe
instrumentos = pd.read_sql('SELECT * FROM VerTodosLosInstrumentos', con=db_connection)
instrumentos_json = instrumentos.to_dict('records')
