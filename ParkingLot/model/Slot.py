from model import Car


class Slot:
    def __init__(self, parkedCar: Car = None, slotNumber: int = None) -> None:
        self._parkedCar = parkedCar
        self._slotNumber = slotNumber

    def getParkedCar(self) -> Car:
        return self._parkedCar

    def getSlotNumber(self) -> int:
        return self._slotNumber

    # Other Methods

    def isSlotFree(self) -> bool:
        return self._parkedCar is None

    def assignCar(self, car: Car) -> None:
        self._parkedCar = car

    def unAssignCar(self) -> None:
        self._parkedCar = None