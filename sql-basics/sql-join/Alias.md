
So far we were able to join `transaction` and one other table separately, but our original goal was to join _all three_ tables together.

  

To do that, you might think to do something like this:

```
SELECT *
FROM transaction, customer, company
WHERE 
    transaction.customer_id = customer.id AND
    transaction.company_id = company.id;
```
  

However, if you looked close enough, you will have noticed that our resulting table only has _one_ `name` column! That's because _both_ `customer` and `company` have a column named `name`, and SQL can't have repeating columns!

  

The solution to this problem is to use something known as **aliases** - this allows us to give a name to our columns/tables and thereby be more specific in our queries.

  

Using an **alias** requires the `AS` keyword, like so:

```
SELECT 
    item_purchased, amount, 
    customer.name AS cust_name, -- aliasing
    company.name AS comp_name
FROM 
    transaction, 
    customer, 
    company
WHERE 
    transaction.customer_id = customer.id AND
    transaction.company_id = company.id;
```
  

Here we are **aliasing** both the `customer.name` and `company.name` - the first is being aliased to `cust_name` and the second to `comp_name` - this way, our resulting table will have no conflicts on the column name `name`:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dbs/sql/alias-example.PNG)

  

And **finally** - we have all our relevant data, from three separate tables, in a single query.

  

You can think of **aliasing** as "giving another name for" - very useful in cases like this, where separate tables have identical column names.