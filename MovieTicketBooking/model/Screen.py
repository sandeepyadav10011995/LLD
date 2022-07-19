from model.Theater import Theater


class Screen:
    def __init__(self, id: str, name: str, theater: Theater) -> None:
        self.id = id
        self.name = name
        self.theater = theater
        self.seats = list()

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getTheater(self):
        return self.theater

    def getSeats(self):
        return self.seats

    def addSeat(self, seat: Seat) -> None:
        self.seats.append(seat)
