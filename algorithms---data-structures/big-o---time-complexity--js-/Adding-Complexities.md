
Take a look at the following code:

```
const books = {
    A: [{ title: "Alchemist", author: "Pablo" }, { title: "Asmiov's Tales", author: "Issac Asimov" }, { title: "Analysis of Apes", author: "Jane Goodall" }],
    B: [{ title: "Best of Meryl Streep Scripts", author: "Madamme Streep" }, { title: "Boyhood, a Story", author: "Childish Gambino" }],
    //...,
    N: [{ title: "Name of the Wind", author: "Patrick Rothfuss" }, { title: "Nostradamus: Revelations", author: "Dalinar Kholin" }],
    //etc
}

const findBook = function (bookName) {
    let letter = bookName[0]
    let booksStartingWithLetter = books[letter]
    for (let book of booksStartingWithLetter) {
        if (book.title == bookName) {
            return book
        }
    }
}
```

  

Here we have a `books` object, where each key is the next letter of the alphabet, and the value for each letter is an array of book objects whose `title` starts with that letter.

  

The `findBook` function receives a `bookName` string, and uses its first letter to determine which array of books it should search through to find the relevant book.

  

In this case, our time complexity is split into two:

-   We find the relevant array in **O( 1 )**
-   We get the first letter in 1 operation
-   We get the array of books in 1 operation
-   The total is 2 operations, i.e. **O( 1 )**
-   We loop through `booksStartingWithLetter` - this is an **O( n )** operation

  

So our total complexity is: O( 1 ) + O( n ). In such cases, **when we add complexities, we only keep the _bigger_ one**.

  

As such, the complexity for the above code is **O( n )**, because `n > 1`


## Spot check
What is the complexity of the following code?
```
const findBookAndPrint = function (bookName) {
    let letter = bookName[0]
    let booksStartingWithLetter = books[letter]

    booksStartingWithLetter.forEach(b => console.log(b.title))

    for (let book of booksStartingWithLetter) {
        if (book.title == bookName) {
            return book
        }
    }
}
```
<details><summary>
  Click here to reveal the answer.
</summary>
Technically, it's **O( 2n )**:

1.  Printing all the books is **O( n )** - yes, the `forEach` method by definition is **O( n )**
2.  Finding the correct book, again, is still **O( n )**

The sum of **n** and **n** is **2n**

  

But, of course, we ignore constants, so the complexity of the above is still **O( n )**.
</details>