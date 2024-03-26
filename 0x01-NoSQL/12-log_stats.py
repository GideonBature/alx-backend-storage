#!/usr/bin/env python3
"""12 Log stats
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    print(f"{nginx_collection.count_documents({})} logs")

    print(f"Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    method_get_count = nginx_collection.count_documents({"method": "GET",
                                                         "path": "/status"})
    print(f"{method_get_count} status check")
