from OutputPrinter import OutputPrinter
from command.CommandExecutor import CommandExecutor
from model.Car import Car
from model.Command import Command
from model.Slot import Slot
from service.ParkingLotService import ParkingLotService


class StatusCommandExecutor(CommandExecutor):
    COMMAND_NAME = "status"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        super().__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command) -> bool:
        params = command.getParams()
        return len(params) == 0

    def execute(self, command: Command) -> None:
        occupiedSlots: list[Slot] = self.parkingLotService.getOccupiedSlots()

        if not occupiedSlots:
            self.outputPrinter.parkingLotEmpty()
            return

        self.outputPrinter.statusHeader()
        for slot in occupiedSlots:
            parkedCar: Car = slot.getParkedCar()
            slotNumber: str = str(slot.getSlotNumber())

            self.outputPrinter.printWithNewLine(msg=self._padString(slotNumber, 12) +
                                                    self._padString(parkedCar.getRegistrationNumber(), 19) +
                                                    parkedCar.getColor())
    @staticmethod
    def _padString(word: str, length: int) -> str:
        return word + " " * length
