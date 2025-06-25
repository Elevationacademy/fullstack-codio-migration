## Exercise 1

Given the following JSON:

  
```
{
  "name": "Mashed Potatoes",
  "serves": 4,
  "ingredients": [
    {
      "name": "water"
    },
    {
      "name": "potatoes",
      "count": 2
    },
    {
      "name": "butter",
      "count": 2,
      "unit": "tablespoons"
    },
    {
      "name": "salt",
      "count": 0.5,
      "unit": "teaspoon"
    },
    {
      "name": "pepper",
      "count": 0.25,
      "unit": "teaspoons"
    }
  ],
  "directions": [
    "Add potatoes to a pot and cover with an inch of water.",
    "Bring the water to a boil over high heat, then reduce to a simmer and cover.",
    "Simmer for 20 minutes or until potatoes are fork tender.",
    "Drain water from potatoes, leaving the potatoes in the original pot.",
    "Add remaining ingredients to the pot with the potatoes.",
    "Mash potatoes until they reach the desired consistency.",
    "Serve immediately, or cover and refrigerate."
  ]
}
```
  

Note that the first ingredient does not have a count or unit, and second ingredient doesn't have a unit. Though **it is common to have consistent keys** in objects that exist in an array, there is nothing that enforces this inherently in JSON.

  

**Modify this to include a new ingredient**: 2 teaspoons of garlic powder.

## Exercise 2

Add some more JSON to include the following information (use reasonable names for new keys):

  

-   This contains 250 calories
-   It is a healthy meal
-   Insert a new direction at the beginning: "Cut potatoes into half inch thick slices"

  

To make sure you got Exercise 1 & 2 right, copy & paste the following code and check that your console logs match the comments. Note that you may have used slightly different keys - use your head ;)

  
```
let recipe = //YOUR JSON HERE

console.log(recipe.ingredients.filter(i => i.name == "garlic powder")[0].count) //should print 2
console.log(recipe.healthy) //should print true
console.log(recipe.calories) //should print 250
console.log(recipe.directions[0]) //should print "Cut potatoes into half inch thick slices"
```
  

Remember, JSON is valid JS, so you can just initialize your JSON right into a variable and use it normally!

## Exercise 3
![](./2.jpg)


**Design a JSON document** that describes different kinds of animals. **Don't actually write out any JSON yet**, just the keys.

  

Your document should be able to answer the questions below. Think about which keys your JSON will have that make most sense.

  

-   What is the animal's name?
-   How much does the animal weigh? In kilograms? In tons?
-   Where does the animal live?
-   Is it endangered?
-   What different kinds of foods does it eat?
-   What are the names of other animals that eat it?
-   How delicious is the animal, on a scale of 1 to 5?

  

Where will you use strings, numbers, booleans, objects, arrays?

**Hint:** given the above questions, you should be using all of these.

## Exercise 4

Once you've decided on your keys, write out some JSON for one of the following animals:

  

1.  [Cow](https://en.wikipedia.org/wiki/Cattle)
2.  [Elephant](https://en.wikipedia.org/wiki/Elephant)
3.  [Gray Wolf](https://en.wikipedia.org/wiki/Gray_wolf)
4.  [Squirrel](https://en.wikipedia.org/wiki/Squirrel)

## Follow Up Questions

-   Did you have to change the structure of your JSON document at any point while you were filling it out for the different animals?
-   Does the format you chose make later additions to the data easy?
-   Now we want to know how much of each kind of food each animal eats, as a percentage of its overall diet. **Modify your JSON document format as necessary to accommodate this**.

  

----------

  

{"DONE" : true}

  

That was a lot of JSON - but this is super fundamental for communicating between machines, which we will be doing!