# ---------------------- Lambda -----------------------
        The syntax is: lambda arguments: expression

        Example -:
                def add(x,y):
                    return x + y
            Can be translated to:
                lambda x, y: x + y

        Lambdas differ from normal Python methods because they can have only one expression, can't contain any statements and
        their return type is a function object. So the line of code above doesn't exactly return the value x + y but the
        function that calculates x + y


# ----------------------- Map ---------------------------
        The map() function iterates through all items in the given iterable and executes the function we passed as an argument
        on each of them.

        The syntax is: map(function, iterable(s))
        We can pass as many iterable objects as we want after passing the function we want to use:

        # Without using lambdas
        def starts_with_A(s):
            return s[0] == "A"

        fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
        map_object = map(starts_with_A, fruit)

        print(list(map_object))
        Output -: [True, False, False, True, False]

        fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
        map_object = map(lambda s: s[0] == "A", fruit)

        print(list(map_object))
        Output : [True, False, False, True, False]

# ------------------------------- Filter ----------------------------

        The filter() Function
        Similar to map(), filter() takes a function object and an iterable and creates a new list.

        As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition, i.e.
        the function we passed returns True.

        The syntax is: filter(function, iterable(s))


        Using the previous example, we can see that the new list will only contain elements for which the starts_with_A()
        function returns True:

        # Without using lambdas
        def starts_with_A(s):
            return s[0] == "A"

        fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
        filter_object = filter(starts_with_A, fruit)

        print(list(filter_object))
        Output-: ['Apple', 'Apricot']


        fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
        filter_object = filter(lambda s: s[0] == "A", fruit)

        print(list(filter_object))

        Output : ['Apple', 'Apricot']

# -------------------------- Reduce ------------------------

        reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable 
        we've passed. Instead, it returns a single value.

        Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.

        The syntax is:

        reduce(function, sequence[, initial])
        from functools import reduce
        def add(x, y):
            return x + y

        list = [2, 4, 7, 3]
        print(reduce(add, list))
        Running this code would yield:

        16
        Again, this could be written using lambdas:

        from functools import reduce

        list = [2, 4, 7, 3]
        print(reduce(lambda x, y: x + y, list))
        print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))
        Output -:
        16
        With an initial value: 26
        
