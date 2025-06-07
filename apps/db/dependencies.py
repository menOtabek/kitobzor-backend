from typing import AsyncGenerator
from apps.db.database import AsyncSessionLocal

async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        yield session
