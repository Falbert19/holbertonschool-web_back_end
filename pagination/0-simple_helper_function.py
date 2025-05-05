#!/usr/bin/env python3
""" this module task 2 integers args and return a tuple of size """


def index_range(page: int, page_size: int) -> tuple:
    """ Returns a tuple of start and end for pagination """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
