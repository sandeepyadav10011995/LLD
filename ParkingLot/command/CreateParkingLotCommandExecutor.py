from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Command import Command
from model.ParkingLot import ParkingLot
from model.parkingStrategy.NaturalOrderingParkingStrategy import NaturalOrderingParkingStrategy
from service.ParkingLotService import ParkingLotService
from validator.Validator import IntegerValidator


class CreateParkingLotCommandExecutor(CommandExecutor):
    COMMAND_NAME = "create_parking_lot"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService=parkingLotService, outputPrinter=outputPrinter)

    def validate(self, command: Command) -> bool:
        params = command.getParams()
        return False if len(params) != 1 else IntegerValidator.isInteger(params[0])

    def execute(self, command: Command) -> None:
        parkingLotCapacity: int = int(command.getParams()[0])
        parkingLot: ParkingLot = ParkingLot(capacity=parkingLotCapacity)
        self.parkingLotService.createParkingLot(parkingLot=parkingLot, parkingStrategy=NaturalOrderingParkingStrategy())
        self.outputPrinter.printWithNewLine(f"Created a parking lot with {parkingLot.getCapacity()} slots")