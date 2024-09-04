from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

metadata = MetaData()

Base = declarative_base(metadata=metadata)
