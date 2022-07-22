from exceptions.exception import StorageFullException, NotFoundException
from storage.Storage import Storage
from policies.EvictionPolicy import EvictionPolicy


class Cache:
    def __init__(self, evictionPolicy: EvictionPolicy, storage: Storage):
        self.evictionPolicy = evictionPolicy
        self.storage = storage

    def put(self, key, value):
        try:
            self.storage.add(key, value)
            self.evictionPolicy.keyAccessed(key)
        except StorageFullException:
            keyToRemove = self.evictionPolicy.evictKey()
            if keyToRemove is None:
                raise RuntimeError
            self.storage.remove(keyToRemove)
            self.put(key, value)

    def get(self, key):
        try:
            value = self.storage.get(key)
            self.evictionPolicy.keyAccessed(key)
            return value
        except NotFoundException:
            return None
