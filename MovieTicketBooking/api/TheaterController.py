from service.ThreaterService import TheaterService


class TheaterController:
    def __init__(self, theaterService: TheaterService):
        self.theaterService = theaterService

    def createTheater(self, theaterName: str) -> str:
        return self.theaterService.createTheater(theaterName=theaterName).getId()

    def createScreenInTheater(self, screenName: str, theaterId: str) -> str:
        theater = self.theaterService.getTheater(theaterId=theaterId)
        return self.theaterService.createScreenInTheater(screenName=screenName, theater=theater).getId()

    def createSeatInScreen(self, rowNo: int, seatNo: int, screenId: str) -> str:
        screen = self.theaterService.getScreen(screenId=screenId)
        return self.theaterService.createSeatInScreen(rowNo=rowNo, seatNo=seatNo, screen=screen).getId()
