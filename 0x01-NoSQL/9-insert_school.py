#!/usr/bin/env python3

"""
Module inserts an new  document to mongo_collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection.
        **kwargs: Keyword arguments representing the document to insert.

    Returns:
        The _id of the new document inserted.
    """
    new_docs = mongo_collection.insert_one(kwargs)
    return new_docs.inserted_id
