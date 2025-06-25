
Alright - fun and games is fun..and gamey, but it's time to put handlebars to practice.

  

Start by forking [this repository](https://github.com/Elevationacademy/apartment-seller) and looking around the code a bit. Then come back here for detailed instructions.

  

----------

  

Let's start by understanding what the project is: an apartment listing app.

At the top of the page, you have some inputs that you can fill in to filter the apartments you want to see.

  

For instance, if you enter _1000_ to the Max Price field, you'll only see apartments with a price of $1,000 or below.

  

The code that does the filtering exists for you - that's in apt-filter.js - and you don't need to worry about it for now.

  

The apt-data.js file is just an array of apartment objects - you should explore this file a bit to understand the data you'll be working with.

  

For most of this project, you should only have to make changes in index.html and main.js - so let's talk instructions.

  

----------

  

**To Do**

  

**JS**

In your main.js file you'll have to set up your Handlebars source, template, etc. It's very little code, but make sure you're adding the HTML you genereate to the #results element.

  

To do this, you'll have to work in the renderApts function.

  

Notice that it has an apartments parameter: this is the list of apartments you'll have to render; it's already filtered for you based on the user selection!

  

**Side note:** the main.js file has access to the apartments variable because we have the script of our apt-data.js in our HTML _before_ the script for our main.js - hence apartments is effectively a global variable in main.js

  

----------

  

**HTML**

  

Now for the interesting part.

  

Feel free to **ignore everything inside of the** **div** **with an ID of** **search** - that's not relevant to the Handlebars stuff you'll be writing.

  

You can also **ignore the** **#results** **div** - that's where all your generated HTML will be added.

  

**Important:** Before you get started on the handlebars template, make sure you review and understand the CSS file as you'll need to add the correct classes and id's to render everything properly.

  

**Here's what you need to do:**

  

-   Create the script parameter that will house all your Handlebar HTML
-   Remember that you're working with an array - how do you render each item in the array?
-   Start by just displaying the relevant data - don't worry too much about styling
-   You should only display the contactDetails if the immediate boolean is true - do this through Handlebars, not JS logic
-   You should only display "Parking available"* if the parking boolean is true

  

Don't forget to take advantage of the styling given to you, and wrap your results inside a div with a class of result, and checkout the CSS file for other hints

###### *Instead of displaying "Parking available", use a [font-awesome](https://fontawesome.com/icons?d=gallery) icon for parking instead

  

Again, for starters - forget styling, just make sure everything is rendering.

  

Once you're done with the basics above, do the following:

  

-   If there are no matching results, display a message that says so. [This resource](https://handlebarsjs.com/guide/builtin-helpers.html) will help
-   Check out [this resource](https://www.npmjs.com/package/handlebars-intl) to figure out how to use Handlebars to format your price to a nice currency format. Note you'll need to research something called [npm](https://www.npmjs.com/).

  

Now, if you really wanna _get_ Handlebars, do the following:

  

-   Add a features property to each item in the apartments array - that's in apt-data.js
-   The value should be an **array** of features the apartment has, such has "AC", "Elevator", "Indoor Plumbing", etc.
-   Render each of the features for each of the apartments using Handlebars
    -   This will be an _inner_ each
    -   Remember [this resource](https://stackoverflow.com/questions/20773464/rendering-a-string-array-with-handlebars)

  

----------

  

**Logical Challenges**

  

Do the following for a nice logical challenge:

  

-   You'll notice that the parking checkbox doesn't actually filter
-   Check out the code in apt-filter.js and make it filter!

  

Finally, for a really cool, non-Handlebar related logical challenge:

  

-   Delete the code in apt-filter.js
-   Re-write it yourself
    -   Keep the findRelevantApts function signature
    -   Use those filter parameters and the globally available apartments variable to return a subset of apartments that match the filters

  

----------

  

#### **{{DONE}}**

  

There are many other templating libraries like handlebars, but they all pretty much do the same thing with few variations. Congratulations on learning this one ~