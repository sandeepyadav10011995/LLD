# MongoDB

## Intro -:
### MongoDB is a document database. It stores data in a type of JSON format called BSON.
* The MongoDB Query API is the way you will interact with your data.
* A record in MongoDB is a document, which is a data structure composed of key value pairs similar to the structure of JSON objects.
* Records in a MongoDB database are called documents, and the field values may include numbers, strings, booleans, arrays, or even nested documents.
    
#### The MongoDB Query API can be used two ways:
      CRUD Operations
      Aggregation Pipelines

#### Create DB
      To see all available databases, in your terminal type -:  show dbs
      
      Change or Create a Database -: use blog --> Create a new database called "blog"
      
#### Create Collection using mongosh  
      Method 1: db.createCollection("posts")
      Method 2: db.posts.insertOne(object)
      
      Remember: In MongoDB, a collection is not actually created until it gets content!

#### Insert Documents
      Method 1: insertOne() -> Note: If you try to insert documents into a collection that does not exist, MongoDB will create the collection automatically.
      Method 2: To insert multiple documents at once, use the insertMany() method.

#### Find Data
      Method 1: find()
          To select data from a collection in MongoDB, we can use the find() method.
          This method accepts a query object. If left empty, all documents will be returned.
      Method 2: findOne()
          To select only one document, we can use the findOne() method.
          This method accepts a query object. If left empty, it will return the first document it finds.
          Note: This method only returns the first match it finds.
      
      This parameter is optional. If omitted, all fields will be included in the results.
      Note: You cannot use both 0 and 1 in the same object. The only exception is the _id field. 
            You should either specify the fields you would like to include or the fields you would like to exclude.


#### Update Document
      Method 1: updateOne()
            The updateOne() method will update the first document that is found matching the provided query.
      Method 2: updateMany()
            The updateMany() method will update all documents that match the provided query.
      
      Insert if not found
            If you would like to insert the document if it is not found, you can use the upsert option.

#### Delete Documents
      Method 1: deleteOne()
            The deleteOne() method will delete the first document that matches the query provided.
      Method 2: deleteMany()
            The deleteMany() method will delete all documents that match the query provided.
      
### MongoDB Query Operators

#### Comparison
      The following operators can be used in queries to compare values:
            $eq: Values are equal
            $ne: Values are not equal
            $gt: Value is greater than another value
            $gte: Value is greater than or equal to another value
            $lt: Value is less than another value
            $lte: Value is less than or equal to another value
            $in: Value is matched within an array

#### Logical
      The following operators can logically compare multiple queries.
            $and: Returns documents where both queries match
            $or: Returns documents where either query matches
            $nor: Returns documents where both queries fail to match
            $not: Returns documents where the query does not match

#### Evaluation
      The following operators assist in evaluating documents.
            $regex: Allows the use of regular expressions when evaluating field values
            $text: Performs a text search
            $where: Uses a JavaScript expression to match documents

### MongoDB Update Operators

#### Fields
      The following operators can be used to update fields:
            $currentDate: Sets the field value to the current date
            $inc: Increments the field value
            $rename: Renames the field
            $set: Sets the value of a field
            $unset: Removes the field from the document
            
#### Array
      The following operators assist with updating arrays.
            $addToSet: Adds distinct elements to an array
            $pop: Removes the first or last element of an array
            $pull: Removes all elements from an array that match the query
            $push: Adds an element to an array

### Aggregation Pipelines
* Aggregation operations allow you to group, sort, perform calculations, analyze data, and much more.
* Aggregation pipelines can have one or more "stages". The order of these stages are important. 
* Each stage acts upon the results of the previous stage.

        Example
        db.posts.aggregate([
          // Stage 1: Only find documents that have more than 1 like
          {
            $match: { likes: { $gt: 1 } }
          },
          // Stage 2: Group documents by category and sum each categories likes
          {
            $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
          }
        ])


#### Aggregation $group
    This aggregation stage groups documents by the unique _id expression provided.
    This will return the distinct values from the property_type field.
    
#### Aggregation $limit
    This aggregation stage limits the number of documents passed to the next stage.

#### Aggregation $project
    This aggregation stage passes only the specified fields along to the next aggregation stage.
    This will return the documents but only include the specified fields.

#### Aggregation $sort
    This aggregation stage groups sorts all documents in the specified sort order.
    
