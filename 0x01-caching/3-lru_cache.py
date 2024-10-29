#!/usr/bin/env python3
"""
LRUCache module implementing an LRU caching system.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache provides a caching system that follows the LRU algorithm.
    """

    def __init__(self):
        """
        Initialize the cache and call the parent class's init method.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to cache_data and manages overflow using LRU.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the least recently used item is del
        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:

                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieves an item from cache_data by key,
        moving it to the most recent end.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key in cache_data, or None
            if the key is None or doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
