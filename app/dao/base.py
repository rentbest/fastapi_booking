from app.database import async_session

from sqlalchemy import select


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def find_by_parameters(cls, **params):
        async with async_session() as session:
            query = select(cls.model).filter_by(**params)
            result = await session.execute(query)
            return result.scalars().all()