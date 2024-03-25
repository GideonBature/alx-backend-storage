#!/usr/bin/env python3
"""Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection
    based on kwargs
    args:
        @mongo_collection: pymongo collection
        @kwargs: dictionary
    return:
        the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
