from model.Seat import Seat
from model.Show import Show
from providers.SeatLockProvider import SeatLockProvider
from service.BookingService import BookingService


class SeatAvailabilityService:
    def __init__(self, bookingService: BookingService, seatLockProvider: SeatLockProvider) -> None:
        self._bookingService = bookingService
        self._seatLockProvider = seatLockProvider

    def getUnavailableSeats(self, show: Show) -> list[Seat]:
        unavailableSeats = self._bookingService.getBookedSeats(show=show)
        unavailableSeats.extend(self._seatLockProvider.getLockedSeats(show=show))
        return unavailableSeats

    def getAvailableSeats(self, show: Show) -> list[Seat]:
        allSeats = show.getScreen().getSeats()
        unavailableSeats = self.getUnavailableSeats(show)
        availableSeats = allSeats
        availableSeats.remove(unavailableSeats)
        return availableSeats
