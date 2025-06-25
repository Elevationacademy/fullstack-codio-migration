
To remedy this, we will **split the table** to separate tables and then use **foreign keys** to connect them and ensure their integrity (more on integrity later).

  

We'll work with these two tables for starters:

```
-- don't forget your USE ...;

CREATE TABLE customer(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    city VARCHAR(20),
    gender INT
);

CREATE TABLE company(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    industry VARCHAR(20),
    employees INT
);
``` 

These two are simple - a table for our customers, and a _separate_ table for our companies.

  

Now we need a table for our _transactions_, and that's going to bring these two tables together.

Here is the `transaction` table, we'll discuss new syntax below:

```
CREATE TABLE transaction(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    
    item_purchased VARCHAR(20),
    amount INT,
    discount FLOAT DEFAULT 0, 
   
    customer_id INT,
    company_id INT,
    FOREIGN KEY(customer_id) REFERENCES customer(id),
    FOREIGN KEY(company_id) REFERENCES company(id)
);
```
  

*note the use of `FLOAT` which allows us to use decimals

The first few lines are familiar: defining a primary key and some attributes.

  

Next we have our `FOREIGN KEY` (FK) definitions. These lines **create a relationship** between this table and the others.

  

Notice that we had to **first define the property in _this_ table <ins>before</ins> assigning it as a FK**.

Specifically, we first have to define `customer_id` and `company_id` as `INT`s _before_ we declare them as **F**oreign **K**eys.

  

Finally, we use the `REFERENCES` command to tell SQL which table and what property in that table we are creating a relationship through.

Specifically, we are creating the following **relationships**:

  

-   Between `transaction` and `customer`
    -   This relation is through the `customer_id` property in `transaction` and the `id` property in the `customer` table
-   Between `transaction` and `company`
    -   This relation is through the `company_id` property in `transaction` and the `id` property in the `company` table

  

----------

  

This begs the question: _what does this FK give us anyway?_

  

To answer that, **create the above tables, then run the following command:**

```
INSERT INTO transaction (item_purchased, amount, customer_id, company_id)
VALUES("The Everlasting Wind", 2, 1711, 32);
```
  

You should have received a similar error:

```
Error: ER_NO_REFERENCED_ROW_2: Cannot add or update a child row: a foreign key constraint fails (`shoobert_db`.`transaction`, CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`))
```
  

This is happening because we told SQL that there is a relationship between our `transactions` and `customer` & `company` tables - in particular,

-   There must be row in `customer` with an `ID` of `1711`
-   There must be a row in `company` with an `ID` of `32`

  

To fix this, you can insert values into `transactions` with row IDs you know exist in the other two tables. For example:

```
INSERT INTO customer (id, name, city, gender)
VALUES(1000, "Byron Trunks", "Corinth", 3);

INSERT INTO company(id, name, industry, employees)
VALUES(10, "Twitch", "Entertainment", 800);
```
  

And now we can add a row to our `transaction` table:

```
INSERT INTO transaction (item_purchased, amount, customer_id, company_id)
VALUES("The Everlasting Wind", 2, 1000, 10);
```
  

Now we are inserting a `transaction` with

-   An `item_name` of "The Everlasting Winds"
-   An `amount` of 2
-   A `customer_id` of 1000, which we had previously defined in the `customer` table
-   A `company_id` of 10, which we had previously defined in the `company` table

  

Once successfully done, we can say that the `transaction` table is related to the `customer` table through `customer_id` and `id`, and related to the `company` table through `company_id` and `id`

  

Not only is it related, but we can _guarantee_ that these relationships won't fail. If you try to `DELETE` a `customer`/`company` row, SQL will **prevent** you from doing that because `transaction` depends on these rows! And thus we can say (to an extent) that we are guaranteeing the **integrity** of our data.

  

----------

  

**Note**: The solution we just used was **hard-coded**, which is generally bad.

For now hard coding is fine - when we get to using SQL more dynamically, we'll see how to avoid this.