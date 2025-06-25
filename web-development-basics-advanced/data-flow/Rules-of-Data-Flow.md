
Based on the wonderful architecture ideas laid out above, let's summarize them into a short list of best-practices:

  

1.  Store application **data in one place** only (an array, or a certain file, etc)
2.  Update your _data_ in response to events (a click, a key press, a mouse-over, etc) - don't update your DOM directly when events happen
3.  Render your views only in response to changes in your data

  

Here's another way to think about the flow:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/data-flow-simple.PNG)

  

Another popular name for working like this is called the **MVC Architecture** - this stands for **M**odel **V**iew **C**ontroller.

The **Model** is where our data is stored.

The **View** is what the user sees.

The **Controller** is what the user interacts with, to update the data, which triggers an update in the view.