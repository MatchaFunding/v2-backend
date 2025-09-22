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

# Crea un nuevo usuario en el sistema en base a los datos
# Devuelve al usuario recien creado y su identificador
def CrearNuevoUsuario(datos_de_usuario, id_persona, app):
    id_usuario = len(app.usuarios)
    usuario = dict(datos_de_usuario)
    usuario["Persona"] = id_persona
    app.usuarios.loc[id_usuario] = usuario
    app.usuarios_json = app.usuarios.to_dict('records')
    return usuario, id_usuario

# Funcion que verifica si el usuario existe en bazse a sus credenciales
def BuscarUsuarioPorCredenciales(credenciales, app):
    # Busca al usuario por nombre/correo o contrasena
    usuario_encontrado = app.usuarios.loc[
        (app.usuarios["NombreDeUsuario"] == credenciales.NombreDeUsuario) |
        (app.usuarios["Correo"] == credenciales.Correo)
    ]
    usuario = usuario_encontrado.loc[
        usuario_encontrado["Contrasena"] == credenciales.Contrasena
    ]
    # Devuelve el usuario encontrado, el cual puede ser valido o vacio
    return usuario

# Despues de buscar al usuario, corrobora si existe / es valido
def EsValidoElUsuario(usuario):
    if usuario.shape[0] == 0:
        return False
    return True
