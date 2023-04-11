from good.executors.CommandExecutor import CommandExecutor
from other.Command import Command


class CommandRunnerBad:
    def __init__(self, commandExecutors: list[CommandExecutor]) -> None:
        self.commandExecutors = commandExecutors

    def runCommand(self, command: Command) -> str:
        for commandExecutor in self.commandExecutors:
            if commandExecutor.isApplicable(command):
                return commandExecutor.execute(command)
        return "InValid Command"
