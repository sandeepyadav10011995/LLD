from abc import ABCMeta, abstractmethod


class Storage(metaclass=ABCMeta):
    @abstractmethod
    def add(self, key, value):
        pass

    @abstractmethod
    def remove(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass
