#!/usr/bin/env python3
"""10 Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name
    args:
        @mongo_collection: pymongo collection
        @name: name
        @topics: list
    return:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
