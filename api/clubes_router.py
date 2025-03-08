from fastapi import APIRouter

from api.schemas.clubeSchema import ClubesSchema, ClubesSchemaUpdate
from services.clubeService import criar_clube, deletar_clube, get_all_clubes, update_clube


router = APIRouter(prefix='/clubes', tags=['clubes'])


@router.get('/')
def get_clubes():
    clubes = get_all_clubes()
    return clubes

@router.post('/add')
def add_clube(clube: ClubesSchema):
    criar_clube(clube.nome, clube.serie, clube.escudo)
    return clube

@router.delete('/delete/{clube_id}')
def delete_clube(clube_id: int):
    return deletar_clube(clube_id)


@router.put('/update/{clube_id}')
def alterar_clube(clube_id: int, clube_update: ClubesSchemaUpdate):  
    return update_clube(clube_id, clube_update)