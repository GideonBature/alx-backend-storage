#!/usr/bin/env python3
"""15 Log stats - new version
add top 10 of the most present IPs in the collection
nginx of the database logs
"""
from pymongo import MongoClient

if __name__ == "__main__":
    nginx_collection = MongoClient().logs.nginx

    print(f"{nginx_collection.count_documents({})} logs")

    print(f"Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    method_get_count = nginx_collection.count_documents({"method": "GET",
                                                         "path": "/status"})
    print(f"{method_get_count} status check")

    ip_top_10 = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in ip_top_10:
        print(f"\t{ip['_id']}: {ip['count']}")
