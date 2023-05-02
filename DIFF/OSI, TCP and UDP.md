## OSI Model

![OSI Model](https://user-images.githubusercontent.com/22426280/225791922-6dbad638-0a5a-47c6-9bb2-f1d9d1480387.png)

## Features -:
    
    Connection status -:
          TCP: Requires an established connection to transmit data (connection should be closed once transmission is complete)

          UDP: Connectionless protocol with no requirements for opening, maintaining, or terminating a connection

    Data sequencing-:
          TCP: Able to sequence

          UDP: Unable to sequence

    Guaranteed delivery -:
          TCP: Can guarantee delivery of data to the destination router

          UDP: Cannot guarantee delivery of data to the destination

    Retransmission of data -:
          TCP: Retransmission of lost packets is possible

          UDP: No retransmission of lost packets

    Error checking-:
          TCP: Extensive error checking and acknowledgment of data

          UDP: Basic error checking mechanism using checksums

    Method of transfer -: 
          TCP: Data is read as a byte stream; messages are transmitted to segment boundaries

          UDP: UDP packets with defined boundaries; sent individually and checked for integrity on arrival

    Speed -:
          TCP: Slower than UDP

          UDP: Faster than TCP

    Broadcasting -:
          TCP: Does not support Broadcasting

          UDP: Does support Broadcasting

    Optimal use -:
          TCP: Used by HTTPS, HTTP, SMTP, POP, FTP, etc

          UDP: Video conferencing, streaming, DNS, VoIP, etc
      
## Analogy -:
TCP and UDP are both ways that computers can send information to each other over the internet, but they work in different ways.

TCP is like sending a package through the mail with a tracking number. When you send a package with a tracking number, you know exactly when it's been sent, when it's been received, and if there were any problems along the way. TCP works in a similar way by making sure that every piece of information that's sent between computers is checked to make sure it gets there safely and in the right order. This is great for things like emails or web pages where you want to make sure all the information arrives intact.

UDP, on the other hand, is like sending a postcard through the mail without any tracking number. You don't know if the postcard gets lost, and you don't know if it arrives out of order. UDP doesn't check to make sure that every piece of information is received correctly, so it's faster than TCP. This is great for things like online gaming, where speed is more important than making sure every piece of information is received.

So, TCP is like sending a package with a tracking number to make sure everything arrives safely, and UDP is like sending a postcard without tracking to get there faster, but you don't know if it got there in one piece.
      
      
