#!/usr/bin/env python3
""" this module has a coroutine that will collect 10 random numbers """
from typing import List
async_generator = __import__('0-async_generator').async_generator



async def async_comprehension() -> List[float]:
    """ Collect 10 random floats from async_generator
    and return them as a list """
    return [i async for i in async_generator()]
