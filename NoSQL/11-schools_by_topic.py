#!/usr/bin/env python3
""" find schools by topic """


def schools_by_topic(mongo_collection, topic):
    """ return a list of schools """
    return mongo_collection.find({ "topics": topic })
