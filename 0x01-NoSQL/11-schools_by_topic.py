#!/usr/bin/env python3

"""
Module returns a list of school
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function returns a list of specific topic
    Args:
        mongo_collection: Pymongo collection object
        topic: topic searched
    """
    query = {"topics": {"$in": [topic] }}
    specific_topic = list(mongo_collection.find(query))

    return specific_topic
