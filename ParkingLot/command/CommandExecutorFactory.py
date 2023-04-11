from OutputPrinter import OutputPrinter

from model.Command import Command
from service.ParkingLotService import ParkingLotService

from command.CommandExecutor import CommandExecutor
from command.CreateParkingLotCommandExecutor import CreateParkingLotCommandExecutor
from command.ParkCommandExecutor import ParkCommandExecutor
from command.LeaveCommandExecutor import LeaveCommandExecutor
from command.ColorToRegNumberCommandExecutor import ColorToRegNumberCommandExecutor
from command.ColorToSlotNumberCommandExecutor import ColorToSlotNumberCommandExecutor
from command.ExitCommandExecutor import ExitCommandExecutor
from command.SlotForRegNumberCommandExecutor import SlotForRegNumberCommandExecutor
from command.StatusCommandExecutor import StatusCommandExecutor

from exception.Exception import InvalidCommandException


class CommandExecutorFactory:
    def __init__(self, parkingLotService: ParkingLotService) -> None:
        self._commands: dict[str: CommandExecutor] = {}
        self.outputPrinter: OutputPrinter = OutputPrinter()
        # Insert all the commands in the commands dict
        self._commands[CreateParkingLotCommandExecutor.COMMAND_NAME] = CreateParkingLotCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)
        self._commands[ParkCommandExecutor.COMMAND_NAME] = ParkCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)
        self._commands[LeaveCommandExecutor.COMMAND_NAME] = LeaveCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)
        self._commands[StatusCommandExecutor.COMMAND_NAME] = StatusCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)
        self._commands[ColorToRegNumberCommandExecutor.COMMAND_NAME] = ColorToRegNumberCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)
        self._commands[ColorToSlotNumberCommandExecutor.COMMAND_NAME] = ColorToSlotNumberCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)
        self._commands[SlotForRegNumberCommandExecutor.COMMAND_NAME] = SlotForRegNumberCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)
        self._commands[ExitCommandExecutor.COMMAND_NAME] = ExitCommandExecutor(
            parkingLotService=parkingLotService, outputPrinter=self.outputPrinter)

    def getCommandExecutor(self, command: Command) -> CommandExecutor:
        commandExecutor: CommandExecutor = self._commands.get(command.getCommandName().replace("\n", ""))
        if commandExecutor is None:
            print("InValid Commenad")
            # raise InvalidCommandException
        else:
            return commandExecutor
