#!/usr/bin/env python3

"""
Module contains a function list_all only
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection, or an empty list.
    """
    all_docs = list(mongo_collection.find({}))
    return all_docs if all_docs else []
