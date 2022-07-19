from model.Screen import Screen


class Theater:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name
        self.screens = list()

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getScreens(self):
        return self.screens

    def addScreens(self, screen: Screen):
        self.screens.append(screen)
