from fastapi import Request, APIRouter
from model.tipo_de_empresa import * 
from view.tipo_de_empresa import * 

router = APIRouter(prefix="/tipos_de_empresa", tags=['tipos_de_empresa'])

@router.get("")
async def VerTiposDeEmpresa(request: Request):
    return TiposDeEmpresa(request.app)
