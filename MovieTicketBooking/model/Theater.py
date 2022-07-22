from model import Screen


class Theater:
    def __init__(self, id: str, name: str) -> None:
        self._id = id
        self._name = name
        self._screens = list()

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getScreens(self):
        return self._screens

    def addScreens(self, screen: Screen):
        self._screens.append(screen)
