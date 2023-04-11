from abc import ABCMeta, abstractmethod


class ParkingStrategy(metaclass=ABCMeta):
    @abstractmethod
    def addSlot(self, slotNumber: int) -> None:
        """
        :param slotNumber: Slot number to be added.
        :return: None
        """
        raise NotImplemented("Please implement this method!")

    @abstractmethod
    def removeSlot(self, slotNumber: int) -> None:
        """
        :param slotNumber: Slot number to be removed.
        :return: None
        """
        raise NotImplemented("Please implement this method!")
    @abstractmethod
    def getNextSlot(self) -> int:
        """
        :return: Next free slot number.
        """
        raise NotImplemented("Please implement this method!")