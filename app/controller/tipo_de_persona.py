from fastapi import Request, APIRouter
from model.tipo_de_persona import * 
from view.tipo_de_persona import * 

router = APIRouter(prefix="/tipo_de_persona", tags=['tipo_de_persona'])

@router.get("")
async def VerTiposDePersona(request: Request):
    return TiposDePersona(request.app)
