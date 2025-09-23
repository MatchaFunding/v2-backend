from sqlalchemy import create_engine
from datetime import datetime
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pandas as pd
import sys
import os

# Importa todos los controladores
from controller import beneficiario
from controller import financiador
from controller import instrumento
from controller import persona
from controller import proyecto
from controller import sexo
from controller import usuario

# Carga cada una de las tablas en dataframes para optimizar las lecturas y escrituras
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Se conecta a la base de datos para luego cargar las tablas en memoria
    db_connection_str = os.environ['MATCHA_CONF']
    db_connection = create_engine(db_connection_str)
    # Instrumentos
    app.instrumentos = pd.read_sql('SELECT * FROM VerTodosLosInstrumentos', con=db_connection)
    app.instrumentos_json = app.instrumentos.to_dict('records')
    # Beneficiarios
    app.beneficiarios = pd.read_sql('SELECT * FROM VerTodosLosBeneficiarios', con=db_connection)
    app.beneficiarios_json = app.beneficiarios.to_dict('records')
    # Proyectos
    app.proyectos = pd.read_sql('SELECT * FROM VerTodosLosProyectos', con=db_connection)
    app.proyectos_json = app.proyectos.to_dict('records')
    # Postulaciones
    app.postulaciones = pd.read_sql('SELECT * FROM VerTodasLasPostulaciones', con=db_connection)
    app.postulaciones_json = app.postulaciones.to_dict('records')
    # Ideas
    app.ideas = pd.read_sql('SELECT * FROM VerTodasLasIdeas', con=db_connection)
    app.ideas_json = app.ideas.to_dict('records')
    # Personas
    app.personas = pd.read_sql('SELECT * FROM VerTodasLasPersonas', con=db_connection)
    app.personas_json = app.personas.to_dict('records')
    # Usuarios
    app.usuarios = pd.read_sql('SELECT * FROM VerTodosLosUsuarios', con=db_connection)
    app.usuarios_json = app.usuarios.to_dict('records')
    # Sexos
    app.sexos = pd.read_sql('SELECT * FROM VerSexos', con=db_connection)
    app.sexos_json = app.sexos.to_dict('records')
    # Miembros
    app.miembros = pd.read_sql('SELECT * FROM VerMiembros', con=db_connection)
    app.miembros_json = app.miembros.to_dict('records')
    # Financiadores
    app.financiadores = pd.read_sql('SELECT * FROM VerTodosLosFinanciadores', con=db_connection)
    app.financiadores_json = app.financiadores.to_dict('records')
    yield

# Inicializa el servidor de FastAPI
app = FastAPI(title="MatchaFunding - API del BackEnd", lifespan=lifespan)

# Agrega los controladores a la aplicacion
app.include_router(beneficiario.router)
app.include_router(financiador.router)
app.include_router(instrumento.router)
app.include_router(persona.router)
app.include_router(proyecto.router)
app.include_router(sexo.router)
app.include_router(usuario.router)

# Permite conectarse remotamente a la API
origins = ["http://localhost","http://localhost:8080","*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Para ver el estado de el servidor
@app.get("/")
def root():
    return {"message": "BackEnd activo!"}
