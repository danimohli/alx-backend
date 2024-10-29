#!/usr/bin/env python3
"""
FIFOCache module implementing a FIFO caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache provides a caching system that follows the FIFO algorithm.
    """

    def __init__(self):
        """
        Initialize the cache and call the parent class's init method."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to cache_data and manages overflow using FIFO.
        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS, the oldest item is discarded.
        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

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
