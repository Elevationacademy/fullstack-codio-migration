Exercise 1
------

Find the count of people who make more than 25000.

  

You should find it to be `231`.


Exercise 2
------

Find _only_ the top 3 earning people, and return _only_ their first name and salary.

  

They should be:

  
```js
{ "firstName" : "Alice", "salary" : 69900 }
{ "firstName" : "Eva", "salary" : 69500 }
{ "firstName" : "Maisie", "salary" : 69400 }
```

Exercise 3
-------

Find the total number of people currently working at Walmart that are earning [_at least_](https://docs.mongodb.com/manual/reference/operator/query/gte/) 7000.

  

You should find it to be `24` people.

Exercise 4
-------

Find the current company name, full name, and salary of the highest earning person that currently works in either Sales or Retail.

  

Make sure you're returning only those fields (company name, first and last name, and salary.)

  

You should find it to be `Holly Gonzales`, working at `Groupon` for `20,000`.


Exercise 5
--

Find the number of people who have ever worked at Apple, past or present.

  

You should find it to be `325`.

Extension 1
--

The following exercises involve the `aggregate` command. Very powerful stuff.

  

----------

  

Now find the count of people _per industry_ that are _currently_ working at Apple.

  

You should get this result:

  
```js
{ "_id" : "Tech", "count" : 10 }
{ "_id" : "Manufacturing", "count" : 26 }
{ "_id" : "Sales", "count" : 51 }
{ "_id" : "Retail", "count" : 28 }
```

Extension 2
------

Find the average salary of an Analyst per company.

  

You can validate that you did this right by yourself:

-   Find the total (sum) of salaries per company for Analysts
-   Find the number of people working at each company
-   Divide the total salary by the number of people

  

To double check your work, here are the results you should receive:

  
```js
{ "_id" : "Microsoft", "averageSalary" : 32000 }
{ "_id" : "Nintendo", "averageSalary" : 14550 }
{ "_id" : "Amazon", "averageSalary" : 31300 }
{ "_id" : "Google", "averageSalary" : 32650 }
{ "_id" : "Goldman Sachs", "averageSalary" : 37200 }
{ "_id" : "J.P Morgan", "averageSalary" : 48960 }
{ "_id" : "Suisse Bank", "averageSalary" : 24975 }
{ "_id" : "Chase", "averageSalary" : 40580 }
{ "_id" : "Robin Hood", "averageSalary" : 50500 }
{ "_id" : "Dell", "averageSalary" : 28700 }
{ "_id" : "HP", "averageSalary" : 24880 }
{ "_id" : "Twitter", "averageSalary" : 24325 }
{ "_id" : "Capital One", "averageSalary" : 38533.333333333336 }
```

Extension 3
---

There is a superstition that says that your family name can affect your salary.

  

To test that, find the average salary for people that (work at _either_ Google or Apple) _and_ (are in the _Tech_ industry).

  

Your result should be _per last name_ and sorted from highest to lowest average.

  

Check this out to validate the result you got:

  
```js
{ "_id" : "Ortiz", "average" : 39500 }
{ "_id" : "Russell", "average" : 38700 }
{ "_id" : "Morales", "average" : 38400 }
{ "_id" : "Reynolds", "average" : 38300 }
{ "_id" : "Gonzales", "average" : 38000 }
{ "_id" : "Bennett", "average" : 35100 }
{ "_id" : "Foster", "average" : 34850 }
{ "_id" : "Barnes", "average" : 33600 }
{ "_id" : "Sullivan", "average" : 32900 }
{ "_id" : "Chavez", "average" : 32000 }
{ "_id" : "Gutierre", "average" : 31500 }
{ "_id" : "Griffin", "average" : 30400 }
{ "_id" : "Hughes", "average" : 30200 }
{ "_id" : "Perry", "average" : 30100 }
{ "_id" : "Price", "average" : 28900 }
{ "_id" : "Ross", "average" : 28500 }
{ "_id" : "Myers", "average" : 27100 }
{ "_id" : "Jenkins", "average" : 23800 }
{ "_id" : "Wood", "average" : 23500 }
{ "_id" : "Fisher", "average" : 23400 }
```
