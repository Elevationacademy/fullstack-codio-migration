## Exercise 1

Create a StringFormatter module. It should have two functions:

  

1.  capitalizeFirst - receives a string and returns the string with the first letter uppercased, and the next ones lowercased
2.  toSkewerCase - receives a string and replaces any spaces with a dash

  
```
const formatter = StringFormatter()

formatter.capitalizeFirst("dorothy") //should return Dorothy
formatter.toSkewerCase("blue box") //should return blue-box
```

## Exercise 2

Create a Bank module. It should have a variable and two functions:

  

1.  A private money variable which starts off at 500
2.  A depositCash function which takes a cash parameter and uses it to increase money
3.  A checkBalance function which logs the money

  
```
const bank = Bank()
bank.deposit(200)
bank.deposit(250)
bank.showBalance() //should print 950
```
  

The above is not a mistake. The names are purposefully different from the instructions. Understand why?

## Exercise 3

Do you ever get tired of going to YouTube for a song, typing the name in, finding the right video, then selecting it? Ugh.

  

Let's make a simple SongsManager. Here is the desired result:

  
```
const songsManager = SongsManager()
songsManager.addSong("sax", "https://www.youtube.com/watch?v=3JZ4pnNtyxQ")
songsManager.addSong("how long", "https://www.youtube.com/watch?v=CwfoyVa980U")
songsManager.addSong("ain't me", "https://www.youtube.com/watch?v=D5drYkLiLI8")

songsManager.getSong("sax") // should print https://www.youtube.com/watch?v=3JZ4pnNtyxQ
```
  

Effectively, you will be creating a hyper-specific, YouTube Song Manager object.

Did you notice that each URL starts the same way?

  

Inside of SongsManager there should be a songs object, _but_, instead of saving songs like this:

  
```
const songs = {
  "sax": "https://www.youtube.com/watch?v=3JZ4pnNtyxQ",
  "how long": "https://www.youtube.com/watch?v=CwfoyVa980U"
}
```
  

The addSong function in SongsManager will make sure that we only save the _identifiers_, like this:

  
```
const songs = {
  "sax": "3JZ4pnNtyxQ",
  "how long": "CwfoyVa980U"
}
```
  

Imagine how much space we'd be saving if we actually had to store this in a database!

  

Of course, when we call getSong - it should give us the full URL!

  

Go ahead, create SongsManager - it should not be a very long function ~

  

Take a crack at this for a good 20-30 minutes. If you're still struggling, ask someone for help. Then, if you're still stuck, here is a guided hint:

<details><summary>
  Click here to reveal the hint.
</summary>

You should start by creating a SongsManager function. Inside of it, define the following:

-   A private songs object
-   A public addSong function that receives the name of a song and its full URL
--   The function should add to the songs object using the name as the key, and URL's identifier as the value
--   That means it should turn this: "https://www.youtube.com/watch?v=ZbZSe6N_BXs" to this: "ZbZSe6N_BXs"
-   A public getSong function that receives a song name, and returns the song's full URL
--   This function should use the name and access the songs object to get the URL identifier, but add on the YouTube base URL

Then, return only the addSong and getSong functions in an object

</details>  

</br>



  

If you've been working on this for more than 50 minutes, check out [this solution](https://codepen.io/ElevationPen/pen/MdxxBO?editors=0010) (it uses arrow functions)

  

----------

  

#### **DONE**

  

Try to work with modules as much as possible. If all your code is modular, it will help you maintain, scale, and debug your code.