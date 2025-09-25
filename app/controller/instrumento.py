from fastapi import Request, APIRouter
from model.instrumento import * 
from view.instrumento import * 

router = APIRouter(prefix="/instrumentos", tags=['instrumentos'])

@router.get("")
async def VerTodosLosInstrumentos(request: Request):
    return TodosLosInstrumentos(request.app)

@router.get("/vigentes")
async def VerInstrumentosVigentes(request: Request):
    return InstrumentosVigentes(request.app)

@router.get("/historicos")
async def VerInstrumentosHistoricos(request: Request):
    return InstrumentosHistoricos(request.app)
