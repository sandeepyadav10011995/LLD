"""
n Python, hashability is an important property for objects that are intended to be used as keys in dictionaries or elements in sets. If an object 
is not hashable, it cannot be used as a key in a dictionary or as an element in a set.

Making classes sortable is equally important because it allows instances of the class to be sorted and ordered. This can be useful in a wide range
of applications, including data analysis, numerical computing, and user interfaces.

#python

In Python, to make a user-defined class sortable and hashable, you need to define certain special methods in your class. These methods are:

__eq__: defines the equality comparison between objects of your class.
__lt__: defines the less-than comparison between objects of your class, which is used for sorting.
__hash__: returns a hash value for the object, which is used for hashing and for storing objects in sets and dictionaries.



# define Person class with two attributes name & age.
# define
#
__lt__ --: method to compare objects based on their name & age, method to compare objects based on their age
__hash__ -: method to generate a hash for object based on name & age.
"""
class Person:
    def __init _(self, name, age):
        self.name = name
        self.age = age
    def _eq_(self, other):
        return self.name == other. name and self.age == other. age

    def _It_(self, other):
        return self.age < other.age

    def __hash__ (self):
        return hash((self .name, self.age))
# Below is a usage example
person1 = Person("Alice", 30)
person2 = Person ("Bob", 25)
person3 = Person("Charlie", 35)
person4 = Person ("Charlie", 35)

people = [person1, person2, person, person4]
people_sorted = sorted (people)
# [person2, person1, person3, person4]

people_set = set(people)
# {person1, person2, person3}

print (person1 == person2)
# False
print (person1 == Person ("Alice", 30))
# True
