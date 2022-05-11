#!/usr/bin/env python3
""" asdaspdsapap asdasdasdal"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ caching system sadsadas"""
    def put(self, key, item):
        if item is None or key is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ get a key by item asdasdasdsa"""
        if key is None:
            pass
        else:
            return self.cache_data.get(key)
