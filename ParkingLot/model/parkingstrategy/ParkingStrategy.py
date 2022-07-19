from abc import ABCMeta, abstractmethod


class ParkingStrategy(metaclass=ABCMeta):
    @abstractmethod
    def addSlot(self, slotNumber: int) -> None:
        pass

    @abstractmethod
    def removeSlot(self, slotNumber: int) -> None:
        pass

    @abstractmethod
    def getNextSlot(self) -> int:
        pass
