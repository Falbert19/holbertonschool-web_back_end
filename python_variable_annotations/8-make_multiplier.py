#!/usr/bin/env python3
""" this module type-annotate make_multiplier function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ this return a function that multiplier a float by multipler """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
