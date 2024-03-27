#!/usr/bin/env python3
"""
web.py
"""
import requests
import redis

redis_client = redis.Redis()


def get_page(url):
  """
  Fetches a webpage and caches the content with
  expiration in Redis.
  Tracks access count for the URL using Redis.
  """
  cached_content = redis_client.get(url)
  if cached_content:
    access_count = int(redis_client.incr(f"count:{url}")
    return cached_content.decode()

  response = requests.get(url)
  content = response.text
  redis_client.set(url, content, ex=10)
  redis_client.incr(f"count:{url}")
  return content
