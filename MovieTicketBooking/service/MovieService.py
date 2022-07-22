import uuid

from model.Movie import Movie


class MovieService:
    def __init__(self) -> None:
        self._movies = dict()

    def getMovie(self, movieId: str) -> Movie:
        if movieId not in self._movies:
            pass
        return self._movies.get(movieId)

    def createMovie(self, movieName: str) -> Movie:
        movieId = str(uuid.uuid4())
        movie = Movie(id=movieId, name=movieName)
        self._movies[movieId] = movie
        return movie
