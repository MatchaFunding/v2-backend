from fastapi import Request, APIRouter
from model.proyecto import * 
from view.proyecto import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/proyecto", tags=['proyecto'])

# Muestra todos los proyectos vigentes e historicos
@router.get("")
async def VerTodosLosProyectos(request: Request):
    return TodosLosProyectos(request.app)
