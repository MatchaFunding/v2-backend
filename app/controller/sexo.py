from fastapi import Request, APIRouter
from model.sexo import * 
from view.sexo import * 

router = APIRouter(prefix="/sexo", tags=['sexo'])

@router.get("")
async def VerTodosLosSexos(request: Request):
    return TodosLosSexos(request.app)