
Take this step by step:

-   Remove all values from the collection again
-   Add a `currentEmployee` field to each doc (hard-code this)
-   The values should be `false` for Brendon, Loreli, and Soren, and `true` otherwise
-   Run the `insert` commands again (for everyone)
-   Find the sum of salaries of all the departments _only_ for those are are currently employed
-   You will need to use the [`$match`](https://docs.mongodb.com/manual/reference/method/db.collection.aggregate/) [operator](https://docs.mongodb.com/manual/reference/method/db.collection.aggregate/)
-   Sort the results from the highest to the lowest sum (look at the `$sort` in the `aggregate` docs)
-     
    

You should receive `2300` for R&D, `1200` for `Finance`, and `950` for `Sales`

  

[Click here](https://codepen.io/ElevationPen/pen/EBKjVY?editors=0010) to see the solution.
