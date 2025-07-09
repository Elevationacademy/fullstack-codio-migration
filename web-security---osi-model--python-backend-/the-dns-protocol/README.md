# Overview

All computers on the internet, from smart phones to the servers that serve massive amount of content, communicate with each other by using IP addresess. 

When you open a browser and go to a website, you don't have to remember and enter the server IP address. Instead, you can enter a domain name like example.com and still end up in the right place. The DNS service helps to make that connection between domain names and IP addresses.

The DNS is an application-layer protocol that allows a given hosts (clients) to query a complex distributed database system in order to resolve a domain (e.g. www.google.com) to the IP address (e.g. 142.250.201.14).

Suppose a user wants to visit www.google.com. The web browser needs to translate the google.com hostname to an IP address. The browser will invoke the client side of DNS, which send a query message into the network. All DNS query and reply messages are sent over **UDP** on **port 53**. After a delay ranging from milliseconds to seconds, DNS in the user’s host receives a DNS reply message that provides the desired hostname -> IP address mapping.


|||definition
## Why UDP?

 
DNS utilizes the low overhead of UDP to resolve hostname as fast as possible. UDP, as a *connectionless* protocol, is **much faster** than TCP which requires the handshake before sides can communicate. DNS queries are usually not more than 512 bytes and can be delivered within a **single packet**, so no order control is required. If packet is getting lost, DNS just try again! DNS implements a simple logic to check data integrity itself (instead of relying on that of TCP).  

Note that DNS **may** use TCP for large size queries.
|||