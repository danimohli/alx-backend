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
        self.most_recent_keys = []

    def put(self, key, item):
        """
        Adds an item to cache_data and manages overflow using MRU.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the most recently used item is del
        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
                self.most_recent_keys.remove(key)

            self.cache_data[key] = item
            self.most_recent_keys.append(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = self.most_recent_keys.pop()
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieves item from cache_data by key marking it most recent used.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key in cache_data, or None
            if the key is None or doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]

        if key in self.most_recent_keys:
            self.most_recent_keys.remove(key)
        self.most_recent_keys.append(key)
        return item
