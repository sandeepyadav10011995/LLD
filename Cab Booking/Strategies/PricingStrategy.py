from abc import ABCMeta, abstractmethod

from models.Location import Location


class PricingStrategy(metaclass=ABCMeta):
    @abstractmethod
    def findPrice(self, fromPoint: Location, toPoint: Location) -> float:
        pass
