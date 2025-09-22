from fastapi import Request, APIRouter

# Maneja las rutas relacionadas a los sexos
sexo_controlador = APIRouter()

# Muestra todos los sexos validos para los formularios
@router.get("/sexo", tags=['sexo'])
async def VerSexos(request: Request):
    return request.app.state.sexos_json

# Permite el detalle de un sexo especifico
@router.get("/sexo/{id}", tags=['sexo'])
async def VerSexo(request: Request, id):
    return request.app.state.sexos_json[int(id)]

# Permite agregar un sexo nuevo al sistema
@router.post("/sexo", tags=['sexo'])
async def CrearSexo(request: Request, sexo: Sexo):
    request.app.state.sexos.loc[len(request.app.state.sexos)] = dict(sexo)
    request.app.state.sexos_json = request.app.state.sexos.to_dict('records')
    return dict(sexo)

