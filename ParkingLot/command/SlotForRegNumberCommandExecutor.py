from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Command import Command
from model.Slot import Slot
from service.ParkingLotService import ParkingLotService


class SlotForRegNumberCommandExecutor(CommandExecutor):
    COMMAND_NAME = "slot_number_for_registration_number"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        return len(command.getParams()) == 1

    def execute(self, command: Command) -> None:
        occupiedSlots: list[Slot] = self.parkingLotService.getOccupiedSlots()
        regNumberToFind: str = command.getParams()[0]

        foundSlot = None
        for slot in occupiedSlots:
            if slot.getParkedCar().getRegistrationNumber() == regNumberToFind:
                foundSlot = slot
                break

        if foundSlot:
            self.outputPrinter.printWithNewLine(str(foundSlot.getSlotNumber()))
        else:
            self.outputPrinter.notFound()
