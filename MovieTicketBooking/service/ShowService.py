import uuid
from datetime import datetime

from model.Movie import Movie
from model.Screen import Screen
from model.Show import Show


class ShowService:
    def __init__(self):
        self.shows = dict()

    def getShow(self, showId: str) -> Show:
        if showId not in self.shows:
            pass
        return self.shows.get(showId)

    def createShow(self, movie: Movie, screen: Screen, startTime: datetime, durationInSeconds: int) -> Show:
        if not self.checkIfShowCreationAllowed(screen, startTime, durationInSeconds):
            pass
        showId = str(uuid.uuid4())
        show = Show(id=showId, movie=movie, screen=screen, startTime=startTime, durationInSeconds=durationInSeconds)
        self.shows[showId] = show
        return show

    def getShowsForScreen(self, screen: Screen) -> list[Show]:
        allShowsForScreen = []
        for show in self.shows:
            if show.getScreen() == screen:
                allShowsForScreen.append(show)

        return allShowsForScreen

    @staticmethod
    def checkIfShowCreationAllowed(screen, startTime, durationInSeconds) -> bool:
        # Write the Logic
        return True
