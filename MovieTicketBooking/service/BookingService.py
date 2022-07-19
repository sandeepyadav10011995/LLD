import uuid

from model.BokkingStatus import BookingStatus
from model.Booking import Booking
from model.Seat import Seat
from model.Show import Show


class BookingService:
    def __init__(self, seatLockProvider):
        self.seatLockProvider = seatLockProvider
        self.showBookings = dict()

    def getBookings(self, bookingId: str) -> Booking:
        if bookingId not in self.showBookings:
            pass
        return self.showBookings.get(bookingId)

    def getAllBookings(self, show) -> list[Booking]:
        allBookingsForShow = []
        for booking in self.showBookings:
            if booking.getShow() == show:
                allBookingsForShow.append(booking)

        return allBookingsForShow

    def createBooking(self, userId: str, show: Show, seats: list[Seat]) -> Booking:
        if self.isAnySeatAlreadyBooked(show, seats):
            pass
        self.seatLockProvider.lockSeats(show, seats, userId)
        bookingId = str(uuid.uuid4())
        newBooking = Booking(id=bookingId, show=show, seatsBooked=seats, user=userId)
        self.showBookings[bookingId] = newBooking
        return newBooking

    def getBookedSeats(self, show: Show) -> list[Seat]:
        allBookings = self.getAllBookings(show)
        return [booking.getSeatsBooked() for booking in allBookings if booking.bookingStatus == BookingStatus.Confirmed]

    def confirmBooking(self, booking: Booking, user: str) -> None:
        if not booking.getUser() == user:
            pass
        for seat in booking.getSeatsBooked():
            if not self.seatLockProvider.validateLock(booking.getShow(), seat, user):
                pass
            booking.confirmBooking()

    def isAnySeatAlreadyBooked(self, show: Show, seats: list[Seat]) -> bool:
        bookedSeats = self.getBookedSeats(show)
        for seat in seats:
            if seat in bookedSeats:
                return True
        return False


















