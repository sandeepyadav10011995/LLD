from exception.Exception import ParkingLotException
from model.Car import Car
from model.ParkingLot import ParkingLot
from model.Slot import Slot
from model.parking_strategy.ParkingStrategy import ParkingStrategy


class ParkingLotService:
    __parkingLot = None
    __parkingStrategy = None

    def __validateParkingLotExists(self) -> None:
        if self.__parkingLot is None:
            raise ParkingLotException("Parking lot does not exists to park.")

    def park(self, car: Car) -> int:
        self.__validateParkingLotExists()
        nextFreeSlot = self.__parkingStrategy.getNextSlot()
        self.__parkingLot.park(car=car, slotNumber=nextFreeSlot)
        self.__parkingStrategy.removeSlot(nextFreeSlot)
        return nextFreeSlot

    def makeSlotFree(self, slotNumber: int) -> None:
        self.__validateParkingLotExists()
        self.__parkingLot.makeSlotFree(slotNumber=slotNumber)
        self.__parkingStrategy.addSlot(slotNumber=slotNumber)

    def getOccupiedSlots(self) -> list[Slot]:
        self.__validateParkingLotExists()
        occupiedSlotsList = list()
        allSlots = self.__parkingLot.getSlots()
        for slotNumber in range(1, self.__parkingLot.getCapacity()):
            if slotNumber in allSlots:
                slot: Slot = allSlots.get(slotNumber)
                if not slot.isSlotFree():
                    occupiedSlotsList.append(slot)

        return occupiedSlotsList

    def getSlotsForColor(self, color: str) -> list[Slot]:
        occupiedSlotList = self.getOccupiedSlots()
        return [slot for slot in occupiedSlotList if slot.getParkedCar().getColor() == color]

    def createParkingLot(self, parkingLot: ParkingLot, parkingStrategy: ParkingStrategy) -> None:
        if self.__parkingLot is not None:
            raise ParkingLotException("Parking lot already exists.")
        self.__parkingLot = parkingLot
        self.__parkingStrategy = parkingStrategy
        for slotNumber in range(1, self.__parkingLot.getCapacity()):
            self.__parkingStrategy.addSlot(slotNumber=slotNumber)
