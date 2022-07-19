from model.Seat import Seat
from model.Show import Show
from service.BookingService import BookingService


class SeatAvailabilityService:
    def __init__(self, bookingService: BookingService, seatLockProvider) -> None:
        self.bookingService = bookingService
        self.seatLockProvider = seatLockProvider

    def getUnavailableSeats(self, show: Show) -> list[Seat]:
        unavailableSeats = self.bookingService.getBookedSeats()
        unavailableSeats.append(self.seatLockProvider.getLockedSeats(show))
        return unavailableSeats

    def getAvailableSeats(self, show: Show) -> list[Seat]:
        allSeats = show.getScreen().getSeats()
        unavailableSeats = self.getUnavailableSeats(show)
        availableSeats = allSeats
        availableSeats.remove(unavailableSeats)
        return availableSeats
