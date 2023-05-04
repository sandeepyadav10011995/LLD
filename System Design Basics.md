## Understanding the Basics of System Design

### a. Key concepts and principles

##### Scalability
* The ability of a system to handle increasing amounts of load or traffic. 
* It’s important to understand different scalability approaches such as horizontal scaling (adding more machines to a system) and vertical scaling (adding more resources to a single machine).

##### Fault tolerance
* The ability of a system to continue functioning despite the failure of one or more of its components. 
* Techniques such as redundancy and load balancing can help increase a system’s fault tolerance.

##### Load balancing
* Load balancers distribute workloads across multiple machines in order to optimize resource usage and ensure that no single machine is overwhelmed.

##### Caching
* Storing frequently accessed data in a high-speed storage layer to reduce the load on the underlying data store and improve system performance.

##### Availability
* The ability of a system to respond to requests in a timely manner. 
* This is closely related to fault tolerance and is typically measured as a percentage of time that the system is operational.

##### Consistency
* The degree to which all nodes in a distributed system see the same data at the same time. 
* Consistency can be divided into different levels, such as strong consistency, eventual consistency, and no consistency.

##### Latency
* The time it takes for a request to be processed and a response to be returned. 
* Latency is an important factor in system design, particularly for systems that handle real-time data.

##### Throughput
* The number of requests a system can handle per unit of time. 
* Throughput is closely related to scalability and is often used as a measure of a system’s performance.

##### Partition Tolerance
* The ability of a system to continue functioning when network partitions occur. 
* In distributed systems, it’s impossible to have both consistency and partition tolerance at the same time, so a designer must decide which one is more important for the use case.

##### CAP Theorem
* The theorem states that it is impossible for a distributed system to simultaneously provide all three of the following guarantees: 
  * Consistency
  * Availability, and 
  * Partition Tolerance.

##### ACID Properties
* A set of properties that guarantee that database transactions are processed reliably. 
* The acronym stands for Atomicity, Consistency, Isolation, and Durability.

I**t’s important to be familiar with these concepts and understand how they apply to different types of systems.** 
* For example, a real-time financial trading system would need to have a high level of consistency and low latency. 
* While a social media platform might prioritize high availability and partition tolerance over consistency

### b. Common design patterns:

##### Microservices
* It is a software architecture pattern in which an application is broken down into a collection of small, independent services that communicate with each other over a network. 
* Each service is responsible for a specific functionality and is developed, deployed, and scaled independently. 
* Microservices offer several benefits, such as increased scalability, improved fault tolerance, and faster deployment cycles. 
* However, they also introduce additional complexity, such as the need for service discovery and inter-service communication.

##### Event sourcing
* Event sourcing is a pattern in which the state of an application is represented as a stream of events, rather than a snapshot of its current state. 
* This pattern is often used in systems that need to handle a large number of concurrent updates, such as financial systems and gaming platforms. 
* Event sourcing allows for easy replay of events, which can be useful for debugging and auditing. 
* However, it also requires additional storage and computational resources to maintain the event stream.

##### Sharding
* Sharding is a technique for horizontally partitioning data across multiple machines in order to improve scalability and performance. 
* In a sharded system, each machine is responsible for a specific subset of the data, and queries are routed to the appropriate machine based on the data’s partition key. 
* Sharding can be used to distribute the load on a system, improve read and write performance, and increase the overall capacity of a system. 
* However, it also introduces additional complexity, such as the need for consistent hashing, data replication, and partition-aware clients

##### CQRS (Command Query Responsibility Segregation)
* CQRS is a pattern that separates the read and write operations of a system into separate models, allowing for optimized performance and scalability. 
* This pattern can be useful in systems that handle a high volume of read and write operations, such as e-commerce websites. 
* CQRS allows for different data stores and caching strategies to be used for read and write operations, improving the performance of both. 
* However, it also requires more complex design and more effort to maintain two separate models of the data.

