from model import Car


class Slot:
    def __init__(self, parkedCar: Car = None, slotNumber: int = None) -> None:
        self.__parkedCar = parkedCar
        self.__slotNumber = slotNumber

    def getSlotNumber(self) -> int:
        return self.__slotNumber

    def getParkedCar(self) -> Car:
        return self.__parkedCar

    # Other Methods

    def isSlotFree(self) -> bool:
        return self.__parkedCar is None

    def assignCar(self, car: Car) -> None:
        self.__parkedCar = car

    def unassignCar(self) -> None:
        self.__parkedCar = None
