from pydantic import BaseModel
from model.persona import *
import pandas as pd

def UnaPersona(id: int, app):
    return app.persona_json[id]

def TodasLasPersonas(app):
    return app.personas_json
