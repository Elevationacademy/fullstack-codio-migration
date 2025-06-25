
Alright, You've just digested quite alot of information, take a quick break; do some squats to let it sink in before starting this.

  

From scratch, make a few Schemas:

-   A **Solar System** with:
-   planets (an array of Planet objects)
-   starName (a String)
-   A **Planet** with:
-   name (String)
-   system (System object)
-   visitors (array of Visitor objects)
-   A **Visitor** with:
-   name (String)
-   homePlanet (Planet object)
-   visitedPlanets (array of Planet objects)

  

Once those are set up, enter a few fields in your DB. You can make up your own planets, but make sure you're using what we learned above (reference IDs).

  

With everything ready, make the following queries using what you know about population:

-   Find a visitor's list of visited planets
-   Find all the visitors on a planet
-   Find all the visitors in a system (subdocuments!)

  

_* If you've finished all the queries above and have more lessons ahead, please head to the next lesson and get started. Otherwise continue to the following queries :)_

  

-   Find the name of the star in the system of a visitor's home planet
-   Find a planet's system's star name as well as its visitors
