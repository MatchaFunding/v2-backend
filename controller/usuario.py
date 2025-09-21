from ..main import *

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
