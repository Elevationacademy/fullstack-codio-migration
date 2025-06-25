
#### **GET EXPENSES BY GROUP**

####   

Create a `get` route called `/expenses/` that takes a parameter `group`

-   Here you should find all expenses per a specific category

  

----------

  

#### **GET TOTAL EXPENSES BY GROUP**

####   

Add a query parameter to your `/expenses/:group` called total. If `total` is `true`, then instead of returning all results from the category you should `aggregate` them and return the total amount of money spent in that category. `$match` will come in handy here.