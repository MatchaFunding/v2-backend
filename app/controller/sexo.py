from fastapi import Request, APIRouter
from model.sexo import * 
from view.sexo import * 

router = APIRouter(prefix="/sexos", tags=['sexos'])

@router.get("")
async def VerTodosLosSexos(request: Request):
    return TodosLosSexos(request.app)
