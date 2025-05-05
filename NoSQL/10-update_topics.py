#!/usr/bin/env python3
""" update topics of doc """


def update_topics(mongo_collection, name, topics):
    """" updates the topics of school doc """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
