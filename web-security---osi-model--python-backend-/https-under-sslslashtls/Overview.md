## HTTPS Protocol

HTTPS (HyperText Transfer Protocol Secure) is an encrypted version of the HTTP protocol usually running on **port 443**. It uses SSL or TLS to encrypt all communication between a client and a server. This secure connection allows clients to safely exchange sensitive data with a server, such as when performing banking activities or online shopping. In today's modern HTTPS protocol, the communication protocol is encrypted using Transport Layer Security (TLS).

To understand the need for HTTPS over TLS, let’s walk through a typical client-server banking scenario. When clients want to transfer money using the bank website, they form an HTTP request which essentially says "I'm Bob, want to transfer 500$ to Alice using the following credit card number....". If no security measures are taken, Bob could be have a few surprises.

- If no **encryption** is used, an intruder (man-in-the-middle) could intercept Bob’s request and use Bob's credit card details. 
- If no **data integrity** is used, an intruder could modify Bob’s transaction (e.g. change "Alice" to "Eve"). 
- Finally, if no **server authentication** is used, a server could display the bank famous logo, when actually the site maintained by Eve, an intruder who is impersonating as the bank website. After receiving Bob’s transaction, Eve could take Bob’s information and run away.


## TLS 

The primary goal of the TLS protocol is to provide **privacy (encryption)**, **data integrity** and **authenticity** between two communicating applications. Once the client and server have agreed to use TLS, they negotiate a stateful connection by using the so-called *handshaking* procedure.