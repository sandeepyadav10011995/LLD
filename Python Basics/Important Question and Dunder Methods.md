## 𝐃𝐮𝐧𝐝𝐞𝐫 𝐦𝐞𝐭𝐡𝐨𝐝𝐬 𝐢𝐧 𝐏𝐲𝐭𝐡𝐨𝐧
    __call__ : makes an instance callable
    __init__ : called when an object is initialized
    __new__ : called when an object is created
    __repr__ : to represent an object
    __eq__ : to check equality of self and the object used with '=='
    __del__ : invoked during object deletion
    __str__ , __int__ , __float__ , __complex__ ,__bool__ : type conversion methods
    __add__ , __sub__ , __mul__ , __truediv__ : invoked during binary operations to perform respective operations (+ , - , *, /)
    __ne__ , __lt__ , __le__ , __gt__ , __ge__ : invoked during comparison operations to perform respective operations (!= , < , <=, >, >=)
    __radd__ , __rsub__ , __rmul__ , __rtruediv__ : reverse methods, called when left-side object doesn't have a method for binary operation
    __iadd__ , __isub__ , __imul__ , __itruediv__ : methods to perform in-place operations like +=, -=, *=



## Interviewer: What does ACID stands for?
__Candidate__: Atomicity, Consistency, Isolation and Durability

## Interviewer: Okay, so what is atomicity?
__Candidate__: It is the ability of a transaction to fail or pass completely without any intermittent stage. 
               When a transaction is initiated and some writes failed so the ability to successfully retry the whole 
               transaction is atomicity. Herein, we can consider that the transaction was aborted and no change happened at all.

## Is atomicity related to concurrency?
-> __No__, it is not about concurrency.
-> That is covered under __Isolation__, I in ACID properties.

## Interviewer: What is a transaction in database?
__Candidate__: Transaction is a logical unit to group multiple reads and writes together in one operation.

## What does 𝗜𝘀𝗼𝗹𝗮𝘁𝗶𝗼𝗻 means in 𝑨𝑪𝑰𝑫 properties of a database?
𝑨𝑪𝑰𝑫 => 𝗔𝘁𝗼𝗺𝗶𝗰𝗶𝘁𝘆, 𝗖𝗼𝗻𝘀𝗶𝘀𝘁𝗲𝗻𝗰𝘆, 𝗜𝘀𝗼𝗹𝗮𝘁𝗶𝗼𝗻 𝗮𝗻𝗱 𝗗𝘂𝗿𝗮𝗯𝗶𝗹𝗶𝘁𝘆
𝐈𝐬𝐨𝐥𝐚𝐭𝐢𝐨𝐧: It means that the transactions will have isolated operations and if two transactions are being carried out at same time 
then neither will hinder the other's read/write operations. If they do, then race conditions occur.
𝑊ℎ𝑒𝑛 𝑐𝑙𝑖𝑒𝑛𝑡𝑠 𝑡𝑟𝑦 𝑡𝑜 𝑎𝑐𝑐𝑒𝑠𝑠 𝑠𝑎𝑚𝑒 𝑟𝑒𝑐𝑜𝑟𝑑𝑠 𝑖𝑛 𝑑𝑎𝑡𝑎𝑏𝑎𝑠𝑒, 𝑐𝑜𝑛𝑐𝑢𝑟𝑟𝑒𝑛𝑐𝑦 𝑖𝑠𝑠𝑢𝑒𝑠 𝑎.𝑘.𝑎. 𝑟𝑎𝑐𝑒 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑠 𝑐𝑎𝑛 𝑜𝑐𝑐𝑢𝑟.

## There are two ways to allocate memory in Python:
    1.) 𝑆𝑡𝑎𝑐𝑘 𝑀𝑒𝑚𝑜𝑟𝑦
    2.) 𝐻𝑒𝑎𝑝 𝑀𝑒𝑚𝑜𝑟𝑦

    𝘽𝙖𝙨𝙞𝙘 𝙙𝙞𝙛𝙛𝙚𝙧𝙚𝙣𝙘𝙚:
    𝑆𝑡𝑎𝑐𝑘 𝑀𝑒𝑚𝑜𝑟𝑦 -> used to store method calls and local variables
    𝐻𝑒𝑎𝑝 𝑀𝑒𝑚𝑜𝑟𝑦 -> used to store global variables

    𝙒𝙝𝙖𝙩'𝙨 𝙞𝙣 𝙩𝙝𝙚 𝙣𝙖𝙢𝙚?
    𝑆𝑡𝑎𝑐𝑘 𝑀𝑒𝑚𝑜𝑟𝑦 -> contiguous block of memory handled by compiler using predefined routines
    𝐻𝑒𝑎𝑝 𝑀𝑒𝑚𝑜𝑟𝑦 -> it is not heap data structure rather a pile of memory space

    𝙋𝙧𝙤𝙜𝙧𝙖𝙢𝙢𝙚𝙧'𝙨 𝙪𝙨𝙖𝙜𝙚:
    𝑆𝑡𝑎𝑐𝑘 𝑀𝑒𝑚𝑜𝑟𝑦 -> need not to be handled by programmers
    𝐻𝑒𝑎𝑝 𝑀𝑒𝑚𝑜𝑟𝑦 -> can be used by programmers to allocate and de-allocate



