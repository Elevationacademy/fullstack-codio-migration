In this lesson we will learn how to handle errors in the server. 

If in a regular code we might of think of throwing an error in case of a problem, we can not do that in a server.

A server is suppose to run at all times, so in case of an error we want the server program to continue to run. So, instead of throwing an error we will return an erroneous response.
This means a response with a status code that describes the problem.

|||
## Question

Which status code families are suitable for errors? remember?

|||



<details>
  <summary>
     Check the answer here
  </summary>
    400 - client errors <br/>
    500 - server errors
</details>


