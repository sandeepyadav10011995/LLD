

class OutputPrinter:
    @staticmethod
    def printWithNewLine(msg: str) -> None:
        print(msg)
    def welcome(self) -> None:
        self.printWithNewLine(msg="Welcome to Go-Jek Parking Lot")

    def end(self) -> None:
        self.printWithNewLine(msg="Thanks for using Go-Jek Parking lot service.")

    def notFound(self) -> None:
        self.printWithNewLine(msg="Not Found")

    def statusHeader(self) -> None:
        self.printWithNewLine(msg="Slot No.    Registration No    Colour")

    def parkingLotFull(self) -> None:
        self.printWithNewLine(msg="Sorry, parking lot is full")

    def parkingLotEmpty(self) -> None:
        self.printWithNewLine(msg="Parking lot is empty")

    def inValidFile(self) -> None:
        self.printWithNewLine(msg="Invalid file given.")
