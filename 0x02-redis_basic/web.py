#!/usr/bin/env python3
"""
web.py
"""
import requests
import redis
from functools import wraps

redis_client = redis.Redis()


def count_access(func):
    """Decorator to count the number of accesses to a URL."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Increment the access count for the URL
        url = args[0]  # Assuming the first argument is the URL
        redis_client.incr(f"count:{url}")
        return func(*args, **kwargs)
    return wrapper


def cache_page(expiration_time=10):
    """Decorator to cache the page content with an expiration time."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]  # Assuming the first argument is the URL
            # Attempt to get the cached content
            cached_content = redis_client.get(url)
            if cached_content:
                return cached_content.decode()
            else:
                # Fetch the page content as it's not cached
                content = func(*args, **kwargs)
                # Cache the content with the specified expiration time
                redis_client.setex(url, expiration_time, content)
                return content
        return wrapper
    return decorator


@count_access
@cache_page(expiration_time=10)
def get_page(url: str) -> str:
    """Obtain the HTML content of a given URL."""
    response = requests.get(url)
    return response.text
