from fastapi import Request, APIRouter
from model.persona import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/persona", tags=['persona'])

# Muestra todos los personas abiertos e historicos
@router.get("")
async def VerTodasLasPersonas(request: Request):
    return request.app.personas_json
