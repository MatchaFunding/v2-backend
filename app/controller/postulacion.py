from fastapi import Request, APIRouter
from model.postulacion import * 
from view.postulacion import * 

router = APIRouter(prefix="/postulaciones", tags=['postulaciones'])

@router.get("")
async def VerTodasLasPostulaciones(request: Request):
    return TodasLasPostulaciones(request.app)
