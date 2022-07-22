from models.Location import Location
from models.Rider import Rider
from models.Trip import Trip
from services.RiderService import RiderService
from services.TripsService import TripService


class RiderController:
    def __init__(self, riderService: RiderService, tripService: TripService) -> None:
        self.riderService = riderService
        self.tripService = tripService

    def registerRider(self, riderId: str, riderName: str) -> None:
        self.riderService.createRider(newRider=Rider(id=riderId, name=riderName))

    def book(self, riderId: str, sourceX: float, sourceY: float, destX: float, destY: float) -> None:
        self.tripService.createTrip(rider=self.riderService.getRider(riderId=riderId),
                                    fromPoint=Location(latitude=sourceX, longitude=sourceY),
                                    toPoint=Location(latitude=destX, longitude=destY))

    def fetchHistory(self, riderId: str) -> list[Trip]:
        trips = self.tripService.tripHistory(rider=self.riderService.getRider(riderId=riderId))
        return trips
