from abc import ABCMeta, abstractmethod

from model.Seat import Seat
from model.Show import Show


class SeatLockProvider(metaclass=ABCMeta):
    @abstractmethod
    def lockSeats(self, show: Show, seats: list[Seat], user: str):
        pass

    @abstractmethod
    def unlockSeats(self, show: Show, seats: list[Seat], user: str):
        pass

    @abstractmethod
    def validateLock(self, show: Show, seat: Seat, user: str):
        pass

    @abstractmethod
    def getLockedSeat(self, show: Show):
        pass
