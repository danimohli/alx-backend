#!/usr/bin/env python3
"""LIFOCache module implementing a LIFO caching system."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache provides a caching system that follows the LIFO algorithm.
    """

    def __init__(self):
        """
        Initialize the cache and call the parent class's init method.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Adds an item to cache_data and manages overflow using LIFO.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS,
        the most recently added item is discarded.
        If either key or item is None, this method does nothing.
        """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from cache_data by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key in cache_data, or None
            if the key is None or doesn't exist.
        """
        return self.cache_data.get(key, None)
