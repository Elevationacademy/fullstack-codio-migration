Create a `put` route called `/update` that receives two variables: `group1` and `group2`

  

In a full-stack app, if you wanted to update an expense you would likely click on it, and pass the server the id of the expense you would like to change. Since we're only building back-end right now, you'll simply find the first expense for a certain group and change it to another group.

  

There are a couple different ways to do this, mongoose has some nice built in methods to help us out with it.

**You should be able to do this with one method, without using promises**

  

`res.send` a message back with the name of the expense changed, and what the group was changed to.
