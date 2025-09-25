from fastapi import Request, APIRouter
from model.tipo_de_beneficio import * 
from view.tipo_de_beneficio import * 

router = APIRouter(prefix="/tipos_de_beneficio", tags=['tipos_de_beneficio'])

@router.get("")
async def VerTiposDeBeneficio(request: Request):
    return TiposDeBeneficio(request.app)
