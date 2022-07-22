from models.Cab import Cab
from models.Location import Location
from models.Rider import Rider
from models.Trip import Trip
from services.CabService import CabService
from services.RiderService import RiderService
from strategies.CabMatchingStrategy import CabMatchingStrategy
from strategies.PricingStrategy import PricingStrategy


class TripService:
    MAX_ALLOWED_TRIP_MATCHING_DISTANCE = 10.0
    tripDetails = dict()  # string: List[trip]

    def __init__(self, cabService: CabService, riderService: RiderService, cabMatchingStrategy: CabMatchingStrategy, pricingStrategy: PricingStrategy) -> None:
        self.cabService = cabService
        self.riderService = riderService
        self.cabMatchingStrategy = cabMatchingStrategy
        self.pricingStrategy = pricingStrategy

    def createTrip(self, rider: Rider, fromPoint: Location, toPoint: Location) -> None:
        closeByCabs = self.cabService.getCabs(fromPoint=fromPoint, toPoint=self.MAX_ALLOWED_TRIP_MATCHING_DISTANCE)
        closeByAvailableCabs = [cab for cab in closeByCabs if cab.getCurrentTrip() is None]
        selectedCab = self.cabMatchingStrategy.matchCabToRider(rider=rider, candidatesCabs=closeByAvailableCabs, fromPoint=fromPoint, toPoint=toPoint)
        if selectedCab is None:
            pass

        price = self.pricingStrategy.findPrice(fromPoint=fromPoint, toPoint=toPoint)
        newTrip = Trip(rider=rider, cab=selectedCab, price=price, fromPoint=fromPoint, toPoint=toPoint)
        if rider.getId() not in self.tripDetails:
            self.tripDetails[rider.getId()] = []
            pass

        self.tripDetails[rider.getId()].append(newTrip)
        selectedCab.setCurrentTrip(currentTrip=newTrip)

    def tripHistory(self, rider: Rider) -> list[Trip]:
        return self.tripDetails.get(rider.getId())

    @staticmethod
    def endTrip(cab: Cab) -> None:
        if cab.getCurrentTrip() is None:
            pass
        cab.getCurrentTrip().endTrip()
        cab.setCurrentTrip(currentTrip=None)
