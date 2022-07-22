from models.Location import Location
from strategies.PricingStrategy import PricingStrategy


class DefaultPricingStrategy(PricingStrategy):
    PER_KM_RATE = 10.0

    def findPrice(self, fromPoint: Location, toPoint: Location) -> float:
        return fromPoint.distance(location2=toPoint) * self.PER_KM_RATE
