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
from controller import postulacion
from controller import persona
from controller import proyecto
from controller import tipo_de_beneficio
from controller import tipo_de_empresa
from controller import tipo_de_perfil
from controller import tipo_de_persona
from controller import estado_de_fondo
from controller import region
from controller import sexo

# Carga cada una de las tablas en dataframes para optimizar las lecturas y escrituras
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Se conecta a la base de datos para luego cargar las tablas en memoria
    configuracion = os.environ['MATCHA_CONF']
    conexion = create_engine(configuracion)
    # Instrumentos
    app.instrumentos = pd.read_sql('SELECT * FROM VerTodosLosInstrumentos', con=conexion)
    app.instrumentos_json = app.instrumentos.to_dict('records')
    # Beneficiarios
    app.beneficiarios = pd.read_sql('SELECT * FROM VerTodosLosBeneficiarios', con=conexion)
    app.beneficiarios_json = app.beneficiarios.to_dict('records')
    # Proyectos
    app.proyectos = pd.read_sql('SELECT * FROM VerTodosLosProyectos', con=conexion)
    app.proyectos_json = app.proyectos.drop(['Beneficiario'], axis=1).to_dict('records')
    # Postulaciones
    app.postulaciones = pd.read_sql('SELECT * FROM VerTodasLasPostulaciones', con=conexion)
    app.postulaciones_json = app.postulaciones.to_dict('records')
    # Ideas
    app.ideas = pd.read_sql('SELECT * FROM VerTodasLasIdeas', con=conexion)
    app.ideas_json = app.ideas.to_dict('records')
    # Personas
    app.personas = pd.read_sql('SELECT * FROM VerTodasLasPersonas', con=conexion)
    app.personas_json = app.personas.to_dict('records')
    # Miembros
    app.miembros = pd.read_sql('SELECT * FROM VerMiembros', con=conexion)
    app.miembros_json = app.miembros.to_dict('records')
    # Financiadores
    app.financiadores = pd.read_sql('SELECT * FROM VerTodosLosFinanciadores', con=conexion)
    app.financiadores_json = app.financiadores.to_dict('records')
    # Tipos y campos comunes
    app.tipos_de_beneficio = set(pd.read_sql('SELECT * FROM VerTiposDeBeneficio', con=conexion)["Nombre"])
    app.tipos_de_empresa = set(pd.read_sql('SELECT * FROM VerTiposDeEmpresa', con=conexion)["Nombre"])
    app.tipos_de_perfil = set(pd.read_sql('SELECT * FROM VerTiposDePerfil', con=conexion)["Nombre"])
    app.tipos_de_persona = set(pd.read_sql('SELECT * FROM VerTiposDePersona', con=conexion)["Nombre"])
    app.estados_de_fondo = set(pd.read_sql('SELECT * FROM VerEstadosDeFondo', con=conexion)["Nombre"])
    app.regiones = set(pd.read_sql('SELECT * FROM VerRegiones', con=conexion)["Nombre"])
    app.sexos = set(pd.read_sql('SELECT * FROM VerSexos', con=conexion)["Nombre"])
    yield

# Inicializa el servidor de FastAPI
app = FastAPI(title="MatchaFunding - API del BackEnd", lifespan=lifespan)

# Agrega los controladores a la aplicacion
app.include_router(beneficiario.router)
app.include_router(financiador.router)
app.include_router(instrumento.router)
app.include_router(postulacion.router)
app.include_router(persona.router)
app.include_router(proyecto.router)
app.include_router(tipo_de_beneficio.router)
app.include_router(tipo_de_empresa.router)
app.include_router(tipo_de_perfil.router)
app.include_router(tipo_de_persona.router)
app.include_router(estado_de_fondo.router)
app.include_router(region.router)
app.include_router(sexo.router)

# Permite conectarse remotamente a la API
origins = ["*"]
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
