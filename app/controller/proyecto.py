from fastapi import Request, APIRouter
from model.proyecto import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/proyecto", tags=['proyecto'])

# Muestra todos los proyectos vigentes e historicos
@router.get("")
async def VerTodosLosProyectos(request: Request):
    return request.app.proyectos_json
