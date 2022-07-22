from datetime import datetime

from model.Seat import Seat
from model.SeatLock import SeatLock
from model.Show import Show
from providers.SeatLockProvider import SeatLockProvider


class InMemorySeatLockProvider(SeatLockProvider):
    def __init__(self, lockTimeout: int) -> None:
        self.lockTimeout = lockTimeout
        self.locks = dict()

    def lockSeats(self, show: Show, seats: list[Seat], user: str) -> None:
        for seat in seats:
            if self.isSeatLocked(show, seat):
                pass

        for seat in seats:
            self.lockSeat(show, seat, user, self.lockTimeout)

    def unlockSeats(self, show: Show, seats: list[Seat], user: str) -> None:
        for seat in seats:
            if self.validateLock(show, seat, user):
                self.unlockSeat(show, seat)

    def validateLock(self, show: Show, seat: Seat, user: str) -> bool:
        return self.isSeatLocked(show, seat) and self.locks.get(show).get(seat).getLockBy() == user

    def getLockedSeats(self, show: Show) -> list[Seat]:
        if show not in self.locks:
            pass

        lockedSeats = []
        for seat in self.locks.get(show).key():
            if self.isSeatLocked(show, seat):
                lockedSeats.append(seat)

        return lockedSeats

    def unlockSeat(self, show: Show, seat: Seat) -> None:
        if show not in self.locks:
            return
        self.locks.get(show).remove(seat)

    def lockSeat(self, show: Show, seat: Seat, user: str, timeOutInSeconds: int) -> None:
        if show not in self.locks:
            self.locks[show] = {}
        seatLock = SeatLock(seat=seat, show=show, timeOutInSeconds=timeOutInSeconds, lockTime=datetime.now(), lockBy=user)
        self.locks[show][seat] = seatLock

    def isSeatLocked(self, show: Show, seat: Seat) -> bool:
        return self.locks.get(show) and self.locks.get(show).get(seat).isLockExpired()
