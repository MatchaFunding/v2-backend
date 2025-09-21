from sqlalchemy import create_engine
from datetime import datetime
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pandas as pd
import sys
import os

# Importa todos los modelos
from model.todos import * 

# Carga cada una de las tablas en dataframes con para optimizar las lecturas y escrituras
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Se conecta a la base de datos para luego cargar los datos en memoria
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
    app.ideas_json = app.ideas.to_dict('records')A
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


# Obtiene los datos completos de la empresa en base al id del representante
def VerOrganizacion(usuario):
    # Primero obtiene el identificador de la persona
    id_persona = usuario.to_dict('records')[0]["Persona"]
    # Se omite la el campo id por temas de seguridad
    usuario = usuario.drop(['Persona'], axis=1).to_dict('records')[0]
    # La persona del usuario es el representante de la organizacion
    representante = app.miembros.loc[app.miembros["Persona"] == id_persona]
    # Con lo anterior, se obtienen los datos del beneficiario
    id_beneficiario = representante.to_dict('records')[0]["Beneficiario"]
    beneficiario = app.beneficiarios_json[id_beneficiario]
    # Con el identificador del beneficiario se obtiene el resto de los objetos
    proyectos = app.proyectos.loc[app.proyectos["Beneficiario"] == id_beneficiario]
    proyectos = proyectos.to_dict('records')
    postulaciones = app.postulaciones.loc[app.postulaciones["Beneficiario"] == id_beneficiario]
    postulaciones = postulaciones.to_dict('records')
    # Muestra los miembros con el modelo de persona
    id_miembros = app.miembros.loc[app.miembros["Beneficiario"] == id_beneficiario]
    id_miembros = id_miembros["Persona"].to_numpy()
    miembros = app.personas.iloc[id_miembros]
    miembros = miembros.to_dict('records')
    # Se muestran todos los assets de la organizacion en formato JSON
    organizacion = {
            "Usuario": usuario,
            "Beneficiario": beneficiario,
            "Proyectos": proyectos,
            "Postulaciones": postulaciones,
            "Representante": miembros[0],
            "Miembros": miembros[1:],
            "Ideas": [],
            "Propuestas": []
    }
    return organizacion

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
async def ObtenerBeneficiario(id):
    return app.beneficiarios_json[int(id)]

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
async def ObtenerUsuario(id):
    return app.usuarios_json[int(id)]

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
async def VerSexo(id):
    return app.sexos_json[int(id)]

# Permite agregar un sexo nuevo al sistema
@app.post("/sexo")
async def CrearSexo(sexo: Sexo):
    app.sexos.loc[len(app.sexos)] = dict(sexo)
    app.sexos_json = app.sexos.to_dict('records')
    return dict(sexo)

# Crea un usuario a partir de un nombre, correo y contrasena
@app.post("/usuario/registrar")
async def RegistrarUsuario(datos: Registro):
    # Primero crea la persona para crear los otros objetos despues
    id_persona = len(app.personas) # ID que tendra la persona
    persona = datos.Persona
    persona = dict(persona)
    app.personas.loc[id_persona] = persona
    app.personas_json = app.personas.to_dict('records')
    # Al crear la persona, el usuario adquiere su ID como FK
    usuario = datos.Usuario
    usuario = dict(usuario)
    usuario["Persona"] = id_persona
    app.usuarios.loc[len(app.usuarios)] = usuario
    app.usuarios_json = app.usuarios.to_dict('records')
    # Luego se crea el beneficiario
    id_beneficiario = len(app.beneficiarios) # ID que tendra el beneficiario
    beneficiario = datos.Beneficiario
    beneficiario = dict(beneficiario)
    app.beneficiarios.loc[len(app.beneficiarios)] = beneficiario
    app.beneficiarios_json = app.beneficiarios.to_dict('records')
    # Finalmente se crea al usuario como miembro
    miembro = {"Persona": id_persona, "Beneficiario": id_beneficiario}
    app.miembros.loc[len(app.miembros)] = miembro
    app.miembros_json = app.miembros.to_dict('records')
    # La funcion devuelve la organizacion completa creada del usuario
    organizacion = {
            "Usuario": usuario,
            "Beneficiario": beneficiario
    }
    return organizacion

# Valida los datos del usuario y devuelve la organizacion completa
# Tambien sirve para actualizar los datos del usuario de forma segura
@app.post("/usuario/autenticar")
async def AutenticarUsuario(credenciales: Usuario):
    usuario_encontrado = app.usuarios.loc[
        (app.usuarios["NombreDeUsuario"] == credenciales.NombreDeUsuario) |
        (app.usuarios["Correo"] == credenciales.Correo)
    ]
    usuario_valido = usuario_encontrado.loc[
        usuario_encontrado["Contrasena"] == credenciales.Contrasena
    ]
    # Si la query resulta en cero filas, las credenciaales eran invalidas
    if usuario_valido.shape[0] == 0:
        return {"message": "Credenciales incorrectas!"}
    return VerOrganizacion(usuario_valido)

# Permite actualizar los datos de la organizacion de un usuario concreto
# (proyectos, miembros, empresa, etc.).
# El usuario que invoque esta API debe suminstrar sus credenciales para
# hacer la modificacion de forma segura.
@app.post("/usuario/modificar")
async def ModificarUsuario(organizacion: Organizacion):
    usuario = organizacion.Usuario
    usuario_encontrado = app.usuarios.loc[
        (app.usuarios["NombreDeUsuario"] == usuario.NombreDeUsuario) |
        (app.usuarios["Correo"] == usuario.Correo)
    ]
    usuario_valido = usuario_encontrado.loc[
        usuario_encontrado["Contrasena"] == usuario.Contrasena
    ]
    # Si la query resulta en cero filas, las credenciaales eran invalidas
    if usuario_valido.shape[0] == 0:
        return {"message": "Credenciales incorrectas!"}
    # TODO: crear funcion nueva que modifique los datos del usuario
    return VerOrganizacion(usuario_valido)
