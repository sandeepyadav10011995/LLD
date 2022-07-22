from OutputPrinter import OutputPrinter
from command.CommandExecutorFactory import CommandExecutorFactory
from mode.Mode import Mode
from model.Command import Command


class FileMode(Mode):
    def __init__(self, commandExecutorFactory: CommandExecutorFactory, outputPrinter: OutputPrinter, fileName: str) -> None:
        super().__init__(commandExecutorFactory, outputPrinter)
        self.fileName = fileName
        
    def process(self):
        with open(file=self.fileName, mode="r") as file:
            for line in file:
                if line != "":
                    command = Command(inputLine=line)
                    self.processCommand(command=command)
