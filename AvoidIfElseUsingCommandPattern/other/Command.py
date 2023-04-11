

class Command:
    def __init__(self, name: str, params: list[str]):
        self.name: str = name
        self.params: list[str] = params

    def getName(self):
        return self.name

    def getParams(self):
        return self.params
