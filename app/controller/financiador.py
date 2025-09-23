from fastapi import Request, APIRouter
from model.financiador import * 
from view.financiador import * 

router = APIRouter(prefix="/financiador", tags=['financiador'])

@router.get("")
async def VerTodosLosFinanciadores(request: Request):
    return TodosLosFinanciadores(request.app)
