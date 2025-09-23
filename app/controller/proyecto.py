from fastapi import Request, APIRouter
from model.proyecto import * 
from view.proyecto import * 

router = APIRouter(prefix="/proyecto", tags=['proyecto'])

@router.get("")
async def VerTodosLosProyectos(request: Request):
    return TodosLosProyectos(request.app)
