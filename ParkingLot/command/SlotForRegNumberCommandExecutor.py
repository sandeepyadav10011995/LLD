from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Command import Command
from model.ParkingLot import ParkingLot
from model.parking_strategy.DefaultOrderParkingStrategy import DefaultOrderParkingStrategy
from service.ParkingLotService import ParkingLotService
from validator.Validator import IntegerValidator


class SlotForRegNumberCommandExecutor(CommandExecutor):
    COMMAND_NAME = "slot_number_for_registration_number"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        return len(command.getParams()) == 1

    def execute(self, command: Command) -> None:
        regNumberToFind = int(command.getParams()[0])
        occupiedSlots = self.__parkingLotService.getOccupiedSlots()
        foundSlot = None
        for slot in occupiedSlots:
            if slot.getParkedCar().getRegistrationNumber() == regNumberToFind:
                foundSlot = slot
                break

        if foundSlot:
            # Print
            pass
        else:
            # Print
            pass
