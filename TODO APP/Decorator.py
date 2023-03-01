"""
Iterator objects in python confirm to the iterator protocol, which basically means they provide two methods;
    a. __iter__()
        The __iter__() return the iterator object and is implicitly called at the start of the loops.

    b. next()
        The nex() method return the next values and is implicitly called at each loop increment. next() raises a
        StopIteration exception when they are no more values to return.

"""
import profile


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# for c in Counter(3, 8):
#     print(c)


"""
Generators : 
    *   Under the hood the generator objects support the iterator protocol.
    *   When body of function contains one or more occurrences of keyword yield, the function is known as generators.
    *   When you call a generator, function body does not execute.
    *   Instead, calling a generator returns special iterator object.
    *   When next method of this iterator object is called, function body executes up-to next yield statement.
    *   When yield statement executes, function execution is frozen; with current point of execution and local variable 
        intact, and expression following yield is returned as result of next method.
    *   When next called again, execution resumes from where it left off; again up-to next yield statement. If function 
        body ends or executes a return statement; iterator raises a StopIteration exception to indicate that iteration 
        is finished.
        
        
    In-short generators are also doing the same just in a simple manner, making our life easier.
"""


def counter(low, high):
    current = low
    while current < high:
        yield current
        current += 1


# for c in counter(3, 8):
#     print(c)

"""
Advantages Of Generators -:
    *   Generators expressions are a whole other can of worms(AWESOME WORMS !!). They may be used in place of List 
        Comprehension to save memory. Generator expressions have been introduced as a high performance, memory efficient
        generalization of list comprehensions.
    *   Generator expressions are especially useful with functions like sum(), min(), max() that reduce an iterable 
        input to a single value.
        
    *   For instance, the following summation code will be build a full list of squares in memory., iterate over those 
        values, and, when the references is no longer needed, delete the list-:
        -   sum([x*x for x in range(10)]) --> Bad  
        -   Memory is conserved by using a generator expression instead;
        -   sum(x*x for x in range(10)) --> Awesome
    
"""


@profile
def list_comprehension():
    val = sum([x*x for x in range(10)])
    print("done")


@profile
def generator_expressions():
    val = sum(x * x for x in range(10))
    print("done")


list_comprehension()
# python -m memory_profiler intro.py





"""
According to python.org, "A decorator is the name used for a software design pattern. Decorators can dynamically alter
the functionality of function, method or class without having to directly use subclasses or change the source code of
the function being decorated.

Reason -: Since functions ar the first-class objects in python, we can write functions that both
          a. accept the function as argument values and,
          b. return function objects as return values.

Nested Decorators : makeitalic --> makebold
Requirement --> First Italic --> Second Bold
Example -: <i>hello world</i>
           <b><i>hello world</i></b>
"""


def make_bold(fn):
    def wrapped(*args):
        return "<b>" + fn(*args) + "</b>"
    return wrapped


def make_italic(fn):
    def wrapped(*args):
        return "<i>" + fn(*args) + "</i>"
    return wrapped


@make_bold
@make_italic
def hello():
    return "hello world"


res = hello()
print(res)


# hello() --> make_italic(hello) --> make_bold(make_italic(hello))






"""
According to python.org, "A decorator is the name used for a software design pattern. Decorators can dynamically alter
the functionality of function, method or class without having to directly use subclasses or change the source code of
the function being decorated.

Reason -: Since functions are the first-class objects in python, we can write functions that both
          a. accept the function as argument values and,
          b. return function objects as return values.

Note: Decorators need not be always be function, they can be actually any callable.
      The only constraint upon the object returned by the decorators is that it can be used as a function --> which
      basically means it must be callable.

      Now the question is --> How to make an object of a class callable ?
"""


class ABC:
    def __init__(self, a):
        print("__init__")
        self.a = a


# Simple flow
obj = ABC(3)
print(callable(obj))  # Return False "AttributeError obj has no __call__ method !"


class Decorator(object):
    def __init__(self, f):
        self.fn = f

    # To make the object of a class callable --> we need to add the in-built __call__()
    def __call__(self, *args):
        print("Something before function is being done")
        self.fn(*args)
        print("Something after function is being done")


# func1 --> Decorator(func1)(*args)
@Decorator
def func1():
    return "hello in func1"


func1()
