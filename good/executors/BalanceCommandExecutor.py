from abc import ABC

from good.executors.CommandExecutor import CommandExecutor
from other.Command import Command
from other.Database import Database


class BalanceCommandExecutor(CommandExecutor, ABC):
    BALANCE: str = "balance"
    def __init__(self, database: Database) -> None:
        super.__init__(database)

    def isApplicable(self, command: Command) -> bool:
        return command.getName() == self.BALANCE

    def isValid(self, command: Command) -> bool:
        return len(command.getParams()) == 1

    def execute(self, command: Command) -> str:
        user = command.getParams()[0]
        return str(self.database.getUserBalance(user))
