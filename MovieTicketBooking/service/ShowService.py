import uuid
from datetime import datetime

from model.Movie import Movie
from model.Screen import Screen
from model.Show import Show


class ShowService:
    def __init__(self):
        self._shows = dict()

    def getShow(self, showId: str) -> Show:
        if showId not in self._shows:
            pass
        return self._shows.get(showId)

    def createShow(self, movie: Movie, screen: Screen, startTime: datetime, durationInSeconds: int) -> Show:
        if not self._checkIfShowCreationAllowed(screen, startTime, durationInSeconds):
            pass
        showId = str(uuid.uuid4())
        show = Show(id=showId, movie=movie, screen=screen, startTime=startTime, durationInSeconds=durationInSeconds)
        self._shows[showId] = show
        return show

    def getShowsForScreen(self, screen: Screen) -> list[Show]:
        allShowsForScreen = []
        for show in self._shows:
            if show.getScreen() == screen:
                allShowsForScreen.append(show)

        return allShowsForScreen

    @staticmethod
    def _checkIfShowCreationAllowed(screen, startTime, durationInSeconds) -> bool:
        # Write the Logic
        return True
