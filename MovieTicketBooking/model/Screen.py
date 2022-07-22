from model.Seat import Seat
from model.Theater import Theater


class Screen:
    def __init__(self, id: str, name: str, theater: Theater) -> None:
        self._id = id
        self._name = name
        self._theater = theater
        self._seats = list()

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getTheater(self):
        return self._theater

    def getSeats(self):
        return self._seats

    def addSeat(self, seat: Seat) -> None:
        self._seats.append(seat)
