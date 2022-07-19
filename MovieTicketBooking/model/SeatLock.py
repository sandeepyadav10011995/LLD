from datetime import datetime
from model.Seat import Seat
from model.Show import Show


class SeatLock:
    def __init__(self, seat: Seat, show: Show, timeOutInSeconds: int, lockTime: datetime, lockBy: str) -> None:
        self.seat = seat
        self.show = show
        self.timeOutInSeconds = timeOutInSeconds
        self.lockTime = lockTime
        self.lockBy = lockBy

    def getSeat(self):
        return self.seat

    def getShow(self):
        return self.show

    def getTimeOutInSeconds(self):
        return self.timeOutInSeconds

    def getLockTime(self):
        return self.lockTime

    def getLockBy(self):
        return self.lockBy

    def isLockExpired(self) -> bool:
        lock_instance = self.lockTime.time() + self.timeOutInSeconds
        current_instance = datetime.now()
        return lock_instance < current_instance
