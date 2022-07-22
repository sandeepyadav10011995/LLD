from abc import ABCMeta, abstractmethod

from models.Cab import Cab
from models.Location import Location
from models.Rider import Rider


class CabMatchingStrategy(metaclass=ABCMeta):
    @abstractmethod
    def matchCabToRider(self, rider: Rider, candidatesCabs: list[Cab], fromPoint: Location, toPoint: Location) -> Cab:
        pass
