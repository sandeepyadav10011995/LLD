from datetime import datetime

from model.Movie import Movie
from model.Screen import Screen


class Show:
    def __init__(self, id, movie: Movie, screen: Screen, startTime: datetime, durationInSeconds: int) -> None:
        self._id = id
        self._movie = movie
        self._screen = screen
        self._startTime = startTime
        self._durationInSeconds = durationInSeconds

    def getId(self):
        return self._id

    def getMovie(self):
        return self._movie

    def getScreen(self):
        return self._screen

    def getStartTime(self):
        return self._startTime

    def getDurationInSeconds(self):
        return self._durationInSeconds
