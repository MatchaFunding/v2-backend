from fastapi import Request, APIRouter
from model.todos import * 
from view.usuario import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/usuario", tags=['usuario'])

# Crea un usuario a partir de un nombre, correo y contrasena
@router.post("/registrar")
async def RegistrarUsuario(datos: Registro, request: Request):
    persona, id_persona = CrearNuevaPersona(datos.Persona, request.app)
    usuario, _ = CrearNuevoUsuario(datos.Usuario, id_persona, request.app)
    beneficiario, id_beneficiario = CrearNuevoBeneficiario(datos.Beneficiario, request.app)
    datos_de_miembro = {"Persona": id_persona, "Beneficiario": id_beneficiario}    
    miembro, _ = CrearNuevoMiembro(datos_de_miembro, request.app)
    return {"message": "Usuario registrado exitosamente!"}

# Valida los datos del usuario y devuelve la organizacion completa
# Tambien sirve para actualizar los datos del usuario de forma segura
@router.post("/autenticar")
async def AutenticarUsuario(credenciales: Usuario, request: Request):
    usuario = BuscarUsuarioPorCredenciales(credenciales, request.app)
    if not EsValidoElUsuario(usuario):
        return {"message": "Credenciales incorrectas!"}
    return OrganizacionDeUsuario(usuario, request.app)

# Permite actualizar los datos de la organizacion de un usuario concreto
# (proyectos, miembros, empresa, etc.).
# El usuario que invoque esta API debe suminstrar sus credenciales para
# hacer la modificacion de forma segura.
@router.post("/modificar")
async def ModificarUsuario(organizacion: Organizacion, request: Request):
    credenciales = organizacion.Usuario
    usuario = BuscarUsuarioPorCredenciales(credenciales, request.app)
    if not EsValidoElUsuario(usuario):
        return {"message": "Credenciales incorrectas!"}
    return OrganizacionDeUsuario(usuario, request.app)
    # TODO: crear funcion nueva que modifique los datos del usuario
