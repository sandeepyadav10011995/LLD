from abc import ABCMeta, abstractmethod


class EvictionPolicy(metaclass=ABCMeta):
    @abstractmethod
    def keyAccessed(self, key):
        pass

    @abstractmethod
    def evictKey(self, key):
        pass
