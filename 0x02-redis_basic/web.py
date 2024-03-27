#!/usr/bin/env python3
"""
web.py
"""
import redis
import requests
from functools import wraps

r = redis.Redis()


def count_requests(func):
    """Decorator to count how many times
    a URL was accessed.
    """
    @wraps(func)
    def wrapper(url):
        r.incr(f"count:{url}")
        return func(url)
    return wrapper


def cache_response(func):
    """Decorator to cache the
    response of a URL fetch.
    """
    @wraps(func)
    def wrapper(url):
        cached = r.get(url)
        if cached:
            return cached.decode("utf-8")
        else:
            html = func(url)
            r.setex(url, 10, html)
            return html
    return wrapper


@count_requests
@cache_response
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL,
    with caching and request counting.
    """
    response = requests.get(url)
    return response.text
