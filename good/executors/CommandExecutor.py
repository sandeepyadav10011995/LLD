from abc import ABCMeta, abstractmethod
from other.Command import Command
from other.Database import Database


class CommandExecutor(metaclass=ABCMeta):
    def __init__(self, database: Database) -> None:
        self.database = database

    def execute(self, command: Command) -> str:
        return (
            self.executeValidCommand(command)
            if self.isValid(command)
            else "InValid Command"
        )

    @abstractmethod
    def isValid(self, command: Command) -> bool:
        pass

    @abstractmethod
    def isApplicable(self, command: Command) -> bool:
        pass

    @abstractmethod
    def executeValidCommand(self, command: Command) -> str:
        pass

