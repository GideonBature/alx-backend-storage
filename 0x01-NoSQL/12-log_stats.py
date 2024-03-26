#!/usr/bin/env python3
"""12 Log stats
"""


db_collection = __import__('pymongo').MongoClient().logs.nginx

print(f"{db_collection.count_documents({})} logs")

print(f"Methods:")

for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = db_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

method_get_count = db_collection.count_documents({"method": "GET",
                                                  "path": "/status"})
print(f"{method_get_count} status check")
