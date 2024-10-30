#!/usr/bin/env python3
"""
MRUCache module implementing an MRU caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache provides a caching system that follows the MRU algorithm.
    """

    def __init__(self):
        """
        Initialize the cache and call the parent class's init method.
        """
        super().__init__()
        self.recent_keys = []

    def put(self, key, item):
        """
        Adds an item to cache_data and manages overflow using MRU.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the most recently used item is del
        If either key or item is None, this method does nothing.
        """
        if key and item:
            if self.cache_data.get(key):
                self.recent_keys.remove(key)
            while len(self.recent_keys) >= self.MAX_ITEMS:
                delet = self.recent_keys.pop()
                self.cache_data.pop(delet)
                print("DISCARD: {}".format(delet))
            self.recent_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves item from cache_data by key marking it most recent used.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key in cache_data, or None
            if the key is None or doesn't exist.
        """
        if self.cache_data.get(key):
            self.recent_keys.remove(key)
            self.recent_keys.append(key)
        return self.cache_data.get(key)
