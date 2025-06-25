
At this point you should have **your first MERN app complete!** - This is very exciting. Great job. Celebrate _somehow_.

Once you've wound down from the excitement, complete the following extension (very doable).

  

**Extension**

<ins>Snackbars</ins> - you should tell your users when an action succeeded or failed - you'll be doing this with snackbars (again, we recommend using [Material UI](https://material-ui.com/components/snackbars/)):

-   When adding a new transaction there should be a little popup letting the user know that their expense was added.
-   In the case of some sort of error there should be a snackbar popup letting them know:
    -   If a user leaves out one of the inputs, let them know with a snackbar that they cannot take action unless they fill in all the inputs.
    -   We also do not want to allow any **Withdraw** operations if the operation would reduce the **Balance** to below 500. You should display a snackbar with a message that says 'Insufficient Funds'.

  

<ins>View by Month</ins> - when you add a transaction you should be able to choose a date for the transaction. By default you will see all transactions that come from your `get` route when you load the page, but the user can also filter by month and view only the transactions of the selected month (make sure to add this for the breakdown by category as well).

  

For this feature you'll need to change a few different areas of your app, so be strong.

1.  Make sure to add a date picker along with the original input options (we recommend using [Material UI](https://material-ui.com/components/pickers/)).
2.  Change your database schema to accommodate for saving a date.
3.  Add a dropdown above your transactions list to filter transactions by month/year

  

  

<ins>Create A Modal</ins> - When you hover over each category in the **Breakdown** section, it should display a small "modal" (i.e a `div`) that displays _that_ category's transactions.