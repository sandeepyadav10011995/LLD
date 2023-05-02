# Python program creating a
# context manager

class ContextManager():
	def __init__(self):
		print('init method called')
		
	def __enter__(self):
		print('enter method called')
		return self
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('exit method called')

with ContextManager() as manager:
	print('with statement block')

  
  
 # Python program shows the
# connection management
# for MongoDB

from pymongo import MongoClient

class MongoDBConnectionManager():
	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port
		self.connection = None

	def __enter__(self):
		self.connection = MongoClient(self.hostname, self.port)
		return self.connection

	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.connection.close()

# connecting with a localhost
with MongoDBConnectionManager('localhost', '27017') as mongo:
	collection = mongo.connection.SampleDb.test
	data = collection.find({'_id': 1})
	print(data.get('name'))
