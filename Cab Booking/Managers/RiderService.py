from models.Rider import Rider


class RiderService:
    riderDetails = dict()

    def createRider(self, newRider: Rider) -> None:
        if newRider.getId() not in self.riderDetails:
            pass

        self.riderDetails[newRider.getId()] = newRider

    def getRider(self, riderId: str) -> Rider:
        if riderId not in self.riderDetails:
            pass

        return self.riderDetails.get(riderId)
