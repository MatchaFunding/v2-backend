from pydantic import BaseModel
from typing import Optional
import pandas as pd

"""
Clase que representa a un usuario de MatchaFunding.
"""
class Usuario(BaseModel):
    Persona: Optional[int] = None
    NombreDeUsuario: str
    Contrasena: str
    Correo: str

def CrearNuevoUsuario(datos_de_usuario, id_persona, app):
    id_usuario = len(app.usuarios)
    usuario = dict(datos_de_usuario)
    usuario["Persona"] = id_persona
    app.usuarios.loc[id_usuario] = usuario
    app.usuarios_json = app.usuarios.to_dict('records')
    return usuario, id_usuario

def ExisteUsuarioConCorreo(correo, app):
    usuarios = app.usuarios.loc[(app.usuarios["Correo"] == correo)]
    if usuarios.shape[0] == 0:
        return False
    return True

def BuscarUsuarioPorCredenciales(credenciales, app):
    usuario = app.usuarios.loc[
        (app.usuarios["NombreDeUsuario"] == credenciales.NombreDeUsuario) |
        (app.usuarios["Correo"] == credenciales.Correo)
    ]
    usuario = usuario.loc[usuario["Contrasena"] == credenciales.Contrasena]
    return usuario

def EsValidoElUsuario(usuario):
    if usuario.shape[0] == 0:
        return False
    return True