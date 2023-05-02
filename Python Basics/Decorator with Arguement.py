# Python code to illustrate
# Decorators basic in Python
def decorator_fun(func):
	print("Inside decorator")
	def inner(*args,**kwargs):
		print("Inside inner function")
		print("Decorated the function")
		# do operations with func
		func()
	return inner()
@decorator_fun
def func_to():
	print("Inside actual function")
func_to


# Python code to illustrate
# Decorators with parameters in Python

def decorator(*args, **kwargs):
	print("Inside decorator")
	
	def inner(func):
		
		# code functionality here
		print("Inside inner function")
		print("I like", kwargs['like'])
		
		func()
		
	# returning inner function
	return inner

@decorator(like = "geeksforgeeks")
def my_func():
	print("Inside actual function")


	
	
# Python code to illustrate
# Decorators with parameters in Python (Multi-level Decorators)


def decodecorator(dataType, message1, message2):
	def decorator(fun):
		print(message1)
		def wrapper(*args, **kwargs):
			print(message2)
			if all([type(arg) == dataType for arg in args]):
				return fun(*args, **kwargs)
			return "Invalid Input"
		return wrapper
	return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
	st = ''
	for i in args:
		st += i
	return st


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ


print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))
