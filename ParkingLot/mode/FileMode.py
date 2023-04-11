from OutputPrinter import OutputPrinter
from command.CommandExecutorFactory import CommandExecutorFactory
from mode.Mode import Mode
from model.Command import Command


class FileMode(Mode):
    _fileName: str = None
    def __init__(self, commandExecutorFactory: CommandExecutorFactory, outputPrinter: OutputPrinter,
                 fileName: str) -> None:
        super().__init__(commandExecutorFactory, outputPrinter)
        self._fileName = fileName

    def process(self):
        try:
            with open(file=self._fileName, mode="r") as file:
                for line in file:
                    if line is not None:
                        command: Command = Command(inputLine=line)
                        self.processCommand(command=command)
        except FileNotFoundError as e:
            self.outputPrinter.inValidFile()
            return