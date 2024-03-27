#!/usr/bin/env python3
"""0. Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class
    __init__ method to initialize redis
    store method to generate random key
    """
    def __init__(self):
        """Initialize redis
        """
        self._redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
