#### SHARDING

	Data divide into multiple DB (equal distribution but maintaiance could be an issue when introducing new db server so we use consistent 
	hashing rather than a simple mod.

	* SQL Joins are expensive (could use nosql if permits)
	* NoSQL has built for sharding already, but for SQL you need to define alag se
	* Trade off b/w Consistency vs Availibility (Twitter/ fb choose Availibility where as Banking uses Consistency) in case of data replication b/w 
	   several db nodes of replicas
	* To maintain consistentcy b/w db nodes - 3 Phase commit is better (Prepare, Pre Commit, Commit), so if orchestrator (master)dies, a node will 
	  check of any other node is in pre commit phase, otherwise the commit will br aborted

### Event Driven Info
* Kafka is industry standard for queue - Have high throughput (more number of msg can be passed fastly)
* Pub Sub Model benefits - Consumer can operate by it's capacity (leaky bucket algo - flash sale), Event Driven

* Rate Limiting - Limiting no. of request per user for a specific time


###### Timeline Generation - Hybrid Model 
* __Push__ - for normal users (not many followers) - push (append) their tweets to their follower's timeline data
* __Pull__ - for celebrities (many followers) - place the tweet in cache too and whenever a follower open's timeline we'll pull data from 
       cache too plus it's timeline data

##### Some Important Rules
* 80-20 rule - 20% request bring 80% of traffic so we'll put that data in cache
* LRU Cache - Remove the least recently used one to put new data in cache
	
#### Google Maps
* Any Nearby Usecase - ola, swiggy, nearbuy, etc - We use Google's S2 API
    Google Maps has divided whole world into cells/tiles and with each zoom level you can see 2**(zoom_level*2) tiles . So you need to pass the 
    user location , zoom level and radius to S2 to get all the nearby data (cell IDs) - it has total 21 zoom levels

* Master Slave Architectue - Master will handle writes, slave will handle reads
* Gossip Protocol - DB servers (sharded) tell each other the range of data they are storing through this (Used in Uber)


* Bloom Filter - to check if any data is preexisted in DB (used in web crawler to see if we have saved a URL or to check whether we have that 
    name as username in DB) - Apply multiple hashing to a string and for each hash value make true a bit in the array https://youtu.be/XbXL9ijDJpo?t=2708


#### API Protocols

* HTTP Long Polling is a technique used to push information to a client as soon as possible on the server. In Long Polling, the server does not close the connection once it receives a request from the client. Instead, the server responds only if any new message is available or if a timeout threshold is reached.
* Web Sockets - Persistent and dedicated connection and bidirectional comm (for chat system, gaming, stocks)
* XMPP - Extensible Messaging and Presence Protocol is an open communication protocol designed for instant messaging, presence information, and contact list maintenance. Based on XML, it enables the near-real-time exchange of structured data between two or more network entities (for chats) (in python u can install ejabberd)

#### Proxies
	
	* Collapsed forwarding - Proxies can combine the same data access requests into one request and then return the result to the user; 
	    this technique is called collapsed forwarding. Consider a request for the same data across several nodes, but the data is not in cache. 
	    By routing these requests through the proxy, they can be consolidated into one so that we will only read data from the disk once.
	* forward proxy -  hides the identity of the client
	* everse proxy - conceals the identity of the server

#### CAP Theorem
* CAP theorem  - states that it is impossible for a distributed system to simultaneously provide all three of the following desirable properties Consistency ( C ), Availability ( A ), Partition tolerance ( P ), any distributed system needs to pick two out of the three properties
* Partition tolerance ( P ): A partition is a communication break (or a network failure) between any two nodes in the system, i.e., both nodes are up but cannot communicate with each other. A partition-tolerant system continues to operate even if there are partitions in the system. Such a system can sustain any network failure that does not result in the failure of the entire network. Data is sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.
* The PACELC theorem states that in a system that replicates data:
	if there is a partition (‘P’), a distributed system can tradeoff between availability and consistency (i.e., ‘A’ and ‘C’);
	else (‘E’), when the system is running normally in the absence of partitions, the system can tradeoff between latency (‘L’) and consistency (‘C’).

* MongoDB -  in the case of a network partition, MongoDB chooses availability, but otherwise guarantees consistency

* Server-Sent Events (SSEs) - Under SSEs the client establishes a persistent and long-term connection with the server. The server uses this 
 connection to send data to a client. If the client wants to send data to the server, it would require the use of another technology/protocol 
 to do so . SSEs are best when we need real-time traffic from the server to the client or if the server is generating data in a loop and will 
 be sending multiple events to the client.
* Quorum - In a distributed environment, a quorum is the minimum number of servers on which a distributed operation needs to be performed successfully before declaring the operation’s overall success. 
* What value should we choose for a quorum? --> More than half of the number of nodes in the cluster
* Master - Slave -  Problem - using quorum can lead to another problem, that is, lower availability; at any time, the system needs to ensure 
 that at least a majority of replicas are up and available, otherwise the operation will fail. Quorum is also not sufficient, as in certain 
 failure scenarios, the client can still see inconsistent data.
 Solution by master-slave - Allow only a single server (called leader) to be responsible for data replication and to coordinate work.


#### PROGRAM VS PROCESS VS THREAD
* __PROGRAM__ -: A program is an executable file which consists of a set of instructions to perform some task and is usually stored on the disk of your computer.
* __PROCESS__ -: A process is what we call a program that has been loaded into memory along with all the resources it needs to operate. It has its own memory space.
* __THREAD__ -: A thread is the unit of execution within a process. A process can have multiple threads running as a part of it, where each thread uses the process’s memory space and shares it with other threads.

##### Multithreading -: 
It is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one 
after the other. This gives you the illusion that the threads are running in parallel, but they are actually run in a 
concurrent manner. In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.
##### Multiprocessing -: 
It is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple CPU cores, 
which do not share the resources among them. Each process can have many threads running in its own memory space. 
In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.



#### HTTP Info
* HTTP CODES -: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
		Informational responses (100 – 199)
		Successful responses (200 – 299)
		Redirection messages (300 – 399)
		Client error responses (400 – 499)
		Server error responses (500 – 599)

#### Security
* SECURITY -: https://www.okta.com/resources/whitepaper/8-ways-to-secure-your-microservices-architecture/
		1. Make your microservices architecture secure by design
		2. Scan for dependencies
		3. Use HTTPS everywhere
		4. Use access and identity tokens 
		5. Encrypt and protect secrets
		6. Slow down attackers
		7. Know your cloud and cluster security
		8. Cover your security bases

* JWT VS OAUTH -: https://stackoverflow.com/questions/39909419/what-are-the-main-differences-between-jwt-and-oauth-authentication

JWT (JSON Web Tokens)- It is just a token format. JWT tokens are JSON encoded data structures contains information about issuer, subject 
                      (claims), expiration time etc. It is signed for tamper proof and authenticity and it can be encrypted to protect the 
		      token information using symmetric or asymmetric approach. JWT is simpler than SAML 1.1/2.0 and supported by all devices 
		      and it is more powerful than SWT(Simple Web Token).

OAuth2 - OAuth2 solve a problem that user wants to access the data using client software like browse based web apps, native mobile apps or 
         desktop apps. OAuth2 is just for authorization, client software can be authorized to access the resources on-behalf of end user using 
	 access token. OAuth 2.0 is protocol for authorization.

OpenID Connect - OpenID Connect builds on top of OAuth2 and add authentication. OpenID Connect add some constraint to OAuth2 like UserInfo 
                 Endpoint, ID Token, discovery and dynamic registration of OpenID Connect providers and session management. 
		 JWT is the mandatory format for the token.

CSRF protection - You don't need implement the CSRF protection if you do not store token in the browser's cookie.


#### 

KONG -: Kong is an open source API gateway and platform that acts as middleware between compute clients and the API-centric applications. 
        The platform easily extends the capabilities of APIs with the use of plugins.
	Kong provides different ways of load balancing requests to multiple services - 
	  - DNS-based method - A DNS-based method will configure a domain in DNS in such a manner that the user requests to the domain are 
	                       distributed among a group of services.
	  - round-robin method and a 
	  - hash-based balancing method. 

* In general, ZooKeeper provides an in-sync view of the Kafka cluster.
  ZooKeeper is an open source Apache project that provides a centralized service for providing configuration information, naming, 
  synchronization and group services over large clusters in distributed systems. The goal is to make these systems easier to manage with 
  improved, more reliable propagation of changes.
  ZooKeeper is a system that helps application developers build coordination services through its client API. 
  ZooKeeper's client API combines components from distributed lock services, shared registers, and group messaging into a replicated centralized coordination service.
  
  
  
  
  
