#!/usr/bin/env python3
""" execute multiple coroutines at same time then returns list of dlys """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait_random n times with
    specified max_delay and returns list of dlays

    args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay for each wait_random

    returns:
        List[float]: list of delays in ascending order
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed = []
    for task in asyncio.as_completed(delays):
        delay = await task
        completed.append(delay)

    return completed
