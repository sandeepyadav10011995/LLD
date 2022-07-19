from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Command import Command
from model.ParkingLot import ParkingLot
from model.parking_strategy.DefaultOrderParkingStrategy import DefaultOrderParkingStrategy
from service.ParkingLotService import ParkingLotService
from validator.Validator import IntegerValidator


class ColorToSlotNumberCommandExecutor(CommandExecutor):
    COMMAND_NAME = "slot_numbers_for_cars_with_colour"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        return len(command.getParams()) == 1

    def execute(self, command: Command) -> None:
        slotsForColor = self.__parkingLotService.getSlotsForColor(color=command.getParams()[0])
        if len(slotsForColor) == 0:
            result = "Not Found"
        else:
            car_list = [str(slot.getSlotNumber()) for slot in slotsForColor]
            result = ", ".join(car_list)
        self.__outputPrinter.printWithNewLine(result)
