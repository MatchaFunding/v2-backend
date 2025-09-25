from pydantic import BaseModel
from model.proyecto import *
import pandas as pd

def UnProyecto(id: int, app):
    return app.proyectos_json[id]

def TodosLosProyectos(app):
    return app.proyectos_json

def ProyectosAdjudicados(app):
    adjudicados = app.postulaciones.loc[
        app.postulaciones["Resultado"] == "Adjudicado"
    ]
    id_proyectos = adjudicados["Proyecto"].to_numpy() - 1
    proyectos = app.proyectos.iloc[id_proyectos]
    proyectos = proyectos.to_dict('records')
    return proyectos

def ProyectosRechazados(app):
    rechaazados = app.postulaciones.loc[
        app.postulaciones["Resultado"] == "Rechazado"
    ]
    id_proyectos = rechaazados["Proyecto"].to_numpy() - 1
    proyectos = app.proyectos.iloc[id_proyectos]
    proyectos = proyectos.to_dict('records')
    return proyectos

def ProyectosPendientes(app):
    rechaazados = app.postulaciones.loc[
        app.postulaciones["Resultado"] == "Pendiente"
    ]
    id_proyectos = rechaazados["Proyecto"].to_numpy() - 1
    proyectos = app.proyectos.iloc[id_proyectos]
    proyectos = proyectos.to_dict('records')
    return proyectos