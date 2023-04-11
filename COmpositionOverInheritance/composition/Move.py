from abc import ABCMeta, abstractmethod

from Cell import Cell


class Move(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def canMove(source: Cell, destination: Cell) -> bool:
        pass
