#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
import math
from typing import List, Dict, Any


class Server:
    """ Server class to paginate a database """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server and prepare dataset cache"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset from the CSV file"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset
    
    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset
    
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Return paginated data that is resilient to deletion."""
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index < len(self.dataset())

        data = []
        current_index = index
        collected = 0

        while collected < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        return{
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data
        }
