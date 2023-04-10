# SWIFT payment messaging system
* The __Society for Worldwide Interbank Financial Telecommunication__ (SWIFT) is the main secure messaging system that links the world’s banks.
* The __Belgium-based system__ is run by its member banks and handles millions of payment messages per day. The diagram below illustrates how 
  payment messages are transmitted from Bank A (in New York) to Bank B (in London). 

## Steps -:
__Step 1__: Bank A sends a message with transfer details to Regional Processor A in New York. The destination is Bank B.

__Step 2__: Regional processor validates the format and sends it to Slice Processor A. The Regional Processor is responsible for input message validation and output message queuing. The Slice Processor is responsible for storing and routing messages safely.

__Step 3__: Slice Processor A stores the message.

__Step 4__: Slice Processor A informs Regional Processor A the message is stored.

__Step 5__: Regional Processor A sends ACK/NAK to Bank A. ACK means a message will be sent to Bank B. NAK means the message will NOT be sent to Bank B.

__Step 6__: Slice Processor A sends the message to Regional Processor B in London.

![image](https://user-images.githubusercontent.com/22426280/230946533-d4a0be73-984f-46de-8cba-ae1969bc4ddc.png)

__Step 7__: Regional Processor B stores the message temporarily.

__Step 8__: Regional Processor B assigns a unique ID MON (Message Output Number) to the message and sends it to Slice Processor B

__Step 9__: Slice Processor B validates MON.

__Step 10__: Slice Processor B authorizes Regional Processor B to send the message to Bank B.

__Step 11__: Regional Processor B sends the message to Bank B.

__Step 12__: Bank B receives the message and stores it.

__Step 13__: Bank B sends UAK/UNK to Regional Processor B. UAK (user positive acknowledgment) means Bank B received the message without error; UNK (user negative acknowledgment) means Bank B received checksum failure.

__Step 14__: Regional Processor B creates a report based on Bank B’s response, and sends it to Slice Processor B.

__Step 15__: Slice Processor B stores the report.

__Step 16 - 17__: Slice Processor B sends a copy of the report to Slice Processor A. Slice Processor A stores the report.
