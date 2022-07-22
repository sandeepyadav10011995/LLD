from service.MovieService import MovieService


class from service.MovieService import MovieService


class MovieController:
    def __init__(self, movieService: MovieService):
        self._movieService = movieService

    def createMovie(self, movieName: str) -> str:
        return self._movieService.createMovie(movieName=movieName).getId()
:
    def __init__(self, movieService: MovieService):
        self._movieService = movieService

    def createMovie(self, movieName: str) -> str:
        return self._movieService.createMovie(movieName=movieName).getId()
