from datetime import datetime

from service.MovieService import MovieService
from service.SeatAvailabilityService import SeatAvailabilityService
from service.ShowService import ShowService
from service.ThreaterService import TheaterService


class ShowController:
    def __init__(self, seatAvailabilityService: SeatAvailabilityService, showService: ShowService,
                 theaterService: TheaterService, movieService: MovieService) -> None:
        self.seatAvailabilityService = seatAvailabilityService
        self.showService = showService
        self.theaterService = theaterService
        self.movieService = movieService

    def createShow(self, movieId: str, screenId: str, startTime: datetime, durationInSeconds: int) -> str:
        screen = self.theaterService.getScreen(screenId=screenId)
        movie = self.movieService.getMovie(movieId=movieId)
        return self.showService.createShow(movie=movie, screen=screen, startTime=startTime, durationInSeconds=durationInSeconds).getId()

    def getAvailableSeats(self, showId: str) -> list[str]:
        show = self.showService.getShow(showId=showId)
        availableSeats = self.seatAvailabilityService.getAvailableSeats(show=show)
        return [seat.getId() for seat in availableSeats]

