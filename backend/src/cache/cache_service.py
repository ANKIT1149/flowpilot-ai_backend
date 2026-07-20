from .redis import redis_client


class CacheService:
    async def get(self, key: str):
        return await redis_client.get(key)

    async def set(self, key: str, value: str, expire: int = 3600):
        await redis_client.set(key, value, ex=expire)

    async def delete(self, key: str):
        await redis_client.delete(key)

cache_service = CacheService();

