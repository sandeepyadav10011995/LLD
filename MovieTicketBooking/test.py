import unittest

from api.BookingController import BookingController
from api.MovieController import MovieController
from api.PaymentsController import PaymentsController
from api.ShowController import ShowController
from api.TheaterController import TheaterController
from providers.InMemorySeatLockProvider import InMemorySeatLockProvider
from service.BookingService import BookingService
from service.MovieService import MovieService
from service.PaymentService import PaymentService
from service.SeatAvailabilityService import SeatAvailabilityService
from service.ShowService import ShowService
from service.ThreaterService import TheaterService


class BaseTest(unittest.TestCase):
    bookingController = None
    showController = None
    theaterController = None
    movieController = None
    paymentsController = None

    def setupControllers(self, lockTimeout: int, allowedRetries: int) -> None:
        seatLockProvider = InMemorySeatLockProvider(lockTimeout=lockTimeout)
        bookingService = BookingService(seatLockProvider=seatLockProvider)
        movieService = MovieService()
        showService = ShowService()
        theaterService = TheaterService()
        seatAvailabilityService = SeatAvailabilityService(
            bookingService=bookingService, seatLockProvider=seatLockProvider)
        paymentsService = PaymentService(allowedRetries=allowedRetries, seatLockProvider=seatLockProvider)

        # Set up all the controllers
        self.bookingController = BookingController(showService=showService, bookingService=bookingService,
                                                   theaterService=theaterService)
        self.showController = ShowController(seatAvailabilityService=seatAvailabilityService, showService=showService,
                                             theaterService=theaterService, movieService=movieService)
        self.theaterController = TheaterController(theaterService=theaterService)
        self.movieController = MovieController(movieService=movieService)
        self.paymentsController = PaymentsController(paymentService=paymentsService, bookingService=bookingService)

    def validateSeatsList(self, seatsList: list[str], allSeatsInScreen: list[str], excludedSeats: list[str]) -> None:
        for includedSeat in allSeatsInScreen:
            if includedSeat not in excludedSeats:
                self.assertTrue(includedSeat in seatsList)

        for excludedSeat in excludedSeats:
            self.assertFalse(excludedSeat in seatsList)

    @staticmethod
    def createSeats(theaterController: TheaterController, screen: str, numRows: int, numSeatsInRow: int) -> list[str]:
        seats = []
        for row in range(numRows):
            for seatNo in range(numSeatsInRow):
                seat = theaterController.createSeatInScreen(rowNo=row, seatNo=seatNo, screenId=screen)
                seats.append(seat)
        return seats

    def setupScreen(self):
        theater = self.theaterController.createTheater(theaterName="Theater 1")
        return self.theaterController.createScreenInTheater(screenName="Screen 1", theater=theater)
