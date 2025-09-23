from fastapi import Request, APIRouter
from model.instrumento import * 
from view.instrumento import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/instrumento", tags=['instrumento'])

# Muestra todos los instrumentos abiertos e historicos
@router.get("")
async def VerTodosLosInstrumentos(request: Request):
    return TodosLosInstrumentos(request.app)
