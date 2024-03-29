

class InvalidModeException(Exception):
    pass


class InvalidCommandException(Exception):
    pass


class ParkingLotException(Exception):
    status_code = 500

    def __init__(self, errorMessage: str) -> None:
        self.errorMessage = errorMessage


class InvalidSlotException(ParkingLotException):
    pass


class SlotAlreadyOccupiedException(ParkingLotException):
    pass


class NoFreeSlotAvailableException(ParkingLotException):
    pass
