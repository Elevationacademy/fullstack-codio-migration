
Of course, having a DB is no fun if all we can do is extract the entire table or entire columns.

Sometimes we need to _filter_ our results. And the syntax for finding data where certain conditions are met is riveting:

  

`SELECT ...`

`FROM TABLE_NAME`

`WHERE SOME_CONDITION`

  

For this next part, it will only be interesting if you have more data in your table.

  

For instance, if we wanted to find all the deities in our table from Greek Mythology:


```
SELECT name 
FROM Deity
WHERE mythology = "greek"
```
  

Two notes:

-   Tragically, SQL doesn't adhere to the usual `==` vs `=` concept that virtually **every other programming language** does - be strong
-   We've split the **query** to three separate lines
    -   This is fine: SQL will keep reading until it reaches a semicolon or end of file, _then_ execute the command

  

Our results for the above look like this (note that we only selected the  `name`  column, so that's all we see in the results):

  

![](./sql-intro-2.png)