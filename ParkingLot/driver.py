import args as args
import kwargs as kwargs

from OutputPrinter import OutputPrinter
from command.CommandExecutorFactory import CommandExecutorFactory
from exception.Exception import InvalidModeException
from mode.FileMode import FileMode
from mode.InteractiveMode import InteractiveMode
from service.ParkingLotService import ParkingLotService


class Driver:
    def __init__(self, args=None) -> None:
        if args is None:
            args = []
        self.outputPrinter: OutputPrinter = OutputPrinter()
        self.parkingLotService: ParkingLotService = ParkingLotService()
        self.commandExecutorFactory: CommandExecutorFactory = CommandExecutorFactory(parkingLotService=self.parkingLotService)

        if self._isInteractiveMode(args=args):
            InteractiveMode(commandExecutorFactory=self.commandExecutorFactory,
                            outputPrinter=self.outputPrinter).process()
        elif self._isFileMode(args=args):
            FileMode(commandExecutorFactory=self.commandExecutorFactory,
                     outputPrinter=self.outputPrinter, fileName=args[0]).process()
        else:
            raise InvalidModeException()

    @staticmethod
    def _isFileMode(args: list[str]) -> bool:
        return len(args) == 1

    @staticmethod
    def _isInteractiveMode(args: list[str]) -> bool:
        return not args


def main():
    m = Driver(args=["file.txt"])
    m

if __name__ == "__main__":
    main()
