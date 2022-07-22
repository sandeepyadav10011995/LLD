
from abc import ABCMeta, abstractmethod

from OutputPrinter import OutputPrinter
from command.CommandExecutorFactory import CommandExecutorFactory
from model.Command import Command


class Mode(metaclass=ABCMeta):
    def __init__(self, commandExecutorFactory: CommandExecutorFactory, outputPrinter: OutputPrinter):
        self.commandExecutorFactory = commandExecutorFactory
        self.outputPrinter = outputPrinter

    def processCommand(self, command: Command) -> None:
        commandExecutor = self.commandExecutorFactory.getCommandExecutor(command=command)
        if commandExecutor.validate(command=command):
            commandExecutor.execute(command=command)
        else:
            pass

    @abstractmethod
    def process(self):
        pass
