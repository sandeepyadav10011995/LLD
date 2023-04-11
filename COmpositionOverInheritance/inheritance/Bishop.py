from Cell import Cell
from inheritance.Piece import Piece


class Bishop(Piece):
    @staticmethod
    def canMove(source: Cell, destination: Cell) -> bool:
        """
            Check if source and destination are in diagonal
        """
        return True
