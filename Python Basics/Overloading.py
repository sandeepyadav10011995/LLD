"""
------------------------------------------- Overloading ---------------------------------------------------------

1. Python invokes the __call__ method any time, someone tries to treat an instance of your object as a function.
   In simple word, it makes the object CALLABLE.

2. Python call the __getattr__ function only after a search through the instance dictionary and base classes comes up
   empty-handed. ---> DELEGATION

3.We can use the __lt__, __gt__ and other methods to implement support for the rich comprehensions where we have more
  complete control over how the objects behave during different types of comparisons.

"""

class Student:
    def __init__(self, marks):
        self.marks = marks

    def displayMarks(self):
        return self.marks

    def __add__(self, gracemarks):
        self.marks += gracemarks

    def __repr__(self):
        return "I WILL NOT PRINT"

raj = Student(marks=45)
print(raj.displayMarks())
raj+32
print(raj.displayMarks())


# Addition of two vectors

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)

    def __repr__(self):
        return f"Vector {self.a}, {self.b}"


v1 = Vector(4, 8)
print(v1)
v2 = Vector(9, 8)
print(v2)
print(v1+v2)
