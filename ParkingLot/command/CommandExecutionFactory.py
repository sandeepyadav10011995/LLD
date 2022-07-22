from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from command.CreateParkingLotCommandExecutor import CreateParkingLotCommandExecutor
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class CommandExecutorFactory:
    __commands = dict()

    def __init__(self, parkingLotService: ParkingLotService):
        self.__parkingLotService = parkingLotService
        self.__outputPrinter = OutputPrinter()
        self.__commands[CreateParkingLotCommandExecutor.COMMAND_NAME] = CreateParkingLotCommandExecutor(self.__parkingLotService, self.__outputPrinter)

    def getCommandExecutor(self, command: Command) -> CommandExecutor:
        commandExecutor = self.__commands.get(command.getCommandName())
        if commandExecutor is None:
            pass
        return commandExecutor
