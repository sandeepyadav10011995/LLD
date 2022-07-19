import uuid

from model.Screen import Screen
from model.Seat import Seat
from model.Theater import Theater


class TheaterService:
    def __init__(self, theaters: dict, screens: dict, seats: dict):
        self.theaters = theaters
        self.screens = screens
        self.seats = seats

    def getTheater(self, theaterId: str) -> Theater:
        if theaterId not in self.theaters:
            pass
        return self.theaters.get(theaterId)

    def getScreen(self, screenId: str) -> Screen:
        if screenId not in self.screens:
            pass
        return self.seats.get(screenId)

    def getSeat(self, seatId: str) -> Seat:
        if seatId not in self.seats:
            pass
        return self.seats.get(seatId)

    def createTheater(self, theaterName: str) -> Theater:
        theaterId = str(uuid.uuid4())
        theater = Theater(id=theaterId, name=theaterName)
        self.theaters[theaterId] = theater
        return theater

    def createScreen(self, screenName: str, theater: Theater) -> Screen:
        screenId = str(uuid.uuid4())
        screen = Screen(id=screenId, name=screenName, theater=theater)
        self.screens[screenId] = screen
        return screen

    def createScreenInTheater(self, screenName: str, theater: Theater) -> Screen:
        screen = self.createScreen(screenName=screenName, theater=theater)
        theater.addScreens(screen=screen)
        return screen

    def createSeatInScreen(self, rowNo: int, seatNo: int, screen: Screen) -> Seat:
        seatId = str(uuid.uuid4())
        seat = Seat(id=seatId, rowNo=rowNo, seatNo=seatNo)
        self.seats[seatId] = seat
        screen.addSeat(seat=seat)
        return seat
