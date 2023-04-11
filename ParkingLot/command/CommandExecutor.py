from abc import ABCMeta, abstractmethod

from OutputPrinter import OutputPrinter
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class CommandExecutor(metaclass=ABCMeta):
    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter

    @abstractmethod
    def validate(self, command: Command) -> bool:
        raise NotImplementedError("Please implement this method!")

    @abstractmethod
    def execute(self, command: Command) -> None:
        raise NotImplementedError("Please implement this method!")