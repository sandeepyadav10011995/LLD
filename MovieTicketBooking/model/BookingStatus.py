from enum import Enum


class BookingStatus(Enum):
    Created = "Created",
    Confirmed = "Confirmed",
    Expired = "Expired"
