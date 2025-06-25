
Time to actually _store_ stuff in our table - it's so empty in there right now. The command for inserting data into our table is - again, no big surprise here:

  

`INSERT INTO TABLE_NAME`
  

Now you have two options, you can either tell it specifically which values to insert into which columns:

```
INSERT INTO Deity(name, coolness)
VALUES("Zeus", 11)
```
  

This will insert only these values (in the order you write them), and leave the other values _blank_.

  

**Or** if you're inserting all the values in the order of the columns, you can just do:

  
```
INSERT INTO Deity 
VALUES(null, "Zeus", "Greek", "Thunder", 11, "-1400")
```
  

A few notes on the above:
-   You must insert the first `null` as a **placeholder** for the `id` column
-   Negative numbers must be wrapped in quotes - though they're still stored as numbers

  

Anyway, run that command and **bam**! You've saved some data. We'll learn how to see that data in a second, but for now let's make sure this is clear.