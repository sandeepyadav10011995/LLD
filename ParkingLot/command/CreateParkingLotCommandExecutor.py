from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Command import Command
from model.ParkingLot import ParkingLot
from model.parking_strategy.DefaultOrderParkingStrategy import DefaultOrderParkingStrategy
from service.ParkingLotService import ParkingLotService
from validator.Validator import IntegerValidator


class CreateParkingLotCommandExecutor(CommandExecutor):
    COMMAND_NAME = "create_parking_lot"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        params = command.getParams()
        if len(params) != 1:
            return False

        return IntegerValidator.isInteger(params[0])

    def execute(self, command: Command) -> None:
        parkingLotCapacity = int(command.getParams()[0])
        parkingLot = ParkingLot(capacity=parkingLotCapacity)
        self.__parkingLotService.createParkingLot(parkingLot=parkingLot, parkingStrategy=DefaultOrderParkingStrategy())
        self.__outputPrinter.printWithNewLine(f"Created a parking lot with {parkingLot.getCapacity()} slots")
