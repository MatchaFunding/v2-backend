from fastapi import Request, APIRouter
from model.tipo_de_perfil import * 
from view.tipo_de_perfil import * 

router = APIRouter(prefix="/tipos_de_perfil", tags=['tipos_de_perfil'])

@router.get("")
async def VerTiposDePerfil(request: Request):
    return TiposDePerfil(request.app)
