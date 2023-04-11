from exception.Exception import ParkingLotException, InvalidSlotException, SlotAlreadyOccupiedException
from model.Car import Car
from model.Slot import Slot


class ParkingLot:
    MAX_CAPACITY: int = 10000

    def __init__(self, capacity: int) -> None:
        if capacity > self.MAX_CAPACITY or capacity <= 0:
            raise ParkingLotException("Invalid capacity given for parking lot.")

        self._capacity = capacity
        self._slots = {}

    def getCapacity(self) -> int:
        return self._capacity

    def getSlots(self) -> dict:
        return self._slots

    def _getSlot(self, slotNumber: int) -> Slot:
        if slotNumber > self.getCapacity() or slotNumber <= 0:
            raise InvalidSlotException()

        allSlots = self.getSlots()
        if slotNumber not in allSlots:
            allSlots[slotNumber] = Slot(slotNumber=slotNumber)
        return allSlots.get(slotNumber)

    def park(self, car: Car, slotNumber: int) -> Slot:
        slot: Slot = self._getSlot(slotNumber=slotNumber)
        if not slot.isSlotFree():
            raise SlotAlreadyOccupiedException()
        slot.assignCar(car=car)
        return slot

    def makeSlotFree(self, slotNumber: int) -> Slot:
        slot: Slot = self._getSlot(slotNumber=slotNumber)
        slot.unAssignCar()
        return slot