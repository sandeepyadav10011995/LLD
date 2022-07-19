from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from exception.Exception import NoFreeSlotAvailableException
from model.Car import Car
from model.Command import Command
from model.ParkingLot import ParkingLot
from model.parking_strategy.DefaultOrderParkingStrategy import DefaultOrderParkingStrategy
from service.ParkingLotService import ParkingLotService
from validator.Validator import IntegerValidator


class ParkCommandExecutor(CommandExecutor):
    COMMAND_NAME = "park"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        return len(command.getParams()) == 2

    def execute(self, command: Command) -> None:
        car: Car = Car(registrationNumber=command.getParams()[0], color=command.getParams()[1])
        try:
            slot_number_allocated = self.__parkingLotService.park(car=car)
            self.__outputPrinter.printWithNewLine(f"Allocated Slot Number is : {slot_number_allocated}")
        except NoFreeSlotAvailableException:
            self.__outputPrinter.printWithNewLine("Parking Lot is Full !!")
