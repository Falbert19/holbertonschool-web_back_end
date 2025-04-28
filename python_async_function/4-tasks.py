#!/usr/bin/env python3
""" execute multiple tasks concurrently using task_wait_random """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns task_wait_random n times with
    specified max_delay and returns list of delays

    args:
        n (int): number of times to spawn task_wait_random
        max_delay (int): maximum delay for each task

    returns:
        List[float]: list of delays in ascending order
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    completed = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed.append(delay)

    return completed
