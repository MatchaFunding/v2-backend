from fastapi import Request, APIRouter
from model.proyecto import * 
from view.proyecto import * 

router = APIRouter(prefix="/proyectos", tags=['proyectos'])

@router.get("")
async def VerTodosLosProyectos(request: Request):
    return TodosLosProyectos(request.app)

@router.get("/adjudicado")
async def VerProyectosAdjudicados(request: Request):
    return ProyectosAdjudicados(request.app)

@router.get("/rechazado")
async def VerProyectosRechazados(request: Request):
    return ProyectosRechazados(request.app)

@router.get("/pendiente")
async def VerProyectosPendientes(request: Request):
    return ProyectosPendientes(request.app)
