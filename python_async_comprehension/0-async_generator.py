#!/usr/bin/env python3
""" this module Write a coroutine called
async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ yield a random num between 0 and 10 after 1 sec of waiting """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
