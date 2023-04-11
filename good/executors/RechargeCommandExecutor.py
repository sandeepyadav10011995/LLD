from abc import ABC

from good.executors.CommandExecutor import CommandExecutor
from other.Command import Command
from other.Database import Database
from other.RechargeProvider import RechargeProvider


class RechargeProviderExecutor(CommandExecutor, ABC):
    RECHARGE: str = "recharge"
    def __init__(self, database: Database, rechargeProvider: RechargeProvider) -> None:
        super.__init__(database)
        self.rechargeProvider = rechargeProvider

    def isApplicable(self, command: Command) -> bool:
        return command.getName() == self.RECHARGE

    def isValid(self, command: Command) -> bool:
        return len(command.getParams()) == 2

    def execute(self, command: Command) -> str:
        user: str = command.getParams()[0]
        rechargeAmount: int = int(command.getParams()[1])
        userBalance: int = self.database.getUserBalance(user)
        if userBalance < rechargeAmount:
            return "Not sufficient balance"

        self.rechargeProvider.recharge(user=user, amount=rechargeAmount)
        return "Recharge Done"
