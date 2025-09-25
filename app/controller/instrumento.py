from fastapi import Request, APIRouter
from model.instrumento import * 
from view.instrumento import * 

router = APIRouter(prefix="/instrumento", tags=['instrumento'])

@router.get("")
async def VerTodosLosInstrumentos(request: Request):
    return TodosLosInstrumentos(request.app)

@router.get("/vigente")
async def VerInstrumentosVigentes(request: Request):
    return InstrumentosVigentes(request.app)

@router.get("/historico")
async def VerInstrumentosHistoricos(request: Request):
    return InstrumentosHistoricos(request.app)
