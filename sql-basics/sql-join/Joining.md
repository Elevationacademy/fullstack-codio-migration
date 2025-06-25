
Let's take a look at our tables. **Query everything for each table**, and you should see (at least) the following (if you've been following along; though you may have different IDs):

  

**Customer Table**

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dbs/sql/customer-table-result.PNG)

  

**Company Table**

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dbs/sql/client-table-result.PNG)

  

**Transaction Table**

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dbs/sql/transaction-table-result.PNG)

  

While the `customer` and `company` tables display useful data, the `transaction` table only has some plain data, as well as a couple of references.

  

In this case (where we only have one row in each table) it's not a problem - but if we had even 10 items in each table, it would be hard to map everything in our brain.

  

In short, **our goal is to determine which customer purchased what item from which company in a single query.**

  

To do this, we need to **join tables**. The simplest way to do this is to use the `WHERE` clause we already know, like so:


```
SELECT * 
FROM transaction, customer
WHERE transaction.customer_id = customer.id;
```
  

For simplicity's sake we select everything, but note these three new things:

1.  We're selecting **FROM** _two_ tables - `transaction` and `customer` - separated by a comma
2.  Our `WHERE` condition is "filtering" on matches between the `ID` field in the `customer` table, and the `customer_id` field in `transactions`
    -   In other words, we're looking to **join** between those tables **based on the relevant ID**
3.  We used **dot notation** to "access" the relevant column for each table