from OutputPrinter import OutputPrinter
from command.CommandExecutorFactory import CommandExecutorFactory
from command.ExitCommandExecutor import ExitCommandExecutor
from mode.Mode import Mode
from model.Command import Command


class InteractiveMode(Mode):
    def __init__(self, commandExecutorFactory: CommandExecutorFactory, outputPrinter: OutputPrinter) -> None:
        super().__init__(commandExecutorFactory, outputPrinter)

    def process(self):
        self.outputPrinter.welcome()
        while True:
            line: str = str(input("Enter the command: "))
            command: Command = Command(inputLine=line)
            self.processCommand(command=command)
            if command.getCommandName() == ExitCommandExecutor.COMMAND_NAME:
                break