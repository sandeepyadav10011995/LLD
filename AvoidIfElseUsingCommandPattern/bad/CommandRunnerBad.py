from other.Command import Command
from other.Database import Database
from other.RechargeProvider import RechargeProvider


class CommandRunnerBad:
    def __init__(self, database: Database, rechargeProvider: RechargeProvider) -> None:
        self.database = database
        self.rechargeProvider = rechargeProvider

    def runCommand(self, command: Command) -> str:
        if command.getName() == "balance":
            if len(command.getParams()) != 1:
                return "InValid Command"
            user = command.getParams()[0]
            return self.database.getUserBalance(user)
        elif command.getName() == "recharge":
            if len(command.getParams()) != 1:
                return "InValid Command"
            user = command.getParams()[0]
            rechargeAmount = int(command.getParams()[1])
            userBalance = self.database.getUserBalance(user)
            if userBalance < rechargeAmount:
                return "Not sufficient balance"

            self.rechargeProvider.recharge(user=user, amount=rechargeAmount)
            return "Recharge Done"
        else:
            return "InValid Command"
