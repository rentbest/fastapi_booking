from app.database import async_session

from sqlalchemy import select, insert, update, delete


class BaseDAO:
    """
    Base class for operations with database.
    All is need for working to pass 'model'
    """
    model = None

    @classmethod
    async def read_all(cls):
        async with async_session() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def read_by_parameters(cls, **params):
        async with async_session() as session:
            if params:
                query = select(cls.model).filter_by(**params)
            else:
                query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def create(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            new_object = result.scalars().first()
            await session.commit()
            return new_object
        
    
    @classmethod
    async def update(cls, id: int, **data):
        async with async_session() as session:
            query = update(cls.model).where(cls.model.id==id).values(**data).returning(cls.model)
            result = await session.execute(query)
            updated_object = result.scalars().first()
            await session.commit()
            return updated_object


    @classmethod
    async def delete(cls, id: int):
        async with async_session() as session:
            query = delete(cls.model).where(cls.model.id==id).returning(cls.model.id)
            await session.execute(query)
            await session.commit()
        