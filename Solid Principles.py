"""
S: Single Responsibility
O: Open/Closed Principle
L: Liskov Substitution Principle
I: Interface Segmented Principle
D: Dependency Inversion Principle

Advantages -: Helps to write better code
- Avoid Duplicate Code
- Easy to maintain
- Easy to understand
- Flexible software
- Reduce Complexity

"""
from abc import ABC, abstractmethod

"""
S: Single Responsibility :: A class should have only 1 reason to change.
Before.py
Marker Entity:
"""

class Marker:
    name: str
    color: str
    year: int
    price: int

    def __init__(self, name: str, color: str, year: int, price: int) -> None:
        self.name = name
        self.color = color
        self.year = year
        self.price = price


class Invoice:
    marker: Marker
    quantity: int

    def __init__(self, marker: Marker, quantity: int) -> None:
        self.marker = marker
        self.quantity = quantity

    def calculationTotal(self) -> int:
        totalPrice = self.marker.price * self.quantity
        return totalPrice

    def printInvoice(self):
        # print the Invoice
        pass

    def saveToDB(self):
        # Save the data into DB
        pass


"""
Problem : 
Reasons to change Invoice Class
1. Lets say we want to add GST to the totalPrice
2. Change in the logic of printing the Invoice
3. Change in the logic of saving the data to DB
After.py
"""

class Invoice:
    marker: Marker
    quantity: int

    def __init__(self, marker: Marker, quantity: int) -> None:
        self.marker = marker
        self.quantity = quantity

    def calculationTotal(self) -> int:
        totalPrice = self.marker.price * self.quantity
        return totalPrice

class InvoiceDAO:
    invoice: Invoice
    def __init__(self, invoice: Invoice) -> None:
        self.invoice = invoice

    def saveToDB(self):
        # Save the data into DB
        pass

class InvoicePrinter:
    invoice: Invoice
    def __init__(self, invoice: Invoice) -> None:
        self.invoice = invoice

    def saveToDB(self):
        # Save the data into DB
        pass


"""
O: Open/Closed Principle :: Open for Extension but Closed for Modification :: Solution: Interface
Requirement :: Save the data into file
Before.py
"""
class InvoiceDAO:
    invoice: Invoice
    def __init__(self, invoice: Invoice) -> None:
        self.invoice = invoice

    def saveToDB(self):
        # Save the data into DB
        pass

    def saveToFile(self, fileName: str):
        # Save the data into File
        pass

"""
Problem : It is not following Open/Close Principle -> Violation
After.py
"""
class IInvoiceDAO(metaclass=ABC):
    @abstractmethod
    def save(self, invoice: Invoice):
        pass


class DatabaseInvoiceDAO(IInvoiceDAO):
    def save(self, invoice: Invoice):
        # Save the data into DB
        pass

class FileInvoiceDAO(IInvoiceDAO):
    def save(self, invoice: Invoice):
        # Save the data into File
        pass




"""
L: Liskov Substitution Principle :: If class B is a subtype of class A, then we should be able to replace object of A 
and B without breaking the behaviour of the program.
Note :: Subclass should extend the capability of parent class not narrow it down !!
Before.py
"""

class Bike(metaclass=ABC):
    @abstractmethod
    def turnOnEngine(self) -> None:
        pass

    @abstractmethod
    def accelerate(self) -> None:
        pass


class Motorcycle(Bike):
    isEngineOn: bool
    speed: int

    def turnOnEngine(self) -> None:
        # turn on the engine
        self.isEngineOn = True

    def accelerate(self) -> None:
        # increase the speed
        self.speed += 10

class Bicycle(Bike):
    def turnOnEngine(self) -> None:  ## Here we have narrow down the capability !!
        raise AssertionError("There is no engine")

    def accelerate(self) -> None:
        # Do something
        pass


"""
I: Interface Segmented Principle :: Interface should be such, that client should not implement unnecessary functions 
they do not need !!

Before.py
"""

class RestaurantEmployee(metaclass=ABC):
    @abstractmethod
    def washDishes(self) -> None:
        pass

    @abstractmethod
    def servesCustomer(self) -> None:
        pass

    @abstractmethod
    def cookFood(self) -> None:
        pass

class Waiter(RestaurantEmployee):
    def washDishes(self) -> None:  # Don't need
        # NOT MY JOB
        pass

    def servesCustomer(self) -> None:
        # Yes and here is my implementation
        print("Serving the customer!!")

    def cookFood(self) -> None:  # Don't need
        # NOT MY JOB
        pass

"""
After.py
"""
class IWaiter(metaclass=ABC):
    @abstractmethod
    def servesCustomer(self) -> None:
        pass

    @abstractmethod
    def takeOrder(self) -> None:
        pass

class IChef(metaclass=ABC):
    @abstractmethod
    def cookFood(self) -> None:
        pass

    @abstractmethod
    def decideMenu(self) -> None:
        pass


class Waiter(IWaiter):
    def servesCustomer(self) -> None:
        # Yes and here is my implementation
        print("Serving the customer!!")

    def takeOrder(self) -> None:
        print("Taking orders!!")



"""
D: Dependency Inversion Principle :: Class should depend on interfaces rather concrete class
Before.py
"""
class IKeyboard(metaclass=ABC):
    pass

class WiredKeyboard(IKeyboard):  # Concrete class
    pass

class WirelessKeyboard(IKeyboard):  # Concrete class
    pass


class IMouse(metaclass=ABC):
    pass

class WiredMouse(IMouse):  # Concrete class
    pass

class WirelessMouse(IMouse):  # Concrete class
    pass


class MacBook:
    keyboard: WiredKeyboard
    mouse: WiredMouse
    def __init__(self):
        self.keyboard = WiredKeyboard()  # Concrete class
        self.mouse = WiredMouse()  # Concrete class

"""
Problem :: In future I want to enhance the Mac --> Cannot do it.
After.py
"""

class MacBookChanged:
    keyboard: IKeyboard
    mouse: IMouse
    def __init__(self, keyboard: IKeyboard, mouse: IMouse):  # Take the keyboard or mouse via constructor injection
        self.keyboard = keyboard
        self.mouse = mouse

