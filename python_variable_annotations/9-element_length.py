#!/usr/bin/env python3
""" this module type-annotate element_length fucntion """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ this return a list of tuple with each element and legnth """
    return [(i, len(i)) for i in lst]
