## Definition
High-level modules should not depend on low-level modules. 
Both should depend on the abstraction.

Abstractions should not depend on details. 
Details should depend on abstractions.
## Example
Of course we will start with an example.
Let's say we want to count the number of times each letter appears in a string. 
Look at the following function:

```js
function increaseCount(char, charCounter) {
  let count = charCounter[char] || 0
  charCounter[char] = count + 1
}
```

This function receives a char an object that will count the appearances. 

## Question
Does this function violate the Dependency Inversion principle?
<details>
  <summary>
     The Answer is here
  </summary>
    Yes!!
    <br>
    Can you tell in what way?
</details>
<hr>

# Explanation
When we access the count of the  given char by:
```
charCounter[char]
```
we create a dependency upon the implementation of the `charCounter` object.

Can you tell how it is implemented?


<details>
  <summary>
     Click here to reveal the answer
  </summary>
    it is an object with key value pairs, where the key is the char and the value is it's count
    for example:

    {
      "a": 5,
      "g": 2,
      "t": 1
    }
</details>
<br>

So `increaseCount` function knows how `charCounter` is implemented. This is a dependency, where `increaseCount` is dependent on the implementation details of `charCounter`. If we would change the implementation of `charCounter`, we would have to change the `increaseCount` function.

Let's see how it would happen!

We could implement the `charCounter` as an array, where the char that we count will be represented by the array index according to it's ASCII value, and the count will be represented by the value. Since we want to count letters we would want `a` to be mapped to index 0, `b` to 1 and so on.
The ASCII value of "a" is 97 (our algorithms will  be case insensitive, meaning we will count a and A no matter if it is small or capital) so we will want to reduce `97`, so that a will map to 0.
For example:
```js
[0,4,3,0]
``` 
In this example:
The letter a appears 0 times
The letter b appears 4 times
The letter c appears 3 times
The letter d appears 0 times

So now our `increaseCount` function should look like that:
```js
function increaseCount(char, charCounter) {
  let code = char.charCodeAt() - 97
  charCounter[code] = (charCounter[code] || 0) + 1
}
```

Note that we might have other functions that are using `charCounter` and depend on the implementation of it. So now we would have to change all of them...

OH, man... Isn't there a better way?

Of course there is.
Use **ABSTRACTION**

```js
function increaseCount(char, charCounter) {
  let currentCount = charCounter.getCount(char)
  charCounter.setCount(char, currentCount + 1)
}
```

If we hide the implementation on `charCounter` behind an interface, we can now change it without changing the `increaseCount` function.
So if `charCounter` was implemented first as an object:

```js
class CharCounter {
  constructor(){
    this.counts = {}
  }

  getCount(char){
    return this.counts[char] || 0
  }

  setCount(char, newCount = 0){
    this.counts[char] = newCount
  }

}

function increaseCount(char, charCounter) {
  let currentCount = charCounter.getCount(char)
  charCounter.setCount(char, currentCount + 1)
}
```

and now we want to change it to an array with ASCII based mapping. No problem:


```js
class CharCounter {

  constructor(){
    this.counts = []
  }

  getCount(char){
    let charCode = char.charCodeAt() - 97
    return this.counts[charCode] || 0
  }

  setCount(char, newCount = 0){
    let charCode = char.charCodeAt() - 97
    this.counts[charCode] = newCount
  }

}

function increaseCount(char, charCounter) {
  let currentCount = charCounter.getCount(char)
  charCounter.setCount(char, currentCount + 1)
}
```

Note that the `increaseCount` function did not changed!

Boom! This is what we call abstraction.