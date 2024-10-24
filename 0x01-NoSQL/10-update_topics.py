#!/usr/bin/env python3

"""
Module is a method that changes all topics of a 
school document based on the name
"""


from pymongo import MongoClient
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """
    Changes all topics of a school document based on the name.
    Args:
        mongo_collection: pymongo collection object.
        name (str): The school name to update.
        topics (List[str]): The list of topics approached in the school.
    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(filter_query, update)
