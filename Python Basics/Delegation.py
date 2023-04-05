"""
Delegation is an object-oriented technique(also called a design pattern)

Let's say we have an object x and, we want to change the behaviour of just one it's methods.

We can create a new class that provides a new implementation of the method we're interested in changing and delegates
all other methods to the corresponding method of x.

Example :


"""

class MyList:
    def __init__(self, a):
        self.a = a

    def append(self, s):
        self.a.append(s.upper())

    def __getattr__(self, name):  # To make other functionality work as it is we are using __getattr__ as a dispatcher.
        return getattr(self.a, name)


a = [1, 2, 3, 4]
b = MyList(a)
print(b.a)
b.append("sd")
print(b.a)
b.remove(3)
print(b.a)
