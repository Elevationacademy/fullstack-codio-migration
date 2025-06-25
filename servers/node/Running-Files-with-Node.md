
Now for the good stuff: executing JS code from a _file_ using node.

  

Create some dummy JS file, and write some code that has some console output in it. Maybe a console log, maybe a function call - you're the boss here.

  

Now, in your terminal - make sure you're in the same directory as your file - then type: node yourFileName.js and hit enter.

  

Shablam! You should see your code's output in the terminal. Maybe not terribly exciting yet but this is certainly a much friendlier way to test your JS code, as opposed to creating an HTML file, connecting it to JS, and running it in the browser. Definitely better then copy-pasting code into the browser's console and trying to run it there.

  

**Spot check:** Copy+paste the following code into your dummy JS file, run it, and solve the problem. Notice how much easier it is to work with JS in this way!

  
```
const enemies = [
    { e: "Plastic" },
    { e: "Cigarettes" },
    { e: "The Man" }
]

for (let enemy in enemies) {
    console.log(enemy.e)
}
```