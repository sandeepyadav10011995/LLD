from exception.Exception import InvalidCommandException


class Command:
    SPACE: str = " "
    _params: list[str] = None
    _commandName: str = None

    def __init__(self, inputLine: str) -> None:
        tokenList = inputLine.split(self.SPACE)
        if not tokenList:
            raise InvalidCommandException()

        self._commandName = tokenList[0].lower()
        tokenList.pop(0)
        self._params = tokenList

    def getCommandName(self) -> str:
        return self._commandName

    def getParams(self) -> list[str]:
        return self._params