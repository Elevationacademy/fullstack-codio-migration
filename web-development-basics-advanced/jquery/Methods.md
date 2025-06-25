css & addClass


Run the following inside the console of this lesson's page:
```
$("h4")
```

There - you've called the jQuery function with h4 as an argument.



What comes out is all the h4s on this page, as well as methods relevant to those elements.



Now run this code:
```
$("h4").css("color", "red")
```

That is us using the css method* to manipulate the returned array of elements - in other words, we've changed all the h4's colors to red - bloody nice.

*The css method takes two arguments: the first is the css property and second is the value