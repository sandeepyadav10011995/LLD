from models.Cab import Cab
from models.Location import Location
from services.CabService import CabService
from services.TripsService import TripService


class CabController:
    def __init__(self, cabService: CabService, tripService: TripService) -> None:
        self.cabService = cabService
        self.tripService = tripService

    def registerCab(self, cabId: str, driverName: str) -> None:
        self.cabService.createCab(Cab(id=cabId, driverName=driverName))

    def updateCabLocation(self, cabId: str, new_longitude: float, new_latitude: float) -> None:
        self.cabService.updateCabLocation(cabId=cabId, newLocation=Location(latitude=new_latitude, longitude=new_longitude))

    def updateCabAvailability(self, cabId: str, newAvailability: bool) -> None:
        self.cabService.updateCabAvailability(cabId=cabId, newAvailability=newAvailability)

    def endTrip(self, cabId: str) -> None:
        self.tripService.endTrip(self.cabService.getCab(cabId=cabId))
