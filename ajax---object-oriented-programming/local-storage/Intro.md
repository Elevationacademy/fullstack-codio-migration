
In this lesson we're going to learn about Local Storage - our first foray into persisting data! Specifically we'll cover:

  

-   What Local Storage is
-   Setting items
-   Getting items
-   Removing items
-   Clearing the whole thing
-   Storing complex data

  

No need for more hyping, let's dive right in.

  

----------

  

#### **WHAT IS LOCAL STORAGE?**

  

Local Storage is a browser technology that gives web developers the ability to temporarily (perhaps permanently*) store data right in the browser. This does **not** replace databases, but it is used for storing simpler things (like a shopping cart list, user site-preferences, etc.) that we don't need/want to store in a database.

###### *Theoretically, stuff you save to local storage could stay there forever. You'll understand soon enough =]

  

There's no hard-and-fast rule for _when_ to use Local Storage - it's an architectural decision you'll learn to make as you code more. But there are some cases where you pretty much have to use it (as with authentication, which we are not covering right now).