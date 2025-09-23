from fastapi import Request, APIRouter
from model.sexo import * 
from view.sexo import * 

# Maneja las rutas relacionadas a los sexos
router = APIRouter(prefix="/sexo", tags=['sexo'])

# Muestra todos los sexos validos para los formularios
@router.get("")
async def VerTodosLosSexos(request: Request):
    print("Depurando funcion de: Sexo")
    return TodosLosSexos(request.app)
