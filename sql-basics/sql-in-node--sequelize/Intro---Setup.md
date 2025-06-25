It's time to bring SQL on board our Node train.

  

We're going to use an NPM package called [Sequelize](http://docs.sequelizejs.com/) to help us connect our own server to our database.

  

Conveniently, the setup is pretty straightforward, and then we'll use Sequelize to write raw SQL queries as we've been practicing so far.

  

----------

  

#### **SETUP**

  

For starters, go ahead and run `npm init`, `npm install sequelize`, and then `npm install mysql2`

  

The first will install the actual `sequelize` package that will allow us to access our SQL server, and the second install is for the specific SQL database type we'll be using: MySQL (as opposed to postgres, MSSQL, etc).

  

Now,

-   Create a `testing.js` file
-   Import the module: `const Sequelize = require('sequelize')` at the top of the file

  

To connect to our DB, we'll create a new `Sequelize` instance, like so:

```
const sequelize = new Sequelize('mysql://YOUR_USER:YOUR_PASSWORD@YOUR_HOST/YOUR_DB_NAME')
```
  

So if you're on `localhost` with the `root` user, no password, and the `sql_intro` database, you would do something like this:

  
```
const sequelize = new Sequelize('mysql://root:@localhost/sql_intro')
```
  

To make sure you're connected properly, you should be able to run this and see a success message in your log:

```
sequelize
    .authenticate()
    .then(() => {
        console.log('Connection has been established successfully.');
    })
    .catch(err => {
        console.error('Unable to connect to the database:', err);
    })
```
  

And that's it! You're connected. Now let's get querying.