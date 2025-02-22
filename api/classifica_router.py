from typing import List

from fastapi import APIRouter

from schemas import ClassificacaoUpdate
from services import get_classifications

router = APIRouter(prefix='/classificacao', tags=['classificacao'])


@router.get('/', response_model=List[ClassificacaoUpdate])
def get_stading():
    classificacao = get_classifications
    return classificacao
