from exception.Exception import NoFreeSlotAvailableException
from model.parkingStrategy.ParkingStrategy import ParkingStrategy


class NaturalOrderingParkingStrategy(ParkingStrategy):
    slotOrderedSet = None

    def __init__(self):
        self.slotOrderedSet = set()

    def addSlot(self, slotNumber: int) -> None:
        self.slotOrderedSet.add(slotNumber)

    def removeSlot(self, slotNumber: int) -> None:
        self.slotOrderedSet.remove(slotNumber)

    def getNextSlot(self) -> int:
        if len(self.slotOrderedSet) == 0:
            raise NoFreeSlotAvailableException(errorMessage="")
        return list(self.slotOrderedSet)[0]