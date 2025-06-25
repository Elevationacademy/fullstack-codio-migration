### Socket Interfaces

A network application consists of pairs of programs in different hosts that send messages to each other over a network. For example, in a Web application, the client browser app exchanges messages with a Web server app. 
A program sends messages into, and receives messages from the network, through a software interface called a **socket**. A socket is the interface between the application layer and the transport layer within a host. Simply put, when you, as a software developer, want your application to send or receive data over the Internet (in the lowest level form, without any usage of 3rd party code) it is done by creating and listening to a socket. All you have to do is to choose the the transport layer protocol that the socket will rely on: **TCP** or **UDP**.


|||info
In a modern software development, you will rarely need to deal with socket programming yourself. You will usually use pre-built libraries that implement higher level API for you, which can save you a lot of time and allow you to put your effort in your business logic instead of communication aspects.
|||


### The Transmission Control Protocol (TCP) 
Packets can get lost within a computer network, a packet can overflow a buffer in a router, or can be discarded by a host or router after having some of its bits corrupted. For many applications, such as financial applications, remote host access and Web document transfers, data loss can have devastating consequences. Thus, to support these applications, something has to be done to guarantee that the data sent by one end of the application is delivered correctly and completely to the other end of the application.

TCP is a **connection-oriented** and **reliable** data transfer protocol. 

Before client and server are able to exchange information with each other, a TCP connection has to established. This so-called handshaking procedure initialized by the client, prepare both sides for the actual packets transfer. After the handshaking phase, a **TCP connection** is said to exist between the sockets of the two programs. The connection is a bi-directional, in that the two programs can send messages to each other over the connection at the same time. When the application finishes sending messages, it must tear down the connection. 

The communicating programs can rely on TCP to deliver all data sent without error and in the proper order. When one side of the application passes a stream of bytes into a socket, it can count on TCP to deliver the same stream of bytes to the receiving socket, with no missing or duplicate bytes.

### The User Datagram Protocol (UDP)

UDP is a simple, lightweight transport protocol, providing minimal services. UDP is **connectionless**, so there is no handshaking before the two programs start to communicate. UDP provides an **unreliable** data transfer service, that is, when a program sends a message into a UDP socket, UDP provides no guarantee that the message will ever reach the receiving process. Furthermore, messages that do arrive at the receiving program may arrive out of order. 
UDP is suitalbe for a loss-tolerant applications such a live streaming services, Internet telephony, and online gaming.

