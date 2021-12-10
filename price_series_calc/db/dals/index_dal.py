from sqlalchemy.future import select
from sqlalchemy.orm import Session

from price_series_calc.db.models.index import Index


class IndexDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_index(self, id, weight, prices):
        new_index = Index(id=id, weight=weight, prices=prices)
        self.db_session.add(new_index)
        await self.db_session.flush()

    async def get_all_indices(self):
        q = await self.db_session.execute(select(Index).order_by(Index.id))
        return q.scalars().all()

    async def get_index(self, id):
        q = await self.db_session.execute(select(Index).where(Index.id == id))
        return q.scalars().all()
