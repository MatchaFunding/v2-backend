from fastapi import Request, APIRouter
from model.beneficiario import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/beneficiario", tags=['beneficiario'])

# Muestra todos los beneficiarios vigentes e historicos
@router.get("")
async def VerTodosLosBeneficiarios(request: Request):
    return request.app.beneficiarios_json

