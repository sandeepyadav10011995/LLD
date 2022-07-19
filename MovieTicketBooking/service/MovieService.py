import uuid

from model.Movie import Movie


class MovieService:
    def __init__(self) -> None:
        self.movies = dict()

    def getMovie(self, movieId: str) -> Movie:
        if movieId not in self.movies:
            pass
        return self.movies.get(movieId)

    def createMovie(self, movieName: str) -> Movie:
        movieId = str(uuid.uuid4())
        movie = Movie(id=movieId, name=movieName)
        self.movies[movieId] = movie
        return movie
