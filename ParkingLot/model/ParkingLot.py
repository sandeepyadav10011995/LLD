from exception.Exception import ParkingLotException, InvalidSlotException, SlotAlreadyOccupiedException
from model import Car
from model.Slot import Slot


class ParkingLot:
    MAX_CAPACITY = 10000

    def __init__(self, capacity: int) -> None:
        if capacity > self.MAX_CAPACITY or capacity <= 0:
            raise ParkingLotException("Invalid capacity given for parking lot.")

        self.__capacity = capacity
        self.__slots = dict()

    def getCapacity(self) -> int:
        return self.__capacity

    def getSlots(self) -> dict:
        return self.__slots

    def __getSlot(self, slotNumber: int) -> Slot:
        if slotNumber > self.getCapacity() or slotNumber <= 0:
            raise InvalidSlotException

        allSlots = self.getSlots()
        if slotNumber not in allSlots:
            allSlots[slotNumber] = Slot(slotNumber=slotNumber)
        return allSlots.get(slotNumber)

    def park(self, car: Car, slotNumber: int) -> Slot:
        slot: Slot = self.__getSlot(slotNumber=slotNumber)
        if not slot.isSlotFree():
            raise SlotAlreadyOccupiedException
        slot.assignCar(car=car)
        return slot

    def makeSlotFree(self, slotNumber: int) -> Slot:
        slot: Slot = self.__getSlot(slotNumber=slotNumber)
        slot.unassignCar()
        return slot
