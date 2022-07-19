from exception.Exception import InvalidCommandException


class Command:
    SPACE = " "
    __params = None
    __commandName = None

    def __init__(self, inputLine: str) -> None:
        tokenList = inputLine.split(self.SPACE)
        if len(tokenList) == 0:
            raise InvalidCommandException()

        self.__commandName = tokenList[0].lower()
        tokenList.pop(0)
        self.__params = tokenList

    def getCommandName(self) -> str:
        var = self.__commandName
        return var

    def getParams(self) -> list[str]:
        return self.__params
