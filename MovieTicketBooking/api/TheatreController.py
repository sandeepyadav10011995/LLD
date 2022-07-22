
from providers.InMemorySeatLockProvider import InMemorySeatLockProvider
from service.BookingService import BookingService
from service.ShowService import ShowService
from service.ThreaterService import TheaterService


class BookingController:
    def __init__(self, showService: ShowService, bookingService: BookingService, theaterService: TheaterService) -> None:
        self._showService = showService
        self._bookingService = bookingService
        self._theaterService = theaterService

    def createBooking(self, userId: str, showId: str, seatIds: list[str]) -> str:
        show = self._showService.getShow(showId=showId)
        seats = [self._theaterService.getSeat(seatId=seatId) for seatId in seatIds if
                 self._theaterService.getSeat(seatId=seatId) is not None]
        return self._bookingService.createBooking(userId=userId, show=show, seats=seats).getId()
        
