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
