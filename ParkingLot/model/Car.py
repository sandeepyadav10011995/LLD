

class Car:
    def __init__(self, registrationNumber: str, color: str) -> None:
        self.__color = color
        self.__registrationNumber = registrationNumber

    def getRegistrationNumber(self) -> str:
        return self.__registrationNumber

    def getColor(self) -> str:
        return self.__color
