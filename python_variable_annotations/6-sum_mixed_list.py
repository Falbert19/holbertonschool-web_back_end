#!/usr/bin/env python3
""" this module type annotate the sum_mixed_list function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ this return the sum of a list of ints and floats as float"""
    return sum(mxd_lst)
