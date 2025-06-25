**Exercise 1**
-
**For this and the following exercises,** use [this array](https://jsonplaceholder.typicode.com/users) of user information. You should at no point be using any loops.

Remember, JSON is valid JS, so you can just copy-paste it into a variable `let users = [`...

  

  

----------

  

Here's the first exercise:

  

Map the data differently so you are left with an array of each user's `email` and their company's `name`. Your resulting array should look like this:

  
```js
[
  {email: "Sincere@april.biz", companyName: "Romaguera-Crona"},
  {email: "Shanna@melissa.tv", companyName: "Deckow-Crist"}, 
  ...
]
```

-----

**Exercise 2**
-
Create an array with user objects that have a zip-code that starts with "5".

  

You should be left with the objects whose IDs are 3, 4, and 7.

--------------

**Exercise 3**
-
Modify your code from **Exercise 2** so that your resulting array only has the IDs of the matching users. You should chain your `filter` with a `map`. Ultimately, you should just have this array: `[3, 4, 7]`

------------

**Exercise 4**
-
Create an array of only `name`s, then only keep the names that [start with](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith) with the letter "C".

  

You should be left with `["Clementine Bauch", "Chelsey Dietrich", "Clementia DuBuque"]`

-----

**Exercise 5**
-
Determine whether all of the users live in the city of  "South Christy" - you should find the answer to be false  in a single, beautiful line of code.

---------------------------
**Exercise 6**
-
Find the user who's `suite` is "Apt. 950" - console log her company's name.

Your code should print out "Considine-Lockman".

---------

**Exercise 7**
-
Write a named function that receives a single parameter, `user`.

  

Using `forEach` and the named function you just wrote, console log "NAME lives in CITY, and owns the company COMPANY_NAME" for each user.
