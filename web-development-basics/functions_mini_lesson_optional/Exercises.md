# Exercises

## Instructions
    
    Alright now you.
    
    1.  Create the other functions. Make this bad boy work.
    2.  Write a loop that calls `getSummary` for each person.
    
      
    
    ----------
    
      
    
    Next, you'll have to write everything from scratch. Given this setup:
    
```js    
    const story = "In the beginning there was light. Then there were wolves. 
      Finally there was a big fire. Ultimately, Shelob the wolf-master put out the fire with her feet. But until then, 
      the fire caused one heck of a lot of damage."
    const specialChars = [",", ".", "'", '"',"?", "!", ";"]
    const wordCounts = {}
```    
      
    
   You have to write a program that counts the unique words in `story`, and stores them in the `wordCounts` object.
    
      
    
   If you do it right, when you `console.log(wordCounts)` in the end, it should look like this:

```js    
    { 
      in: 1,
      the: 4,
      beginning: 1,
      there: 3,
      was: 2,
      light: 1,
      '': 6,
      then: 2,
      were: 1,
      wolves: 1,
      finally: 1,
      a: 2,
      big: 1,
      fire: 3,
      ultimately: 1,
      shelob: 1,
      'wolf-master': 1,
      put: 1,
      out: 1,
      with: 1,
      her: 1,
      feet: 1,
      but: 1,
      until: 1,
      caused: 1,
      one: 1,
      heck: 1,
      of: 2,
      lot: 1,
      damage: 1 }
  ```  
      
    
   Notice that though `story` has upper case letters and special characters, the resulting `wordCount` does not - you need to lowercase _and_ remove special characters.
    
      
    
   Do this with at least three separate functions. I suggest at least: one that adds to the counter, one that cleans the text, and one to actually start everything.
    
      
    
   **Guidelines/Hints:**
    
   -   Do this one step at a time
	    -   First design the "big" function that will call the other functions
	    -   Then start implementing one function at a time and make sure they work individually
	    -   Finally, put it all together
    -   Don't do things by hand - loops are your friends!
    -   If you have a sentence `s`, you can do `s = s.split(",").join(" ")` to remove all the commas from s
    -   You can also use `.split(" ")` to turn a string into an array of words: `"this string".split(" ")` will return `["this", "string"]`
    
      
    
   -------------------
    
      
    
   If you've been working on this for more than 10 minutes with little or no headway, see the more detailed hint below. Though, of course, it's better to ask for help first.

    

 <details><summary>
  Click here to reveal the answer.
</summary>   
   Set up a `countWords` function - this should have `sentence` as an argument, and return nothing.
  This function will
    
   -   Call a `cleanText` function that takes a sentence and returns an array of words that are lowercased and without special characters
    -   Loop through this new array and call `addToCounter` for each word
    
   The `addToCounter` function takes one argument: `word` and either adds it to `wordCount` with a value of 1 if it's not there, or increases its current value by 1 if it is
    
      
    
   If you're still stumped - no worries, this can be tricky - here's some [boilerplate](https://codepen.io/ElevationPen/pen/NZRqqg?editors=0010) to organize things for you.
 </details>   
      
    
   ----------


    
   **DONE**
    
      
    
   That's good practice. Keep writing functions like this in the future - it will serve you well!
