

class Movie:
    def __init__(self, id: str, name: str) -> None:
        self._id = id
        self._name = name
        # Other Metadata

    def getId(self):
        return self._id

    def getName(self):
        return self._name
    
