

class Seat:
    def __init__(self, id: str, rowNo: int, seatNo: int) -> None:
        self.id = id
        self.rowNo = rowNo
        self.seatNo = seatNo

    def getId(self):
        return self.id

    def getRowNo(self):
        return self.rowNo

    def getSeatNo(self):
        return self.seatNo
