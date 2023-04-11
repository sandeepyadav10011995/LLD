from Cell import Cell
from composition import Move


class Piece:
    def __init__(self, allowedMoves: list[Move]) -> None:
        self.allowedMoves = allowedMoves

    def canMove(self, source: Cell, destination: Cell) -> bool:
        for allowedMove in self.allowedMoves:
            if allowedMove.canMove(source, destination):
                return True

        return False
