
The simplest thing we know to do with a database is to select everything, so let's see how that looks with sequelize:

```
sequelize
    .query("SELECT * FROM company")
    .then(function ([results, metadata]) {
        console.log(results)
    })
```
  

We use our `sequelize` instance (which is connected to our DB) to invoke the `query` method.

  

In this method we are allowed to write any valid SQL statement.

  

The **chained method** `then` let's us easily read the result as an array of `TextRow` objects using the `results` parameter.

  

The callback in `then` has two parameters: `results` and `metadata` - usually we only care about `results`, but it's important to understand that **`query`** **always returns both of these.**

  

Note how we deconstructing the received arguments from the query with the `[]`. You can try omitting those square brackets and see what you get in `results`.

  

----------

  

Make sure you have a `company` table set up (you can do this with normal SQL) with a few entries (one column should be the `name` of the company), then you can print all the company names in the `then` callback like this:

  
```
sequelize
  .query("SELECT * FROM company")
  .then(function ([results, metadata]) {
    results.forEach(c => console.log(c.name))
  })
```