##### Reverse proxy
* A reverse proxy is a server that sits in front of one or more web servers and forwards client requests to the appropriate server. 
* It can be used to improve security, performance, and scalability of a system. 
* It can also be used to provide additional functionality such as SSL termination, caching, and compression.
![image](https://user-images.githubusercontent.com/22426280/236138231-e53b0e68-f935-4af6-90b4-302146c4dbef.png)

##### Circuit Breaker
* A Circuit breaker is a design pattern that can be used to prevent cascading failures in a distributed system. 
* It works by monitoring the health of a service and, when it detects an issue, it “trips” and prevents further requests from being sent to that service. 
* This helps to prevent a single point of failure from bringing down the entire system.

##### Backpressure
* Backpressure is a technique used to control the rate at which data is processed in a system, preventing it from being overwhelmed. 
* This can be done by buffering incoming data and only processing it at a specific rate, or by rejecting incoming data if the system is unable to handle it.

##### Object Pool
* An object pool is a design pattern that is used to improve the performance of a system by reusing objects, rather than creating new ones. 
* Object pools are often used to manage the lifecycle of expensive resources, such as database connections or threads.

### c. Familiarity with different types of databases

##### Relational databases
* Relational databases are the most common type of database and store data in tables, using SQL (Structured Query Language) for querying and manipulating that data. 
* They are based on the relational model, which organizes data into one or more tables, with each table consisting of rows and columns. 
* Popular examples of relational databases include __MySQL, PostgreSQL, and Oracle__.

##### NoSQL databases
* NoSQL databases, also known as “not only SQL” databases, do not use a fixed schema and are optimized for handling large amounts of unstructured data. 
* They are designed to handle the scale and performance requirements of modern web and mobile applications. 
* NoSQL databases can be classified into different types, such as document databases, key-value stores, graph databases, and column-family stores. 
* Popular examples of NoSQL databases include __MongoDB, Cassandra, and Redis__.

##### Distributed key-value stores
* Distributed key-value stores are a type of NoSQL database that stores data as key-value pairs and is designed for horizontal scalability. 
* They are often used as a caching layer or to store session data. 
* Popular examples of distributed key-value stores include __Riak and Redis__.

##### Document databases
* Document databases store data as semi-structured documents, such as JSON or XML, and are optimized for storing and querying large amounts of data. 
* They are often used for applications that require flexible data modeling and rich querying capabilities. 
* Popular examples of document databases include __MongoDB and Couchbase__.

##### Graph databases
* Graph databases are optimized for storing and querying data with complex relationships. 
* They store data as nodes and edges, rather than tables and rows, and are often used for applications that involve social networking, recommendation systems, and fraud detection.
* Popular examples of graph databases include __Neo4j and JanusGraph__.

##### Time-series databases
* Time-series databases are optimized for storing and querying time-stamped data. 
* They are often used for applications that involve monitoring, IoT, and financial data. 
* Popular examples of time-series databases include __InfluxDB, OpenTSDB, and Prometheus__.

Types of NoSQL databases

### d. Familiarity with different types of distributed systems and algorithms.

##### Merkle Tree

##### Consistent Hashing

##### Read Repair

##### Gossip Protocol

##### Bloom Filter

##### Heartbeat

##### CAP and PACELC Theorems
![image](https://user-images.githubusercontent.com/22426280/236139568-f43bce63-a43d-4c75-be7e-6d58e77c2536.png)

######  What is missing in the CAP theorem?**
* We cannot avoid partition in a distributed system; therefore, as stated above, according to the CAP theorem, a distributed system should choose between consistency or availability
  * __ACID (Atomicity, Consistency, Isolation, Durability)__ databases, such as RDBMSs like MySQL, Oracle, and Microsoft SQL Server, chose consistency (refuse response if it cannot check with peers).
  * In contrast, __BASE (Basically Available, Soft-state, Eventually consistent)__ databases, such as NoSQL databases like MongoDB, Cassandra, and Redis, chose availability (respond with local data without ensuring it is the latest with its peers).

###### One place where the CAP theorem is silent is what happens when there is no network partition? What choices does a distributed system have when there is no partition?
**PACELC theorem to the rescue**

![image](https://user-images.githubusercontent.com/22426280/236140485-1358daf0-a465-4dfd-a85c-afa7eadb7eeb.png)

* The first part of the theorem (PAC) is the same as the CAP theorem, and the ELC is the extension. 
* The whole thesis assumes we maintain high availability by replication. So, when there is a failure, CAP theorem prevails. 
* But if not, we still have to consider the tradeoff between consistency and latency of a replicated system.
* Examples
  * __Dynamo and Cassandra are PA/EL systems__: They choose availability over consistency when a partition occurs; otherwise, they choose lower latency.
  * __BigTable and HBase are PC/EC systems__: They will always choose consistency, giving up availability and lower latency.
  * __MongoDB can be considered PA/EC (default configuration)__: MongoDB works in a primary/secondaries configuration. 
    * In the default configuration, all writes and reads are performed on the primary. 
    * As all replication is done asynchronously (from primary to secondaries), when there is a network partition in which primary is lost or becomes isolated on the minority side, there is a chance of losing data that is unreplicated to secondaries, hence there is a loss of consistency during partitions. 
    * Therefore, it can be concluded that in the case of a network partition, MongoDB chooses availability but otherwise guarantees consistency. 
    * Alternately, when MongoDB is configured to write on majority replicas and read from the primary, it could be categorized as PC/EC.









