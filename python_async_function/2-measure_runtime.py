#!/usr/bin/env python3
""" measure the time running fo execute wait_n """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures total execution time for
    wait_n(n, max_delay) and returns average time per task

    args:
        n (int): number of times wait_random is spawned
        max_delay (int): maximum delay for each wait_random

    returns:
        float: total_time divided by n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time
