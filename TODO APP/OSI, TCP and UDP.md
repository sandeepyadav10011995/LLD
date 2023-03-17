![OSI Model](https://user-images.githubusercontent.com/22426280/225791922-6dbad638-0a5a-47c6-9bb2-f1d9d1480387.png)

Features -:
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
      
      
      
      
