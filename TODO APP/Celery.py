"""
Task queues are used as a mechanism to distribute work across threads or machines.
    * A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues
      for new work to perform.
    * Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a
      task the client adds a message to the queue, the broker then delivers that message to a worker.
    * A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal
      scaling.

Celery -:
* Simple - Celery is easy to use and maintain, and it doesn’t need configuration files.
    from celery import Celery
    app = Celery('hello', broker='amqp://guest@localhost//')

    @app.task
    def hello():
        return 'hello world'

* Highly Available -: Workers and clients will automatically retry in the event of connection loss or failure, and some
                      brokers support HA in way of Primary/Primary or Primary/Replica replication.
* Fast -: A single Celery process can process millions of tasks a minute, with sub-millisecond round-trip latency
          (using RabbitMQ, librabbitmq, and optimized settings).
* Flexible -: Almost every part of Celery can be extended or used on its own, Custom pool implementations, serializers,
              compression schemes, logging, schedulers, consumers, producers, broker transports, and much more.


It supports

* Brokers -: RabbitMQ, Redis, Amazon SQS, and more…

* Concurrency -: prefork (multiprocessing), Eventlet, gevent, thread (multithreaded), solo (single threaded)

* Result Stores -:  AMQP, Redis, Memcached, SQLAlchemy, Django ORM, Apache Cassandra, Elasticsearch, Riak, MongoDB,
                    CouchDB, Couchbase, ArangoDB, Amazon DynamoDB, Amazon S3, Microsoft Azure Block Blob,
                    Microsoft Azure Cosmos DB, File system
* Serialization -: pickle, json, yaml, msgpack. zlib, bzip2 compression. Cryptographic message signing.


The Primitives -: 
group -: The group primitive is a signature that takes a list of tasks that should be applied in parallel.

chain -: The chain primitive lets us link together signatures so that one is called after the other, essentially forming
         a chain of callbacks.

chord -: A chord is just like a group but with a callback. A chord consists of a header group and a body, where the body
         is a task that should execute after all of the tasks in the header are complete.

map -:
"""
