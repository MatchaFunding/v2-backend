from fastapi import Request, APIRouter
from model.beneficiario import * 
from view.beneficiario import * 

router = APIRouter(prefix="/beneficiario", tags=['beneficiario'])

@router.get("")
async def VerTodosLosBeneficiarios(request: Request):
    return TodosLosBeneficiarios(request.app)