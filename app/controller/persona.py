from fastapi import Request, APIRouter
from model.persona import * 
from view.persona import * 

router = APIRouter(prefix="/persona", tags=['persona'])

@router.get("")
async def VerTodasLasPersonas(request: Request):
    return TodasLasPersonas(request.app)
