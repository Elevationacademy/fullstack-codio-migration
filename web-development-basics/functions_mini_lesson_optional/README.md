# Functions Galore

Say I have the following data:

```js
people_info = [
  {
    name: "guido",
    profession: "bungalow builder",
    age: 17,
    country: "canaland",
    city: "sydurn",
    catchphrase: "what a piece of wood!"
  },
  {
    name: "petra",
    profession: "jet plane mechanic",
    age: 31,
    country: "greenmark",
    city: "bostork",
    catchphrase: "that's my engine, bub"
  },
  {
    name: "damian",
    profession: "nursery assistant",
    age: 72,
    country: "zimbia",
    city: "bekyo",
    catchphrase: "with great responsibility comes great power"
  }
]
```
  

And say I want to write up a basic summary of each person, _but_:

-   All proper nouns* should be capitalized
-   The city and country should come together with a comma in between
-   If the age is below 21, it should say "Underage" instead
-   If the age is above 55 it should say "55+" instead
-   The catchphrase should be wrapped in quotes with its first letter capitalized

##### ***for this exercise, everything except** **`age`** **is a proper noun**

  

What I really want is to have one function that, given data about a person, will give me a string with that information:

  

```js
const getSummary = function(person){
  let summary = ""//modify the summary string with the person parameterreturn summary
}
```
  

Then I could do something like `const summary = getSummary(people_info[0])` and I'd have what I want.

  

If something doesn't make sense so far **ask a friend or instructor** right now. Do not skip ahead, it will not make sense.

  

----------

  

So let's start with the first requirement - I want all proper nouns to be capitalized. I could write some code inside `getSummary` - but I still have other requirements to meet, and so this function will get pretty bloated fast if I do that. Therefore, I will **call a different function** to fulfill these sub-tasks for me.

  

The function I'm interested in will take a string and return a capitalized version of that string:

```js
const capitalize = function(str){
  let capitalizedStr = ""
  capitalizedStr += str[0].toUpperCase(); //add the first letter of the str, capitalized
  capitalizedStr += str.slice(1) //add the rest of str normallyreturn capitalizedStr
}
```
  

Ok that's great, but now I need to actually call that function somewhere. We will do that back in `getSummary`:

  
```js
const getSummary = function(person){
  let summary = ""
  summary += capitalize(person.name)
  //more modifications to comereturn summary
}
```
  

Do you see where we're going with this? The `getSummary` function will only be in charge of calling other functions that do the actual work.

  

We will call each of the other functions to _add_ to the `summary` variable which we will eventually return.

  

By the way, another great thing about separating functions like this is that now I can test `capitalize` independently!

Try it out for yourself. Write out `capitalize` and then call it with a few different words, watch it work.

  

In the end, your `getSummary` function should look like this:
```js
const getSummary = function(person){
  let summary = ""
  summary += capitalize(person.name)
  summary += ` is ${getAge(person.age)} ` //Yes - you can put a function call inside the tick quotes!
  summary += //call function for profession
  summary += //call function for country + city
  summary += //call function for catchphrasereturn summary
}
```
  

And if I do `console.log(getSummary(people_info[0]))` I should see:

_Guido is an underage Bungalow Builder from Sydurn, Canaland. Guido loves to say "What a piece of wood!"._

  
```js
console.log(getSummary(people_info[1]))
```
_Petra is 31 year old Jet Plane Mechanic from Bostork, Greenmark. Petra loves to say "That's my engine, bub"._

  

    console.log(getSummary(people_info[2]))

_Damian is a 55+ Nursery Assistant from Bekyo, Zimbia. Damian loves to say "With great responsibility comes great power"._

  

----------

  

This is a broad topic known as **separation of concerns** - that is to say, **each function should do one and only one thing**

  

The `getSummary` function gets the summary pieces from other functions - done.
The `capitalize` function capitalizes a single string - done.
The `getAge` function returns a different representation of an age, depending on some conditions - done.

etc.

  

Notice that when my code is separated like this I can **reuse** functions to my heart's content (see how many times I used capitalize?
