#!/usr/bin/env python3
""" Insert a document """


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document """

    doc= mongo_collection.insert_one(kwargs)
    return doc.inserted_id
