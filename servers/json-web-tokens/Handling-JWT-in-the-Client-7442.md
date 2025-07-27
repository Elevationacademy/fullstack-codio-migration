Now that we managed to adjust our **Backend** to Handlde **JWT**, we want to Handle it in the **Client**.

In the end **JWT** is a **JSON**, we need to save it somewhere on the **Client**. 

## Local Storage

The **Local Storage** is a great place to save small data like the **JWT**.

So when we receive a **JWT** from the **Server** we can save it in our **Local Storage**. 
When we need to make a request again to the **Server** we need to make sure our request has this `token`.

We can do this using the `setItem` method. 

