#!/usr/bin/env python3
""" create and return an asyncio.Task """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ returns an asyncio.Task
    that waits for a random delay

    args:
        max_delay (int): maximum delay for wait_random

    returns:
        asyncio.Task: the created asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
