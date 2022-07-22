from exception.Exception import InvalidStateException
from model.BokkingStatus import BookingStatus
from model.Seat import Seat
from model.Show import Show


class Booking:
    def __init__(self, id: str, show: Show, seatsBooked: list[Seat], user: str, bookingStatus=BookingStatus.Confirmed) -> None:
        self._id = id
        self._show = show
        self._seatsBooked = seatsBooked
        self._user = user
        self._bookingStatus = bookingStatus

    def getId(self):
        return self._id

    def getShow(self):
        return self._show

    def getSeatsBooked(self):
        return self._seatsBooked

    def getUser(self):
        return self._user

    def getBookingStatus(self):
        return self._bookingStatus

    def isConfirmed(self) -> bool:
        return self._bookingStatus == BookingStatus.Confirmed

    def confirmBooking(self) -> None:
        if self._bookingStatus != BookingStatus.Created:
            raise InvalidStateException()
        self._bookingStatus = BookingStatus.Confirmed

    def expireBooking(self):
        if self._bookingStatus != BookingStatus.Created:
            raise InvalidStateException()
        self._bookingStatus = BookingStatus.Expired
