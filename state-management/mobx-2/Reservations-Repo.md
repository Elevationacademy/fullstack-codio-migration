
By the end of this lesson, you should have a working reservation tracking app.

  

Currently, this only renders the number of remaining tables and a couple of inputs. By the end of the lesson, we should be able to add new reservations, complete a reservation, and render all the reservations.

  

The Component tree is as follows:

-   `App`
    -   `Restaurant` - should render data for a restaurant
        -   `ResInput` - component for the inputs for a new reservation
        -   `Reservation` - all the reservation data

  

There are three stores:

-   `GeneralStore` - for all of our general data (will be explained in more detail later)
-   `RestaurantStore` - for all the data on a restaurant
-   `ReservationStore` - for all the data regarding reservations