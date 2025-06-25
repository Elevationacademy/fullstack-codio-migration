
While knowing the basics of SQL is nice for simple data, we generally find ourselves dealing with much more complex data than a few columns can manage.

For example, take a company like Amazon. They [own quite a few companies](https://www.cheatsheet.com/money-career/a-round-up-of-all-the-companies-amazon-owns.html/), and we all know they're tackling everything.

  

You might therefore imagine that a `Customer` table for Amazon looks like this (*view on full screen):

```
customer_name    item_purchased         price    date        subsidiary
Frank Herbert    The Everlasting Winds    2    02-13-2018     Goodreads
Frank Herbert    Duke's of Yore           3    02-13-2018     Goodreads
Anthony Higgins  6-mo subscription        129  01-01-2019     Twitch
Sabrina Brimms   Brown shoes              31   12-06-2017     Zappos
...
```
  

But this is certainly not the case. The above is **bad table design** for a few reasons:

-   It is **unclear what the purpose** of the table is
    -   Could be a table about customer transactions
    -   Or a table about subsidiary transactions
-   The table is **not DRY** - we repeat customer names and subsidiary names
    -   The way it's set up, we would also be repeating item names
-   The table is **not complete** in a business sense. We are missing:
    -   Data about the customer (gender, location, etc)
    -   Data about the subsidiary (owner, branch, etc)
    -   ...much more

  

**Note: in this lesson you should follow along and execute the code** **(which will build your DB)** **in order to solve the spot checks**