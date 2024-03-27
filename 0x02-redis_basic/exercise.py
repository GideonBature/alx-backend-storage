#!/usr/bin/env python3
"""0. Writing strings to Redis
1. Reading from Redis and recovering
original type
"""
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Count calls
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Call history
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper

class Cache:
    """Cache class
    __init__ method to initialize redis
    store method to generate random key
    """
    def __init__(self) -> None:
        """Initialize redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key
        """
        key = str(uuid.uuid4())
        if isinstance(data, (int, float)):
            data = str(data)
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes,
                                                                    int, float]:
        """Get from redis
        """
        value = self._redis.get(name=key)
        if value is None:
            return value
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Get from redis
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Get from redis
        """
        value = self.get(key)
        return int(value) if value else None
