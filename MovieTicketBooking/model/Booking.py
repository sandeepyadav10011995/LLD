from model.BokkingStatus import BookingStatus
from model.Seat import Seat
from model.Show import Show


class Booking:
    def __init__(self, id: str, show: Show, seatsBooked: list[Seat], user: str, bookingStatus=BookingStatus.Confirmed) -> None:
        self.id = id
        self.show = show
        self.seatsBooked = seatsBooked
        self.user = user
        self.bookingStatus = bookingStatus

    def getId(self):
        return self.id

    def getShow(self):
        return self.show

    def getSeatsBooked(self):
        return self.seatsBooked

    def getUser(self):
        return self.user

    def getBookingStatus(self):
        return self.bookingStatus

    def isConfirmed(self) -> bool:
        return self.bookingStatus == BookingStatus.Confirmed

    def confirmBooking(self) -> None:
        if self.bookingStatus != BookingStatus.Created:
            raise InvalidStateException()
        self.bookingStatus = BookingStatus.Confirmed

    def expireBooking(self):
        if self.bookingStatus != BookingStatus.Created:
            raise InvalidStateException()
        self.bookingStatus = BookingStatus.Expired
