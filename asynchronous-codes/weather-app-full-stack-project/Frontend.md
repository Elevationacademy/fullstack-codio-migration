
#### **CLIENT**

####   

For your client you'll need to have a dist folder with a your files separated correctly. You must keep this fully MVC compliant.

  

----------

  

#### **YOUR MODEL**

  

Here's what should go inside your model class:

-   **A Data Structure** - This will hold all the cities we want to display on the client side
-   **A method**, which gets all the cities from the server.
-   **A method** which gets the city's data from the server.
    -   Hint: async
-   When the data comes back, you need to make sure that it is added to your models data .
-   **A method** which saves a city's data to the database
-   Make sure this is MVC compliant
-   **A method** which deletes a city from your database

  
----------

  

#### **YOUR VIEW**

  

Here's what should go inside of your Renderer class:

-   **A method** which appends data to the HTML

  

-   Though it's not explicitly part of your render class, you also need to add in your Handlebars template to your HTML.

  

----------

  

#### **YOUR CONTROLLER**

  

Your controller should have the following:

-   **A function**, which should render any saved data
	-   This function should run when the page loads
-   **A function**, which should call to the server and render new weather data for the specific city the user searched for.
	-   Hint: This function needs to be async to work
-   **An eventHandler for your** **`search`** **button**, which executes the search.
-   **An eventHandler for each of the** **`save`** **buttons** that:
	-   Saves that city in your DB
-   **An eventHandler for each of the** **`remove`** **buttons** that:
	-   Deletes that city from your DB
