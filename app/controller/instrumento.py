from fastapi import Request, APIRouter
from model.instrumento import * 
from view.instrumento import * 

router = APIRouter(prefix="/instrumento", tags=['instrumento'])

@router.get("")
async def VerTodosLosInstrumentos(request: Request):
    return TodosLosInstrumentos(request.app)
