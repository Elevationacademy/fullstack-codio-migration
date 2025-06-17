# Exercises: Loops


## Exercise 1
-
Given the following setup:

  
```js
const names = ["Ashley", "Donovan", "Lucas"]
const ages = [23, 47, 18]
const people = []
```
  

Write a loop that populates (adds to) the people array with objects, that have a name and age, like this:

  

{name: "Ashley", age: 23} 

  

Ultimately, when you console log people, it should look like this:

  
```js
  {name: "Ashley", age: 23},
  {name: "Donovan", age: 47},
  {name: "Lucas", age: 18}
```

## Exercise 2 (Extra Practice)
-
Based off the `people` array from before, write a loop that prints out "Ashley is 23 years old", "Donovan is 47 years old", etc.

  

Again, consider which loop is most appropriate.

  

Note that this is _different_ from Exercise 1 ;)



## Exercise 3
-
**==≡==** The following exercises are a little more challenging - but this is a good chance to practice your programmer's mind. **==≡==**

  

Given this array:

  
```js
const posts = [
  {id: 1, text: "Love this product"},
  {id: 2, text: "This is the worst. DON'T BUY!"},
  {id: 3, text: "So glad I found this. Bought four already!"}
]
```
  

Write some code that removes the post with an `id` of 2 from the `posts` array. Can't have any negative reviews of our product!

  

Obviously, do not do `posts.splice(1, 1)` - you have to _find_ the post to remove! (Of course, you _will_ use `splice` - just not hard coded!)



## Exercise 4
-
Given this array:

  
```js
const posts = [
  {
    id: 1, 
    text: "Love this product",
    comments: []
  },
  { 
    id: 2, 
    text: "This is the worst. DON'T BUY!", 
    comments: [
                {id: 1, text: "Idiot has no idea"}, 
                {id: 2, text:"Fool!"}, 
                {id: 3, text: "I agree!"}
              ]
   },
   {
    id: 3, 
    text: "So glad I found this. Bought four already!",
    comments: []
   }
]
```
  

You are given `2` as the ID of a _post_. Write some code that finds the _comment_ with an ID of `3` (inside of a _post_ with an ID of `2`), and remove just that one comment.


Extension
-
There is something called [Object.keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) - read about this, and then do the following exercise:

  

Given the object below:

  
```js
const dictionary = {
  "A": ["Aardvark", "Abacus", "Actually", "Atomic"],
  "B": ["Banana", "Bonkers", "Brain", "Bump"],
  "C": ["Callous", "Chain", "Coil", "Czech"]
}
```
  

Write some code that prints out the following:

  
```js
Words that begin with  A:
    Aardvark
    Abacus
    Actually
    Atomic
Words that begin with  B:
    Banana
    Bonkers
    Brain
    Bump
Words that begin with  C:
    Callous
    Chain
    Coil
    Czech
```

**Hint 1:** You will have to use what's known as a **double for loop** - that means a for loop _within_ a for loop.


**Hint 2:** Start small; only print out "Words that begin with..." at first, then keep going

----------

  

## **DONE**
```js
while(!done){

  while(headHurts){
    // massage your head
  }

  // keep going for another 20 minutes
}

// celebrate
```
