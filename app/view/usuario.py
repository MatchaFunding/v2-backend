from pydantic import BaseModel
from model.todos import *
import pandas as pd

# Obtiene los datos completos de la empresa en base al id del representante
def OrganizacionDeUsuario(usuario, app):
    # Primero obtiene el identificador de la persona
    id_persona = usuario.to_dict('records')[0]["Persona"]
    # Luego busca al usuarioo, omitiendo el campo id por temas de seguridad
    usuario = usuario.drop(['Persona'], axis=1).to_dict('records')[0]
    # La persona del usuario es el representante de la organizacion
    representante = app.miembros.loc[app.miembros["Persona"] == id_persona]
    representante = representante.to_dict('records')
    # Con lo anterior, se obtienen los datos del beneficiario
    id_beneficiario = representante[0]["Beneficiario"]
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
            "Miembros": miembros,
            "Ideas": [],
            "Propuestas": []
    }
    return organizacion
