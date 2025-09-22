from sqlalchemy import create_engine
from datetime import datetime
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pandas as pd
import sys
import os

# Importa todos los modelos
from model.todos_los_modelos import * 

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
    yield

# Inicializa el servidor de FastAPI
app = FastAPI(title="MatchaFunding - API del BackEnd", lifespan=lifespan)

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

# Muestra todos los instrumentos abiertos e historicos
@app.get("/instrumento")
async def VerTodosLosInstrumentos():
    return app.instrumentos_json

# Muestra todos los proyectos abiertos e historicos
@app.get("/proyecto")
async def VerTodosLosProyectos():
    return app.proyectos_json

# Muestra todos los beneficiarios vigentes e historicos
@app.get("/beneficiario")
async def VerTodosLosBeneficiarios():
    return app.beneficiarios_json

# Muestra todos los beneficiarios vigentes e historicos
@app.get("/beneficiario/{id}")
async def ObtenerBeneficiario(id: int):
    return app.beneficiarios_json[id]

# Muestra todos los proyectos vigentes e historicos
@app.get("/proyecto")
async def VerTodosLosProyectos():
    return app.proyectos_json

# Muestra todas las personas en el sistema registradas
@app.get("/persona")
async def VerTodasLasPersonas():
    return app.personas_json

# Muestra todos los usuarios en el sistema registradas
@app.get("/usuario")
async def VerTodosLosUsuarios():
    return app.usuarios_json

# Obtiene un usuario especifico por su identificador
@app.get("/usuario/{id}")
async def ObtenerUsuario(id: int):
    return app.usuarios_json[id]

# Muestra todos los miembros en el sistema registradas
@app.get("/miembro")
async def VerMiembros():
    return app.miembros_json

# Muestra todos los sexos validos para los formularios
@app.get("/sexo")
async def VerSexos():
    return app.sexos_json

# Permite el detalle de un sexo especifico
@app.get("/sexo/{id}")
async def VerSexo(id: int):
    return app.sexos_json[id]

# Permite agregar un sexo nuevo al sistema
@app.post("/sexo")
async def CrearSexo(sexo: Sexo):
    app.sexos.loc[len(app.sexos)] = dict(sexo)
    app.sexos_json = app.sexos.to_dict('records')
    return dict(sexo)

# Crea un usuario a partir de un nombre, correo y contrasena
@app.post("/usuario/registrar")
async def RegistrarUsuario(datos: Registro):
    persona, id_persona = CrearNuevaPersona(datos.Persona, app)
    usuario, _ = CrearNuevoUsuario(datos.Usuario, id_persona, app)
    beneficiario, id_beneficiario = CrearNuevoBeneficiario(datos.Beneficiario, app)
    miembro, _ = CrearMiembroDesdeIDs(id_persona, id_beneficiario, app)
    return {"message": "Usuario registrado exitosamente!"}

# Valida los datos del usuario y devuelve la organizacion completa
# Tambien sirve para actualizar los datos del usuario de forma segura
@app.post("/usuario/autenticar")
async def AutenticarUsuario(credenciales: Usuario):
    usuario = BuscarUsuarioPorCredenciales(credenciales, app)
    if not EsValidoElUsuario(usuario):
        return {"message": "Credenciales incorrectas!"}
    return VerOrganizacion(usuario, app)

# Permite actualizar los datos de la organizacion de un usuario concreto
# (proyectos, miembros, empresa, etc.).
# El usuario que invoque esta API debe suminstrar sus credenciales para
# hacer la modificacion de forma segura.
@app.post("/usuario/modificar")
async def ModificarUsuario(organizacion: Organizacion):
    credenciales = organizacion.Usuario
    usuario = BuscarUsuarioPorCredenciales(credenciales, app)
    if not EsValidoElUsuario(usuario):
        return {"message": "Credenciales incorrectas!"}
    return VerOrganizacion(usuario, app)
    # TODO: crear funcion nueva que modifique los datos del usuario
