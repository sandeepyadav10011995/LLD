from Cell import Cell
from inheritance.Piece import Piece


class Queen(Piece):
    @staticmethod
    def canMove(source: Cell, destination: Cell) -> bool:
        """
            Check if source and destination are in diagonal
            Check if source and destination are in horizontal
            Check if source and destination are in vertical
        """
        return True