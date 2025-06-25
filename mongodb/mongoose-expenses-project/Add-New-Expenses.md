
Create a `post` route called `/expense`:

  

-   The body sent to the route should have 3-4 fields:
	-   `item`
	-   `amount`
	-   `group`
		-   the previously used groups are "fun", "food", "rent", "bills", and "misc"
	-   and optionally a `date`, written in [RFC2822](https://www.ietf.org/rfc/rfc2822.txt) compliant format of "YYYY-MM-DD"

  

-   You should create a new Expense (using the expense model), from data given in the body of the post request.

  

-   The Expense should be created with each field filling in it's respective spot in the schema - name to name, amount to amount, and group to group

  

-   For the date you can use a [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) to determine if you were given a date in your body.
	-   If you were given a date, use [moment.js](https://momentjs.com/) to `format` the date given to the "LLLL" format.
	-   If you were not given a date, then use moment.js to create a new date, also in the "LLLL" format

  

-   You can also define the date outside of your instance creation, if you don't like ternaries

  

-   Make sure to save the new Expense to your DB. `then` use a promise to `console.log` a string that says the amount of the expense and what you spent your money on.
