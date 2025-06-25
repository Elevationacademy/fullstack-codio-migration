
This section is optional!! don't waste a lot of time on it!

  

Change up your `server.js` code a bit so that instead of writing `Hello, world`, it writes ``Hello, I'm {your_name_here}``. Save the file, and run your server again.

  

Go to [localhost:3000](http://localhost:3000/) again and make sure it works.

  

Now, open up a different terminal and install the following package:
```
npm install ngrok -g
```
  

Then, run the following command:
```
ngrok http 3000
```
this will open you a new window:

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A1615-0.png)

Look at the line:

``Forwarding https://6993891a.ngrok.io -> localhost:3000``

  

  It means that when you accessing the url: ``https://6993891a.ngrok.io`` it will forward to ``localhost:3000`` - your server!!

The "new" url is accessible from every device... try to access this url via your smartphone...

  

In other words, if anyone else on any other computer goes to that address, they will see your personal message: ``Hello, I'm {whichever_name_you_put}``

  

PC users:

If you are running into a error message saying something like this:

```
cannot be loaded because running scripts is disabled on this system.   
For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
```

  

Open your "Window PowerShell" as administrator (You can search for it in the search panel), and run ``Set-ExecutionPolicy remotesigned``

  

  

This is a quick-and-dirty way to expose/host your app to the world - you can read more about Ngrok [here](https://ngrok.com/) - but it's really only good for quick tests. We'll learn a better, permanent way to host our servers in a future lesson.