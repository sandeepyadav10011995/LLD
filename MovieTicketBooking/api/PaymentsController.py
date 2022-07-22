from service.BookingService import BookingService
from service.PaymentService import PaymentService


class PaymentsController:
    def __init__(self, paymentService: PaymentService, bookingService: BookingService):
        self._paymentService = paymentService
        self._bookingService = bookingService

    def paymentFailed(self, bookingId: str, user: str) -> None:
        self._paymentService.processPaymentFailed(booking=self._bookingService.getBookings(bookingId=bookingId),
                                                  user=user)

    def paymentSuccess(self, bookingId: str, user: str) -> None:
        self._bookingService.confirmBooking(booking=self._bookingService.getBookings(bookingId=bookingId), user=user)
