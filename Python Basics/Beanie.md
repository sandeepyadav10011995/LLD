## Introduction
Beanie is a Python library that provides an ORM (Object-Relational Mapping) for MongoDB. It makes it easy to work with MongoDB databases by providing an intuitive 
syntax for querying and manipulating data, similar to other ORM libraries like SQLAlchemy or Django ORM.

## Here are some use cases of Beanie in Python:

  #### Data modeling: 
  Beanie allows you to define data models using Python classes, and map those classes to MongoDB collections. You can define fields for the model and specify their 
  data types, default values, and other attributes.

  #### CRUD operations: 
  Beanie provides an easy-to-use API for performing CRUD (Create, Read, Update, Delete) operations on MongoDB collections. You can create, read, update, and delete 
  documents in a collection using simple Python code.

  #### Querying: 
  Beanie supports MongoDB's query language, allowing you to filter and sort documents based on criteria such as field values, regular expressions, and more. You can 
  use operators such as ==, !=, >, <, in, contains, etc. to filter documents.

  #### Indexing: 
  Beanie supports indexing on MongoDB collections, which can improve query performance. You can define indexes on one or more fields of a collection, and Beanie will 
  automatically create those indexes in the database.

  #### Relationships: 
  Beanie supports relationships between MongoDB collections, similar to how foreign keys work in SQL databases. You can define a reference field in a model that points 
  to another model, and Beanie will automatically manage the relationship between the two collections.

##### User.py
```
from beanie import Document, IntField, StringField

class User(Document):
    name: StringField(required=True)
    age: IntField(minimum=0, maximum=120, required=True)
    email: StringField(required=True, unique=True)
```

##### db.py
In this example, we've created an instance of the AsyncIOMotorClient class to connect to a MongoDB database. We've then initialized Beanie with the database 
name, a list of document models (in this case, just the User model), and the MongoDB client instance. Finally, we've used Beanie's API to perform CRUD 
operations on the User collection.
```
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
init_beanie(database="mydb", document_models=[User], client=client)

# Create a new user
user = User(name="John Doe", age=30, email="john.doe@example.com")
await user.insert()

# Update an existing user
user.age = 31
await user.update()

# Delete a user
await user.delete()

# Query users
users = await User.find_all(age=30)

```


