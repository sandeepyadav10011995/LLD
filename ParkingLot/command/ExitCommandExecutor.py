from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class ExitCommandExecutor(CommandExecutor):
    COMMAND_NAME = "exit"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        params = command.getParams()
        return len(params) == 0

    def execute(self, command: Command) -> None:
        self.outputPrinter.end()
