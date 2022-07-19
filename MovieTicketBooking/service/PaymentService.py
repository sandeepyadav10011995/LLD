from model.Booking import Booking


class PaymentService:
    def __init__(self, allowedRetries: int, seatLockProvider) -> None:
        self.allowedRetries = allowedRetries
        self.seatLockProvider = seatLockProvider
        self.bookingFailures = dict()

    def processPaymentFailed(self, booking: Booking, user: str) -> None:
        if not booking.getUser() == user:
            pass
        if booking not in self.bookingFailures:
            self.bookingFailures[0] = booking

        currentFailuresCount = self.bookingFailures.get(booking)
        newFailuresCount = currentFailuresCount + 1
        self.bookingFailures[booking] = newFailuresCount
        if newFailuresCount > self.allowedRetries:
            self.seatLockProvider.unlockSeats(booking.getShow(), booking.getSeatsBooked(), booking.getUser())
