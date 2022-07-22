from model.Booking import Booking
from providers.SeatLockProvider import SeatLockProvider


class PaymentService:
    def __init__(self, allowedRetries: int, seatLockProvider: SeatLockProvider) -> None:
        self._allowedRetries = allowedRetries
        self._seatLockProvider = seatLockProvider
        self._bookingFailures = dict()

    def processPaymentFailed(self, booking: Booking, user: str) -> None:
        if not booking.getUser() == user:
            pass
        if booking not in self._bookingFailures:
            self._bookingFailures[booking] = 0

        currentFailuresCount = self._bookingFailures.get(booking)
        newFailuresCount = currentFailuresCount + 1
        self._bookingFailures[booking] = newFailuresCount
        if newFailuresCount > self._allowedRetries:
            self._seatLockProvider.unlockSeats(show=booking.getShow(), seats=booking.getSeatsBooked(), user=booking.getUser())
