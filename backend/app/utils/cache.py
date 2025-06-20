import json
from typing import Optional, Any
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

# Try to import redis, fallback to in-memory cache if not available
try:
    import redis
    redis_available = True
    redis_client = redis.Redis.from_url(settings.redis_url, decode_responses=True)
    # Test connection
    redis_client.ping()
    logger.info("Redis connection established")
except Exception as e:
    redis_available = False
    logger.warning(f"Redis not available: {e}. Using in-memory cache.")
    
    # Simple in-memory cache for development
    class InMemoryCache:
        def __init__(self):
            self.store = {}
        
        def get(self, key: str) -> Optional[str]:
            return self.store.get(key)
        
        def set(self, key: str, value: str, ex: Optional[int] = None):
            self.store[key] = value
            # Note: expiration not implemented in simple cache
        
        def setex(self, key: str, seconds: int, value: str):
            self.set(key, value, ex=seconds)
        
        def delete(self, key: str):
            if key in self.store:
                del self.store[key]
        
        def exists(self, key: str) -> bool:
            return key in self.store
    
    redis_client = InMemoryCache()

def cache_key(prefix: str, identifier: str) -> str:
    """Generate a cache key"""
    return f"{prefix}:{identifier}"

def get_cached(key: str) -> Optional[Any]:
    """Get value from cache"""
    try:
        data = redis_client.get(key)
        return json.loads(data) if data else None
    except Exception as e:
        logger.error(f"Cache get error: {e}")
        return None

def set_cached(key: str, value: Any, expire: int = 3600):
    """Set value in cache with expiration"""
    try:
        redis_client.setex(key, expire, json.dumps(value, default=str))
    except Exception as e:
        logger.error(f"Cache set error: {e}")

def delete_cached(key: str):
    """Delete value from cache"""
    try:
        redis_client.delete(key)
    except Exception as e:
        logger.error(f"Cache delete error: {e}")