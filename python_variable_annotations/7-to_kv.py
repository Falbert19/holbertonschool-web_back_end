#!/usr/bin/env python3
""" this module type annotate to_kv function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ this return a tuple with str and square of an int or float"""
    return (k, float(v ** 2))
