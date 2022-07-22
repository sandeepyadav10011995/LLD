from models.Cab import Cab
from models.Location import Location
from models.Rider import Rider
from strategies.CabMatchingStrategy import CabMatchingStrategy


class DefaultCabMatchingStrategy(CabMatchingStrategy):
    def matchCabToRider(self, rider: Rider, candidatesCabs: list[Cab], fromPoint: Location, toPoint: Location) -> Cab:
        if len(candidatesCabs) == 0:
            return None
        return candidatesCabs[0]
