
First thing we need to do is define a table.

  

Typically, we have **one database per project** - for now, you won't be creating any databases. Just tables.

  

**A database can hold many tables, but each table only belongs to one database**.

  

A table defines **the structure of our data** - i.e, what are the table **columns** and what **type** are they.

  

You can imagine an SQL table as a simple Excel sheet:

  

```
item_name 		item_price
Cheese Pinata 		32
Aqua Bread			18
Roasted Books		21
```
  

The **columns** in the above are **item_name** and **item_price**, and each **row** holds all the data about a single **item**.

  

As such, we might call the above our **item** (singular) table.

  

Typically, **the number of columns is fixed** in an SQL table, though you can have **as many rows** as your storage allows.

  

----------

  

Let's put this to practice in SQL.

  

Start by **creating a file called** **`first_script.sql`** (or whatever, so long as it ends with `.sql`), then **code along** with this initial setup.

  

The command to create a table starts - unsurprisingly - with the words:

  

`CREATE TABLE`
  

Next you have to give the table a name and its properties & types. For instance:

  
```
USE sql_intro; -- lets VS code know which DB to use

CREATE TABLE Deity(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    mythology VARCHAR(20),
    main_power VARCHAR(50),
    coolness INT,
    creation_date INT
)
```

  

We'll talk about **primary keys** soon, but here we've created a table named `Deity` which will store the god-like properties `name`, `mythology`, etc.

  

Each of the properties will represent a **column** in our table.

  

As for the VARCHAR/INT business, we have to tell SQL what _type_ our data is representing, so:

-   `VARCHAR`: for string values - the number in parentheses is an upper limit for how many characters to store
-   `INT`: whole numbers (if you give it fractions it _will_ round them)

  

You can check out the other types [here](https://www.w3schools.com/sql/sql_datatypes.asp) or more info on table creation in the [official docs](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)

  

To run the above command you can either right click and press **Run MySQL Query**, or use the shortcut **Ctrl+Alt+E** (on Windows at least)

  

To see that your table was created, **right-click and refresh the** **`sql_intro`** DB on the bottom left of your editor under the **MYSQL** tab - you should see all your columns and their types.

  

Now make sure you **comment out/delete this command** - you only need to `CREATE` a table once - then it's persisted in your DB. However, do not comment out the USE `sql_intro` command as you will need this in order to tell VS Code which db to use when inserting, querying, etc.