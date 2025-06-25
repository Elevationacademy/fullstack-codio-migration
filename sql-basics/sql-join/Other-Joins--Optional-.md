
That's all about relationships for now, though there is a bigger world out there.

  

If you're interested in SQL, there's a whole [world of](http://www.mysqltutorial.org/mysql-inner-join.aspx) [join](http://www.mysqltutorial.org/mysql-inner-join.aspx)[ing](http://www.mysqltutorial.org/mysql-inner-join.aspx) that doesn't use the `WHERE` keyword at all, but has the same principle.

In fact doing joins using the `JOIN` command is the newer and clearer syntax.

  

If you expect to be asked about SQL in an interview, or want to be updated with your syntax - **definitely look into this activity.**

  

We saw before that sometimes we want use information from 2 crossing tables (or more), such as we want to know the names of users that purchased 2 items in a single transaction. The user details, such as his name are in the `Customer` table, and the amount of items per transaction is in the `Transaction` table. We can join these two tables like this:

```
SELECT customer.name 
FROM transaction JOIN customer
on transaction.customer_id = customer.id
WHERE transaction.amount=2;
```

In this way we have a separation between joining the tables and filtering the rows.

  

There are all kinds of joins. The one we used is called an Inner join, it means that the rows in the new joined table will contain only ids that appear in both tables.