"""
FastAPIs dependency injection capability to make the index_dal a dependency
of the endpoint. https://fastapi.tiangolo.com/tutorial/dependencies/
"""
from db.config import async_session
from db.dals.index_dal import IndexDAL


async def get_index_dal():
    async with async_session() as session:
        async with session.begin():
            yield IndexDAL(session)
