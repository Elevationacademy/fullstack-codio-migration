
Once you're done with the basics (landing page, adding and removing rented movies, going to the details page), implement the Search and Budget features.

  

**Search**

  

You decide which state holds the search input.

  

Both the **Catalog** and **Rented** sections should change dynamically **as the user types** in the search bar.

  

Only movie titles that match what is in the search-bar should be displayed - the match should be very loose, for instance:

  

If the user types:

-   s - both _Beauty and the Beast_ movies and the _Sword in the Stone_ movie should appear
-   t - all the movies should appear
-   o - _Lion King_ and _Sword in the Stone_
-   tar - only _Tarzan_  
    

The search should be **case insensitive**.

  

When the search bar is empty, all the movies should display.

  

The array method [includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes) might come in handy.

  

**Budget**

  

The budget data (just a number) should be inside the **Catalog** component.

  

The budget should decrease by 3 each time a user rents a movie, and increase by 3 when they "un-rent" it.

  

If a user tries to rent a movie that would lower their budget to below 0, you should alert that there are insufficient funds, and **not allow** the rental to happen.