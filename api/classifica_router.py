from typing import List

from fastapi import APIRouter

from api.schemas import ClassificacaoUpdate
from api.services import get_classifications

router = APIRouter(prefix='/classificacao', tags=['classificacao'])


@router.get('/', response_model=List[ClassificacaoUpdate])
def get_stading():
    classificacao = get_classifications
    return classificacao
