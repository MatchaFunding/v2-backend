from fastapi import Request, APIRouter
from model.instrumento import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/instrumento", tags=['instrumento'])

# Muestra todos los instrumentos abiertos e historicos
@router.get("")
async def VerTodosLosInstrumentos(request: Request):
    return request.app.instrumentos_json
