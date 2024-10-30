#!/usr/bin/env python3
"""
LFUCache module implementing an LFU caching system.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache provides a caching system that follows the LFU algorithm.
    """
    def __init__(self):
        """
        Initialize the cache and call the parent class's init method.
        """
        super().__init__()
        self.count = {}
        self.recent = []

    def put(self, key, item):
        """
        Adds an item to cache_data and manages overflow using LFU and LRU.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        If the cache exceeds MAX_ITEMS,
        the least frequently used item is discarded.
        If multiple items have the same frequency,
        the least recently used is discarded.
        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.count[key] += 1
                self.recent.remove(key)
                self.recent.append(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    mn = min(self.count.values())
                    least = [k for k, freq in self.count.items() if freq == mn]

                    if len(least) > 1:
                        for old_key in self.recent:
                            if old_key in least:
                                discarded_key = old_key
                                break
                    else:
                        discarded_key = least[0]

                    del self.cache_data[discarded_key]
                    del self.count[discarded_key]
                    self.recent.remove(discarded_key)
                    print(f"DISCARD: {discarded_key}")

                self.cache_data[key] = item
                self.count[key] = 1
                self.recent.append(key)

    def get(self, key):
        """
        Retrieves an item from cache_data by key, updating its usage.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key in cache_data, or None
            if the key is None or doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        self.count[key] += 1

        self.recent.remove(key)
        self.recent.append(key)

        return item
