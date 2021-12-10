from fastapi import APIRouter, Depends

from price_series_calc.db.dals.index_dal import IndexDAL
from price_series_calc.db.models.index import Index
from price_series_calc.dependencies import get_index_dal

router = APIRouter()


@router.post("/indices")
async def create_index(index_id, weight, prices, index_dal: IndexDAL = Depends(get_index_dal)):
    return await index_dal.create_index(index_id, weight, prices)


@router.get("/index/{index_id}")
async def get_book(index_id, index_dal: IndexDAL = Depends(get_index_dal)):
    return await index_dal.get_index(index_id, index_id)


@router.get("/indices")
async def get_all_books(index_dal: IndexDAL = Depends(get_index_dal)):
    return await index_dal.get_all_indices()
