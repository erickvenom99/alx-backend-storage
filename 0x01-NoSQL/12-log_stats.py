#!/usr/bin/env python3

"""
Module provides stats about Nginx logs in MongoDB:
"""


from pymongo import MongoClient


def nginx_log_stats():
    """
    This function shows stats about Nginxs logs s
    """

    # Connecting to MongoDB
    mongo_client = MongoClient('mongodb://localhost:27017')
    database = mongo_client.logs
    collection = database.nginx

    # Number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # specific query count
    specific_get_method = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{specific_get_method} status check")


if __name__ == "__main__":
    nginx_log_stats()