#### Aggregation $match
    This aggregation stage behaves like a find. It will filter documents that match the query provided.
    Using $match early in the pipeline can improve performance since it limits the number of documents the next stages must process.

#### Aggregation $addFields
    This aggregation stage adds new fields to documents.

#### Aggregation $count
    This aggregation stage counts the total amount of documents passed from the previous stage.

#### Aggregation $lookup
    This aggregation stage performs a left outer join to a collection in the same database.
    There are four required fields:
          from: The collection to use for lookup in the same database
          localField: The field in the primary collection that can be used as a unique identifier in the from collection.
          foreignField: The field in the from collection that can be used as a unique identifier in the primary collection.
          as: The name of the new field that will contain the matching documents from the from collection.

#### Aggregation $out
    This aggregation stage writes the returned documents from the aggregation pipeline to a collection.
    The $out stage must be the last stage of the aggregation pipeline.


### Indexing & Search
    To use our search index, we will use the $search operator in our aggregation pipeline.
          Example
          db.movies.aggregate([
            {
              $search: {
                index: "default", // optional unless you named your index something other than "default"
                text: {
                  query: "star wars",
                  path: "title"
                },
              },
            },
            {
              $project: {
                title: 1,
                year: 1,
              }
            }
          ])

### Schema Validation
    By default MongoDB has a flexible schema. This means that there is no strict schema validation set up initially.
    Schema validation rules can be created in order to ensure that all documents a collection share a similar structure.
    MongoDB supports JSON Schema validation. The $jsonSchema operator allows us to define our document structure.

          Example
          db.createCollection("posts", {
            validator: {
              $jsonSchema: {
                bsonType: "object",
                required: [ "title", "body" ],
                properties: {
                  title: {
                    bsonType: "string",
                    description: "Title of post - Required."
                  },
                  body: {
                    bsonType: "string",
                    description: "Body of post - Required."
                  },
                  category: {
                    bsonType: "string",
                    description: "Category of post - Optional."
                  },
                  likes: {
                    bsonType: "int",
                    description: "Post like count. Must be an integer - Optional."
                  },
                  tags: {
                    bsonType: ["string"],
                    description: "Must be an array of strings - Optional."
                  },
                  date: {
                    bsonType: "date",
                    description: "Must be a date - Optional."
                  }
                }
              }
            }
          })

### Data API

#### Find a Single Document
    Endpoint -: POST Base_URL/findOne
    The findOne endpoint is used to find a single document in a collection.
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "filter": <query filter>,
          "projection": <projection>
        }

#### Find Multiple Documents
    Endpoint -: POST Base_URL/find
    The find endpoint is used to find multiple documents in a collection.
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "filter": <query filter>,
          "projection": <projection>,
          "sort": <sort expression>,
          "limit": <number>,
          "skip": <number>
        }

#### Insert a Single Document
Endpoint -: POST Base_URL/insertOne
    The insertOne endpoint is used to insert a single document into a collection.
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "document": <document>
        }


#### Insert Multiple Documents
    Endpoint -: POST Base_URL/insertMany
    The insertMany endpoint is used to insert multiple documents into a collection.
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "documents": [<document>, <document>, ...]
        }

#### Update a Single Document
    Endpoint -:POST Base_URL/updateOne
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "filter": <query filter>,
          "update": <update expression>,
          "upsert": true|false
        }

#### Update Multiple Documents
    Endpoint -: POST Base_URL/updateMany
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "filter": <query filter>,
          "update": <update expression>,
          "upsert": true|false
        }

#### Delete a Single Document
    Endpoint -: POST Base_URL/deleteOne
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "filter": <query filter>
        }

#### Delete Multiple Documents
    Endpoint -: POST Base_URL/deleteMany
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "filter": <query filter>
        }

#### Aggregate Documents
    Endpoint -: POST Base_URL/aggregate
    Request Body
        Example
        {
          "dataSource": "<data source name>",
          "database": "<database name>",
          "collection": "<collection name>",
          "pipeline": [<pipeline expression>, ...]
        }



  
### MongoDB Drivers
    Python -:
        Use PyMongo for synchronous Python applications.
        Use Motor for asynchronous Python applications.
    
    Java -:
        Use the Java Driver for synchronous Java applications.
        Use the Reactive Streams Driver to use the Reactive Streams API for asynchronous stream processing.
  



