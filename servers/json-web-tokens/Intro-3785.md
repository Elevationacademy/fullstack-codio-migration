While we implement different servers with it's own routes, we have not taken into consideration that there will be multiple users using our server.

Our users have different data that is unique to them, we need to implement a system to identify the user.

Let's say you want to create a facebook app, if you want to see customized news feed that is unique to you, you need to identify the users that is sending the request and send him data that is relevant only to him.
However, there are different issues that could arise with this.

---

Imagine we implement a simple **login page**, how can we differentiate and secure that the client is truly who he says he is.

![](https://www.milestechnologies.com/wp-content/uploads/websecurityshield.png)


there are different measurements to counter these issues, such as **sessions**, **OAuth**, **OpenID** and more.

We could also solve this issue by using **Json Web Token**.

