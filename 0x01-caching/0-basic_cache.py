#!/usr/bin/env python3
"""
BasicCache module implementing an unlimited caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache provides a basic caching system with no size limit.
    """

    def put(self, key, item):
        """
        Adds an item to the cache_data dictionary.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
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
