from abc import ABC

from Cell import Cell
from composition.Move import Move


class VerticalMove(Move, ABC):
    @staticmethod
    def canMove(source: Cell, destination: Cell) -> bool:
        """
            Check if source and destination are in vertical
        """
        return False
