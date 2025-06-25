
#### **SERVER**

  

Your express server should have a normal set up. Make sure to include a model folder a fitting file.

  

----------

  

#### **DB SCHEMA**

  

Make sure your schema contains the following:

-   name
-   temperature
-   condition
-   conditionPic

  

----------

#### **EXTERNAL API**

  

There are [a lot](https://www.programmableweb.com/news/top-10-weather-apis/analysis/2014/11/13) of different weather APIs you can work with. We recommend using [open weather map](https://openweathermap.org/) as it's free and fairly simple. But you're free to use a different API if you'd like.

  

**Note:** _If you choose to use a different API, do not spend more than 30 minutes trying to figure it out, as this is not the point of this project. The rest of the API directions will be tailored for open weather map_.

  

You'll need to sign up in whichever way you prefer. Once you do, you'll be redirected to a page which provides you with your API key. You'll need to use this to query the API, so save it as a variable in your server somewhere.

  

Now that you have access to the external API:

-   Read over the documentation, it's really thorough and nice
-   On your server, set up a route that makes a request to the API
-   Query the API for a _city_ of your choice, you wan't the current data to start with
-   Use postman to test at this point

  

----------

  

#### **SERVER ROUTES**

  

You should have the following routes on your server:

-   A route that takes a `cityName` parameter and return the city data in a response.
	-   Hint: The city is not yet saved in your DB.
-   A route that finds all of the city data saved in your DB, and send it to the client
-   A route that saves a new `City` to your DB (notice this is an object city and not city name)
-   A route that takes a `cityName` parameter and delete the correct city from your DB
