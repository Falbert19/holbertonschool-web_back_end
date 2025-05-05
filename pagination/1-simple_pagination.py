#!/usr/bin/env python3
""" Implement a method named get_page that
takes two integer arguments page with
default value 1 and page_size with default value 10."""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """ Server class to paginate a database """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server and prepare dataset cache"""
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset from the CSV file"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a specific page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end] if start < len(data) else []
