from exception.Exception import NoFreeSlotAvailableException
from model.parking_strategy.ParkingStrategy import ParkingStrategy


class DefaultOrderParkingStrategy(ParkingStrategy):
    slotOrderedSet = None

    def __init__(self):
        self.slotOrderedSet = set()

    def addSlot(self, slotNumber: int) -> None:
        self.slotOrderedSet.add(slotNumber)

    def removeSlot(self, slotNumber: int) -> None:
        self.slotOrderedSet.remove(slotNumber)

    def getNextSlot(self) -> int:
        if len(self.slotOrderedSet) == 0:
            raise NoFreeSlotAvailableException()
        return self.slotOrderedSet[0]
