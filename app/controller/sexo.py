from fastapi import Request, APIRouter
from model.sexo import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/sexo", tags=['sexo'])

# Muestra todos los sexos validos para los formularios
@router.get("")
async def VerSexos(request: Request):
    print("Depurando funcion de: Sexo")
    return request.app.sexos_json

# Permite el detalle de un sexo especifico
@router.get("/{id}")
async def VerSexo(request: Request, id: int):
    return request.app.sexos_json[id]
