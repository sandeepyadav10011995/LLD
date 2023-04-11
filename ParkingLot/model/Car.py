

class Car:
    def __init__(self, registrationNumber: str, color: str) -> None:
        """
        Model object to represent a car.
        """
        self._color = color
        self._registrationNumber = registrationNumber

    def getColor(self) -> str:
        return self._color

    def getRegistrationNumber(self) -> str:
        return self._registrationNumber
