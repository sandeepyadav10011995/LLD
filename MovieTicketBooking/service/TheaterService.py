import uuid

from model.Screen import Screen
from model.Seat import Seat
from model.Theater import Theater


class TheaterService:
    def __init__(self):
        self._theaters = dict()
        self._screens = dict()
        self._seats = dict()

    def getTheater(self, theaterId: str) -> Theater:
        if theaterId not in self._theaters:
            pass
        return self._theaters.get(theaterId)

    def getScreen(self, screenId: str) -> Screen:
        if screenId not in self._screens:
            pass
        return self._seats.get(screenId)

    def getSeat(self, seatId: str) -> Seat:
        if seatId not in self._seats:
            pass
        return self._seats.get(seatId)

    # Create the theater
    def createTheater(self, theaterName: str) -> Theater:
        theaterId = str(uuid.uuid4())
        theater = Theater(id=theaterId, name=theaterName)
        self._theaters[theaterId] = theater
        return theater

    # Create the screen
    def _createScreen(self, screenName: str, theater: Theater) -> Screen:
        screenId = str(uuid.uuid4())
        screen = Screen(id=screenId, name=screenName, theater=theater)
        self._screens[screenId] = screen
        return screen

    # Create the screen for a theater
    def createScreenInTheater(self, screenName: str, theater: Theater) -> Screen:
        screen = self._createScreen(screenName=screenName, theater=theater)
        theater.addScreens(screen=screen)
        return screen

    def createSeatInScreen(self, rowNo: int, seatNo: int, screen: Screen) -> Seat:
        seatId = str(uuid.uuid4())
        seat = Seat(id=seatId, rowNo=rowNo, seatNo=seatNo)
        self._seats[seatId] = seat
        screen.addSeat(seat=seat)
        return seat
