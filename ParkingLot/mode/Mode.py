
from abc import ABCMeta, abstractmethod
from exception.Exception import InvalidCommandException
from OutputPrinter import OutputPrinter
from command.CommandExecutorFactory import CommandExecutorFactory
from model.Command import Command


class Mode(metaclass=ABCMeta):
    def __init__(self, commandExecutorFactory: CommandExecutorFactory, outputPrinter: OutputPrinter):
        self.commandExecutorFactory: CommandExecutorFactory = commandExecutorFactory
        self.outputPrinter: OutputPrinter = outputPrinter

    def processCommand(self, command: Command) -> None:
        commandExecutor = self.commandExecutorFactory.getCommandExecutor(command=command)
        if commandExecutor.validate(command=command):
            commandExecutor.execute(command=command)
        else:
            raise InvalidCommandException()

    @abstractmethod
    def process(self):
        pass