from OutputPrinter import OutputPrinter
from command.CreateParkingLotCommandExecutor import CreateParkingLotCommandExecutor
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class CommandExecutorFactory:
    __commands = dict()

    def __init__(self, parkingLotService: ParkingLotService):
        self.__parkingLotService = parkingLotService
        self.__outputPrinter = OutputPrinter()
        self.__commands[CreateParkingLotCommandExecutor.COMMAND_NAME] = CreateParkingLotCommandExecutor(self.__parkingLotService, self.__outputPrinter)

    def validate(self, command: Command) -> bool:
        pass

    def execute(self) -> None:
        pass
