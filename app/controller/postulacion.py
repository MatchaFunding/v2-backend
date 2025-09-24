from fastapi import Request, APIRouter
from model.postulacion import * 
from view.postulacion import * 

router = APIRouter(prefix="/postulacion", tags=['postulacion'])

@router.get("")
async def VerTodasLasPostulaciones(request: Request):
    return TodasLasPostulaciones(request.app)