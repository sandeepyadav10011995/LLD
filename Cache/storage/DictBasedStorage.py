from cache.exceptions.exception import StorageFullException, NotFoundException
from cache.storage.Storage import Storage


class DictBasedStorage(Storage):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.storage = dict()

    def isStorageFull(self):
        return len(self.storage) == self.capacity

    def add(self, key, value):
        if self.isStorageFull():
            raise StorageFullException
        self.storage[key] = value

    def remove(self, key):
        if key not in self.storage:
            raise NotFoundException
        self.storage.pop(key)

    def get(self, key):
        if key not in self.storage:
            raise NotFoundException
        return self.storage.get(key)
