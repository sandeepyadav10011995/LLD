from enum import Enum

from models.Cab import Cab
from models.Location import Location
from models.Rider import Rider


class TripStatus(Enum):
    IN_PROGRESS = 1,
    FINISHED = 2


class Trip:
    def __init__(self, rider: Rider, cab: Cab, price: float, fromPoint: Location, toPoint: Location) -> None:
        self.rider = rider
        self.cab = cab
        self.price = price
        self.fromPoint = fromPoint
        self.toPoint = toPoint
        self.status = TripStatus.IN_PROGRESS

    def endTrip(self) -> None:
        self.status = TripStatus.FINISHED
