from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine,AsyncSession
import os
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://receipt:receipt123@127.0.0.1:5433/receipt_judge",
)
engine = create_async_engine(DATABASE_URL,echo = False)
async_session = async_sessionmaker(engine,class_ = AsyncSession,expire_on_commit = False)

