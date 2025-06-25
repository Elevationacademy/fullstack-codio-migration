
You should set up your project to have a `server.js` file and a server folder, which includes a `routes` folder with an `api.js`, and a `model` folder, with an `Expense.js` file in it.

  

Make sure to add npm and git to your project. You'll need express, mongoose, body-parser, and [moment.js](https://momentjs.com/)

  

Set up your express server and your `api.js` file. Once you're all ready to go, create a new mongoose schema for your expenses in your `Expense.js` file, call it "expenseSchema". Your schema should have the following:

-   `item`, a string
-   `amount`, a number
-   `date`, a date
-   `group`, a string

  

Make a model of your schema and export the model for use!

  

Start by adding some data to your db. You can download [this json of data](https://github.com/Elevationacademy/expenses-data). `Save` it into the root of your project directory

  

In order to add this JSON to your DB, you can save the JSON in a `.json` file, then simply `require` it. Next, you can write a simple loop that goes over each item in the JSON and `save`s it using Mongoose.

  

Check your DB to make sure the data saved.

  

**Note:**

**You should do this only once!**

**Make sure to write this code in a separate file and run it only once**.
