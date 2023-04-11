from exception.Exception import ParkingLotException
from model.Car import Car
from model.ParkingLot import ParkingLot
from model.Slot import Slot
from model.parkingStrategy.ParkingStrategy import ParkingStrategy


class ParkingLotService:
    _parkingLot: ParkingLot = None
    _parkingStrategy: ParkingStrategy = None

    def _validateParkingLotExists(self) -> None:
        if self._parkingLot is None:
            raise ParkingLotException("Parking lot does not exists to park.")

    def park(self, car: Car) -> int:
        self._validateParkingLotExists()
        nextFreeSlot = self._parkingStrategy.getNextSlot()
        self._parkingLot.park(car=car, slotNumber=nextFreeSlot)
        self._parkingStrategy.removeSlot(nextFreeSlot)
        return nextFreeSlot

    def makeSlotFree(self, slotNumber: int) -> None:
        self._validateParkingLotExists()
        self._parkingLot.makeSlotFree(slotNumber=slotNumber)
        self._parkingStrategy.addSlot(slotNumber=slotNumber)

    def getOccupiedSlots(self) -> list[Slot]:
        self._validateParkingLotExists()
        occupiedSlotsList = list()
        allSlots = self._parkingLot.getSlots()
        for slotNumber in range(1, self._parkingLot.getCapacity()):
            if slotNumber in allSlots:
                slot: Slot = allSlots.get(slotNumber)
                if not slot.isSlotFree():
                    occupiedSlotsList.append(slot)

        return occupiedSlotsList

    def getSlotsForColor(self, color: str) -> list[Slot]:
        occupiedSlotList = self.getOccupiedSlots()
        return [slot for slot in occupiedSlotList if slot.getParkedCar().getColor() == color]

    def createParkingLot(self, parkingLot: ParkingLot, parkingStrategy: ParkingStrategy) -> None:
        if self._parkingLot is not None:
            raise ParkingLotException("Parking lot already exists.")
        self._parkingLot = parkingLot
        self._parkingStrategy = parkingStrategy
        for slotNumber in range(1, self._parkingLot.getCapacity()+1):
            self._parkingStrategy.addSlot(slotNumber=slotNumber)