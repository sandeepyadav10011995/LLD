Kafka and RabbitMQ are both messaging systems that are commonly used in modern distributed systems. While they share 
some similarities, they differ in several ways.


RabbitMQ : prefetch simply controls how many messsages the broker allows to be outstanding at the consumer at a time.

1.  Architecture:
    *   Kafka is a distributed streaming platform, which means that it is designed to handle high-throughput, 
        low-latency data streams. It is built on a pub-sub model and provides durable, fault-tolerant messaging between 
        producers and consumers.
    *   RabbitMQ, on the other hand, is a message broker that implements the Advanced Message Queuing Protocol (AMQP) 
        and is based on a message queue model. It supports a variety of messaging patterns, including point-to-point, 
        publish/subscribe, and request/response.

2.  Scalability:
    *   Kafka is designed to be highly scalable and can handle millions of messages per second. It achieves this by 
        leveraging a distributed architecture that allows it to spread the load across multiple nodes.
    *   RabbitMQ is also scalable, but it is more limited in terms of the number of messages it can handle per second. 
        This is because RabbitMQ relies on a centralized broker that can become a bottleneck as the number of messages 
        increases.

3.  Persistence:
    *   Kafka is designed to store messages in a distributed, fault-tolerant manner. This means that messages are stored 
        in multiple nodes, which makes them highly available in the event of a node failure.
    *   RabbitMQ also supports persistence, but it stores messages on disk rather than in memory. This means that 
        RabbitMQ can handle larger volumes of messages, but it can also be slower than Kafka when it comes to message 
        processing.

4.  Use cases:
    *   Kafka is often used in real-time streaming applications that require low latency and high throughput, such as 
        log aggregation, data analytics, and event processing.
    *   RabbitMQ is often used in more traditional enterprise applications that require reliable messaging, such as 
        order processing, payment processing, and message routing.

In summary, both Kafka and RabbitMQ are powerful messaging systems that can be used in a variety of distributed 
applications. 
    *   Kafka is better suited for real-time streaming applications that require high throughput and low latency. 
    *   RabbitMQ is better suited for traditional enterprise applications that require reliable messaging.
    
https://www.cloudamqp.com/blog/when-to-use-rabbitmq-or-apache-kafka.html
