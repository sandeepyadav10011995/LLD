from cache.Cache import Cache
from cache.policies.LRUEvictionPolicy import LRUEvictionPolicy
from cache.storage.DictBasedStorage import DictBasedStorage


class CacheFactory:
    @staticmethod
    def defaultCache(capacity: int) -> Cache:
        return Cache(evictionPolicy=LRUEvictionPolicy(), storage=DictBasedStorage(capacity=capacity))
