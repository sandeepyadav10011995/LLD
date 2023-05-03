# Microservice Architecture

## Why Microservices Architecture is needed ?
**Monolith or Legacy System Disadavantages -:**
* Overload IDE
* Scalaing is HARD -: As Continuous Integration(CI) Jobs needs to be fast which is not the case in Monolith.
* Tightly coupled
* Deployment Time -: Takes more time for deployment of another box to become hot.
* Lets say I need to increase the capacity of one module1 then I will have to scale all the modules by bringing another box up (Entire application)

**Microservices ~ Disadavantges -: "__As there is nothing as such as FREE LUNCH__"**
* Should be loosely coupled -: Will increase the latency in some cases.
* SLA's needs to monitored and handled -: Makes Debugging HARD.
* Transaction Management -: HARD -: Solution is SAGA Pattern

## DIFFERENT PHASES OF Microservices

#### 1. DECOMPOSITION
* __By Business Capabilty__
   * __Example -: Online Order__
   * Order Management
   * Product Management
   * Account Management
   * Billing Management
   * Payment Management 

* __By Sub-Domain (DDD Domain Driven Design)__
   * __Example -: Online Order__
   * Lets say Order Management is one Domain
   * Payments -: Services within this
      * Forward Payment
      * Reverse Payment
      * Invoice Generation

#### 2. DATABASE
* __Shared Database__
* __Specific Database__

#### 3. COMMUNICATION
* __API's__
* __EVENTS__

#### 4. INTEGRATION
* __API Gateways__

#### 5. DEPLOYMENT

#### 6. OBSERVABILITY
* __Monitoring__

## Pattern Used to Convert Monolith to Microservices -: STRANGLER ~ GHOONTNA
<img width="331" alt="Screenshot 2023-05-03 at 8 14 30 PM" src="https://user-images.githubusercontent.com/22426280/235951300-1993bdb2-d384-4699-832c-143c02ff1770.png">


## Microservices
* Microservices architecture is an approach to building software systems as a collection of small, independent, and loosely coupled services that communicate with each other through APIs. 
* Each service is responsible for a specific business capability, and can be developed, deployed, and scaled independently of other services.

* __Here are some common patterns and best practices in microservices architecture:__

1. __Single Responsibility Principle__: 
    * Each microservice should have a single responsibility or business capability, and should not be responsible for more than one thing. 
    * This allows for better separation of concerns and helps to keep services small and manageable.

2. __API Gateway__: 
    * An API Gateway is a service that sits between clients and the microservices, and acts as a reverse proxy, routing requests to the appropriate service. 
    * It also provides features such as authentication, rate limiting, and caching.

3. __Service Registry and Discovery__: 
    * A Service Registry is a database that contains information about the microservices, such as their network location and API endpoints. 
    * A Service Discovery mechanism allows microservices to dynamically locate and communicate with other services.

4. __Event-Driven Architecture__: 
    * An event-driven architecture involves using events to trigger and communicate between microservices. 
    * Events can be used to notify other services about changes or updates, or to trigger background tasks.

5. __Resilience Patterns__: 
    * Resilience patterns such as Circuit Breakers, Retries, and Timeouts can be used to improve the robustness and fault-tolerance of microservices.

6. __Continuous Delivery__: 
    * Continuous Delivery is a software development practice that emphasizes rapid and frequent delivery of new software features and improvements. 
    * It requires automated testing, deployment, and monitoring to ensure that changes can be quickly and safely deployed to production.

7. __Containerization and Orchestration__: 
    * Containerization technologies such as Docker allow for easy packaging and deployment of microservices. 
    * Orchestration tools such as Kubernetes can be used to manage and scale the containers in a distributed environment.

**By following these patterns and best practices, microservices architecture can provide a number of benefits such as scalability, resilience, flexibility, and agility.**

## SAGA Pattern -: Sequence of Local Transactions
* Used for Data Management in Microservices
  * Shared Database -> Common ACID Transactions
    * Scaling issues -: Not Good w.r.t to this
    * Modifying columns details (Delete) 
  * Easy when dealing with transactions
  * <img width="382" alt="Screenshot 2023-05-03 at 8 24 44 PM" src="https://user-images.githubusercontent.com/22426280/235954462-b805647e-06f5-4748-bef8-2c50f7153172.png">
  * Database for each service
  * <img width="448" alt="Screenshot 2023-05-03 at 8 33 57 PM" src="https://user-images.githubusercontent.com/22426280/235957112-3d5d0781-a690-41f6-866b-d7e084a3df96.png">
   
**There are two ways of coordination sagas:**
#### Choreography - each local transaction publishes domain events that trigger local transactions in other services
    An e-commerce application that uses this approach would create an order using a choreography-based saga that consists of the following steps:
      1. The Order Service receives the POST /orders request and creates an Order in a PENDING state
      2. It then emits an Order Created event
      3. The Customer Service’s event handler attempts to reserve credit
      4. It then emits an event indicating the outcome
      5. The OrderService’s event handler either approves or rejects the Order
  <img width="404" alt="Screenshot 2023-05-03 at 8 41 40 PM" src="https://user-images.githubusercontent.com/22426280/235959230-828969cf-6224-428c-9d3f-2ad1404a6209.png">

#### Orchestration - an orchestrator (object) tells the participants what local transactions to execute
     An e-commerce application that uses this approach would create an order using an orchestration-based saga that consists of the following steps:
       1. The Order Service receives the POST /orders request and creates the Create Order saga orchestrator
       2. The saga orchestrator creates an Order in the PENDING state
       3. It then sends a Reserve Credit command to the Customer Service
       4. The Customer Service attempts to reserve credit
       5. It then sends back a reply message indicating the outcome
       6. The saga orchestrator either approves or rejects the Order
  <img width="474" alt="Screenshot 2023-05-03 at 8 45 18 PM" src="https://user-images.githubusercontent.com/22426280/235960240-102fff65-a5a5-4449-976d-da436e0c799c.png">

Website Link -: https://microservices.io/patterns/data/saga.html


