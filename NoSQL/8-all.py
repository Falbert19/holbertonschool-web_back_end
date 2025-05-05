#!/usr/bin/env python3
""" List all documents """
from typing import List


def list_all(mongo_collection: object) -> List:
    """Return all documents in the collection, or an empty list"""

    docs = list(mongo_collection.find())
    return docs
