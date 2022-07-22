

class Seat:
    def __init__(self, id: str, rowNo: int, seatNo: int) -> None:
        self._id = id
        self._rowNo = rowNo
        self._seatNo = seatNo

    def getId(self):
        return self._id

    def getRowNo(self):
        return self._rowNo

    def getSeatNo(self):
        return self._seatNo
