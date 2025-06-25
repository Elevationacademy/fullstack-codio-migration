
For this project you will need to use Socket.io.

  

As their documentation states: "_Socket.IO enables real-time, bidirectional and event-based communication"._

  

In other words it means, that until now, when we wanted to receive data from the server, we had to make a GET request, and wait for the data. But, what happens if we are using an app, and the server wants to send a notification or message to the app without getting an action from the user? That's where we can use socket.io.

  

This service enables us to use real time communication, such as, notifications, messages (chat), analysis and more. You can read more about it [here](https://socket.io/).

  

For this project, you will need to read about [rooms](https://socket.io/docs/rooms-and-namespaces/#Rooms), which is can allow socket to 'emit' something to a group of people (who are in the same room). For instance, when a user sends a message to a group, everyone in the group (or in the room - in socket.io language), will receive this message.

  

You'll want to use rooms in this project so that you can have more than two players play in the same game.
