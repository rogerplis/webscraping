from typing import List

from fastapi import APIRouter


from services.classificacaoService import get_classifications

router = APIRouter(prefix='/classificacao', tags=['classificacao'])


@router.get('/')
def get_stading():
    classificacao = get_classifications()
    return classificacao
