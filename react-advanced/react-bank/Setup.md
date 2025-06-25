
You're going to be making a full stack Bank/Expense tracker application.

The initial component tree for this application can looks like this:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/react/react-bank-project-component-tree.PNG)

Think what other components you might need.

On the **backend**, you'll have a single `transactionSchema` with the following properties:

-   `amount` - a number
-   `category` - a string
-   `vendor` - a string

Connecting the frontend and backend in React requires a tiny bit of setup, which we will discuss later on in this guide.