from datetime import datetime
from model.Seat import Seat
from model.Show import Show


class SeatLock:
    def __init__(self, seat: Seat, show: Show, timeOutInSeconds: int, lockTime: datetime, lockBy: str) -> None:
        self._seat = seat
        self._show = show
        self._timeOutInSeconds = timeOutInSeconds
        self._lockTime = lockTime
        self._lockBy = lockBy

    def getSeat(self):
        return self._seat

    def getShow(self):
        return self._show

    def getTimeOutInSeconds(self):
        return self._timeOutInSeconds

    def getLockTime(self):
        return self._lockTime

    def getLockBy(self):
        return self._lockBy

    def isLockExpired(self) -> bool:
        lock_instance = self._lockTime.second + self._timeOutInSeconds
        current_instance = datetime.now().second
        return lock_instance < current_instance
