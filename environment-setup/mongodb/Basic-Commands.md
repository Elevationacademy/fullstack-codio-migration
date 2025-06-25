
The most basic command allows us to see what databases we have available to us. The command looks like this:

  


```bash
show dbs
```

  

Initially, this should only show the default DBs, something like this:

  

```bash
admin   0.000GB
config  0.000GB
local   0.000GB
```
  

To create (or access) our own DB, we have the `use` command:

  


```bash
use test-db
```
  

This command will either create a new database called `test-db`, or access an existing one if you've already created it.

Now however (because it didn't exist before), if you `show dbs` again, you won't see anything new. This is because **Mongo will only show you databases that have some data in them**.

As such, let's add our first "document" (we'll explain what this means later):

  


```bash
db.firstCollection.insert({name: "You"})
```
  

Now if you `show dbs` again you will see your `test-db` listed. Not only that, but if you execute this command:

  


```bash
show collections
```
  

Then you'll see `firstCollection` output - again, we'll explain what a collection is in a separate lesson.

But finally, to see the data you've just created, you can run this command:

  


```bash
 db.firstCollection.find({})
```
----------

  

That's it - if you've reached this point, you're ready to start learning Mongo!
