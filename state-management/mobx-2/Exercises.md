
## Exercise 1
    
Your exercises are to complete this reservations application. Here's what you need to do:
    
      
`src/stores/RestaurantStore.js`
    
      
    
-   add a `computed` value `restPopulation` which calculates the number of people currently in the restaurant (number of people who have reservations which are not completed but are seated)
-   add a `computed` value `completedTables` which calculates the number of tables which have been completed
-   add an `action` `completeRes` which takes a parameter `id`, finds a reservation, and marks the reservation as complete
-   add an `action` `seatRes` which takes a parameter `id`, finds a reservation, and seats the reservation
    

## Exercise 2
    
`src/components/Restaurants.js`
    
-   Render the number of people in the restaurant in a `div`
-   Render the number of completed tables in the restaurant in a `div`
-   Render the reservations from your `RestaurantStore` using the `Reservation` component. Use the prop "res" to pass the reservation down.
    -   Give the reservation a "complete reservation" button which runs the `completeRes` action in your `RestaurantStore`
    -   Give the reservation a "seat reservation" button which runs the `seatRes` action in your `RestaurantStore`
-   Make the "Add Reservation" button work using _both stores_. You need to pass the `observable`s from the `GeneralStore` to the `addRes` function in the `RestaurantStore`


## Exercise 3
    
Make sure to conditionally render reservations which are completed vs. those that are not, using the class "conditional" (we provided basic css for you).