"""
class A  --> Class B ==>
         --> Class C ==> Class D

In Python by-default -: Inheritance follows DFS

In New Style Classes every class is assumed to be inherited by Object Class
It follows BFS

To see the order specified use __mro__ dunder method
"""
# Diamond Inheritance --> In Python older versions.

class A:
    def __init__(self):
        self.x = 100


class B(A):
    pass


class C(A):
    def __init__(self):
        self.x = 50


class D(B, C):
    pass


objD = D()
print(D.__mro__)
print(objD.x)


# New Style Classes
class A(object):
    def __init__(self):
        self.x = 100


class B(A):
    pass


class C(A):
    def __init__(self):
        self.x = 50


class D(B, C):
    pass


objD = D()
print(D.__mro__)
print(objD.x)

