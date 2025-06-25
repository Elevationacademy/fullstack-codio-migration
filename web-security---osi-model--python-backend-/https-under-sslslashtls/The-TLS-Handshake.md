To achieve privacy, data integrity and authenticity, TLS uses famous **symmetric** cryptographic algorithms such as [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) and [MAC](https://en.wikipedia.org/wiki/Message_authentication_code). All the parties (the client and the server) have to do is to exchange some secret key between them. Once they agreed on a key, the rest is easy. A key may look like: 

`358072d6365880d1aeea329adf9121383851ed21a28e3b75e965d0d2cd166254` 

We will call this kind of key a **Master key**.

But this is a chicken-and-egg problem, isn't it? In order to secure the connection, the client and server must exchange a master key (over an unsecured connection) which allows them to talk securely. How could that be?

We can utilize **asymmetric encryption** to achieve that. Asymmetric encryption uses pair of keys (public and private). The public key, as the name suggests, can be sent freely over an unsecured connection, it can be public. The private key should be kept securely on your machine. When someone wants to send you a message securely, he encrypts the data with **your public key** (which he has access to, as it is public). Then only **your private key** can decrypt the message. It is like a [spring lock](https://www.google.com/search?q=%D7%9E%D7%A0%D7%A2%D7%95%D7%9C+%D7%A7%D7%A4%D7%99%D7%A5), when the lock is released, everyone can lock it, but only the keys owner can open it. 

Now consider the following process:

1. The server sends its public key to the client.
2. The client generates a *master key* locally.
3. The client encrypts the generated master key as a message to the server, using the server's public key, and sends it to the server. Since the message is encrypted, no fear to send the message over an unsecured connection. 
4. The server receiving the message and decrypts it. 
5. Now the client and server have the master key which allows them to communicate securely.   

This process is a **simplified version** of what called the *TLS Handshake*.

