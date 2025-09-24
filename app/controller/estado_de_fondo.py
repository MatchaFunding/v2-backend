from fastapi import Request, APIRouter
from model.estado_de_fondo import * 
from view.estado_de_fondo import * 

router = APIRouter(prefix="/estado_de_fondo", tags=['estado_de_fondo'])

@router.get("")
async def VerEstadosDeFondo(request: Request):
    return EstadosDeFondo(request.app)