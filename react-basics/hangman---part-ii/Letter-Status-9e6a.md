
In Hangman, the user selects a letter, and if the letter is part of the secret word, it should appear on the screen.

  

You might think to store all the letters in an array, but to save you a headache, we suggest **creating an object called** **letterStatus** **that looks like this:**

  
```
{  
  "A": false,
  "B": false,
  ...
}
```
  

You should **store** **letterStatus** **in your** **App****'s state** - use another method called `generateLetterStatuses` to create this object.

  

Generating this object is a bit of a logical challenge*, but we're learning React right now so don't burn too much time on it. [Here](https://codepen.io/ElevationPen/pen/dLgErj?editors=0010) is the solution if you're spending more than 20 minutes on this.

  

***Hint:** part of the trick uses [ASCII characters](https://www.asciitable.com/). For instance, the number 65 represents the letter "A" in ASCII, 66 represents "B", and so forth until 90 which represents "Z".

  

***

  

The reason this object is a good idea is because **it will allow us to easily track which letters the user has already selected**, and which they haven't.

  

Think about it this way, there are two main parts to this game: the letters of the secret word, and the place where the user can select the letters:

![](.guides/img/lesson-2.png)

We want to make sure that if the letter C is selected, that we store that information in a single place.

  

The `letterStatus` object is perfect for that, because it is one object that the other components will receive as `props` - then they will both be aware of any changes, and render accordingly!

  

In the above image, we can imagine that a if C has a status of `true`, then it should appear in the top part, and be greyed or crossed out in the bottom part. On the other hand, the letter A has a status of `false`, so it shouldn't appear yet on top, and still be available below.