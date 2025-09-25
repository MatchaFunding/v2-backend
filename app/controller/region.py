from fastapi import Request, APIRouter
from model.region import * 
from view.region import * 

router = APIRouter(prefix="/regiones", tags=['regiones'])

@router.get("")
async def VerTodasLasRegiones(request: Request):
    return TodasLasRegiones(request.app)
