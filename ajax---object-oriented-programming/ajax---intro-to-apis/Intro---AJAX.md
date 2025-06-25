
So far we've been creating little apps that have been mostly self-contained. That is, we (or our fictitious users) have generated all the data in our apps.

  

Today we're going to expand our apps' horizons a little by introducing a couple of concepts that will allow us to bring in data from outside sources.

  

Think about [all the weather apps out there](https://www.androidauthority.com/best-weather-apps-and-weather-widgets-for-android-256942/) - in all likelihood, few of them actually generate their own weather data by themselves; instead, they use an external **API**to get that data, and then display that data with their own UI/UX.

  

Whenever we make such **requests** to external sources, we are executing an operation that can take time*.

  

Because we don't want our user to see a blank or frozen page while that request is happening, we need to make these requests **asynchronously** - that is, out of sync with the rest of our app's functionality. That is where **AJAX** comes in: our first topic for this lesson.

###### Think of it as the internet's version of sending your friend to the library to get some information for you

  

----------

  

#### **AJAX**

  

AJAX stands for **A**synchronous **J**avaScript **A**nd **X**ML, though these days we generally focus on the JavaScript part.

  

It is **a set of web development techniques we use to create asynchronous web apps**. The two main things AJAX allows us to do are:

  

1.  Receive data from a server* (our own or some distant one)
2.  Send data to a server

###### *We'll talk more about servers in a future lesson, but for now you can just think of it as a physical machine that has access to some data (among other things)

  

The two things AJAX allows us to do (receive and send data) beg the questions: who is receiving? From whom are we sending?

  

The answer is: **our client** - the apps we've been building so far have been entirely **client-side applications**. In other words, we've only built the parts that our users will eventually interact with. No servers, no databases; pretty straightforward so far.

  

With AJAX & APIs we begin to introduce the idea of there being some **server** with which our client can interact - receive and send data. This opens up a world of possibilities.

  

Just look at [all these APIs](https://any-api.com/) - that's a lot of data to leverage in our apps!
