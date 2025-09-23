from fastapi import Request, APIRouter
from model.todos import * 
from view.usuario import * 

router = APIRouter(prefix="/usuario", tags=['usuario'])

@router.post("/registrar")
async def RegistrarUsuario(datos: Registro, request: Request):
    persona, id_persona = CrearNuevaPersona(datos.Persona, request.app)
    usuario, _ = CrearNuevoUsuario(datos.Usuario, id_persona, request.app)
    beneficiario, id_beneficiario = CrearNuevoBeneficiario(datos.Beneficiario, request.app)
    datos_de_miembro = {"Persona": id_persona, "Beneficiario": id_beneficiario}    
    miembro, _ = CrearNuevoMiembro(datos_de_miembro, request.app)
    return {"message": "Usuario registrado exitosamente!"}

@router.post("/autenticar")
async def AutenticarUsuario(credenciales: Usuario, request: Request):
    usuario = BuscarUsuarioPorCredenciales(credenciales, request.app)
    if not EsValidoElUsuario(usuario):
        return {"message": "Credenciales incorrectas!"}
    return OrganizacionDeUsuario(usuario, request.app)

@router.post("/modificar")
async def ModificarUsuario(organizacion: Organizacion, request: Request):
    credenciales = organizacion.Usuario
    usuario = BuscarUsuarioPorCredenciales(credenciales, request.app)
    if not EsValidoElUsuario(usuario):
        return {"message": "Credenciales incorrectas!"}
    return OrganizacionDeUsuario(usuario, request.app)
    # TODO: crear funcion nueva que modifique los datos del usuario
