"""
A Socket is a network connection endpoint.

So whenever our web browser requests the web page, for example -: google.com
Then our web browser creates a socket and instructs it to connect to the web server hosting the python website,
where the web server is also listening on a socket for incoming requests.

The two sides use the sockets to send messages and data back and forth.
When in use, each socket is bound to a particular IP Address and port.

IP Address : It is a sequence of four numbers in the range of 0 to 255;
Port : It ranges from 0 to 65535.
      - Ports less than 1024 --> RESERVED for well known networking services.
          - 80 --> Used by HTTP
          - 443 --> Used by HTTPS
      - The maximum reserved value is stored in the socket module's IPPORT_RESERVED variable.

Note -: We can use other port numbers for our own programs.

SPECIAL ADDRESS: 127.0.0.1 also known as localhost; it refers to the current machine/computer.
                 Programs can use this address to connect to other programs running on the same machine.

DOMAIN NAME SERVERS (DNS) : Remembering more than a handful of IP addresses can be tedious, so we can also pay a small
                            fee and register a host name or domain name for a particular address. DNS handles the task
                            of mapping the names to a particular IP addresses.

TCP and UDP Protocols

When sending a messages between two programs of your own, we usually choose between the TCP and UDP Protocols.

------------------SERVER----------------------------       -------------------------CLIENT-----------------------
SOCKET OBJECT:                                             SOCKET OBJECT:
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)       s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Note-: AF_INET --> Signifies IPV4 Addresses
       SOCK_STREAM --> Signifies TCP Protocol

SOCKET BIND:                                               CONNECT:
s.bind((host, port))                                       s.connect((host, port))

SOCKET LISTEN:
s.listen(<max_incoming_connections>)

WAITING FOR CONNECTION (**BLOCKING CALL**):
conn, addr = s.accept()

COMMUNICATION:                                             COMMUNICATION:
conn.recv and conn.send                                    s.recv and s.send

CLOSE CONNECTION/CONNECTIONS:                                          CLOSE CONNECTION:
conn.close                                                 s.close


Python Example-:

"""
# server.py

import socket

def server():
    host = "localhost"
    port = 23456
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    while True:
        print("Waiting for connection !!")
        conn, addr = s.accept()
        print(f"Connected from {addr}")
        print(conn)
        while True:
            data = conn.recv()
            if not data: break
            print(data)
            data1 = input(">>>")
            if not data1: break
            conn.send(data1)
        conn.close()
    conn.close()

server()


# client.py --> this has to be in a separate file
#import socket

def client():
    host = "localhost"
    port = 23456
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        data = input(">>>")
        if not data: break
        s.send(data)
        data1 = s.recv(1024)
        if not data1: break
        print(data1)
    s.close()


client()














