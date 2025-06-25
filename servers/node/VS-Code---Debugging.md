
Of course, we're not barbarians. We need our debugger, and Chrome gave us a great tool for that.

  

Fret not, for if you're using [Visual Studio Code](https://code.visualstudio.com/), then there's a built-in node debugger just waiting for you to use it!

  

In fact, you can run JS code _directly in_ VS Code, and see the results in the IDEs own terminal.

And it's very simple: just press F5 to run your code - it can take a moment, but shortly after you should see the **Debug Console** open up with your code results.

  

Now to actually debug (i.e. stop your code execution and see what's what), click just to the left of the line numbers where you want your code to stop executing. When you hover your mouse over it, you should see a dull red dot appear:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/node-vscode-debugging.PNG)

  

The dot should turn bright red once you click it.

  

Then, run your code again ( press F5 ) and you should see a mostly familiar interface:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/node-vscode-debugging-active.PNG)

  

You can go more in depth about VS Code's debugger by watching this [6 minute video](https://code.visualstudio.com/docs/introvideos/debugging), but it's quite similar to what we had when we worked with our browser - including a display of the call stack on the left!