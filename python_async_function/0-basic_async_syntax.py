#!/usr/bin/env python3
""" Basic asynchronous that waits for random delay """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay and returns it

    args:
        max_delay (int): Maximum delay in seconds (default is 10).

    returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
