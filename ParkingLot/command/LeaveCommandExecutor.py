from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Command import Command
from model.ParkingLot import ParkingLot
from model.parking_strategy.DefaultOrderParkingStrategy import DefaultOrderParkingStrategy
from service.ParkingLotService import ParkingLotService
from validator.Validator import IntegerValidator


class LeaveCommandExecutor(CommandExecutor):
    COMMAND_NAME = "leave"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        params = command.getParams()
        if len(params) != 1:
            return False

        return IntegerValidator.isInteger(params[0])

    def execute(self, command: Command) -> None:
        slotNumber = int(command.getParams()[0])
        self.__parkingLotService.makeSlotFree(slotNumber=slotNumber)
        # Print
