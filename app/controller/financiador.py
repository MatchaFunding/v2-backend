from fastapi import Request, APIRouter
from model.financiador import * 
from view.financiador import * 

router = APIRouter(prefix="/financiadores", tags=['financiadores'])

@router.get("")
async def VerTodosLosFinanciadores(request: Request):
    return TodosLosFinanciadores(request.app)
