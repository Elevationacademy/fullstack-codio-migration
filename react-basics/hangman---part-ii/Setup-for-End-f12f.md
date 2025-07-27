
Finally, once all of that is done, you should:

  

-   Display _either_ the letter _or_ an underscore inside of `Solution` - depending on whether the letter has a status of `true` or `false`
    -   For this, you should simply pass an underscore or the letter from `Solution` down to `Letter`
-   Display _either_ the letter _or_ the letter crossed-out inside of `Letters`, depending on the letter's status
    -   In this case, you'll be passing down a letter no matter what, but you should **pass a different** **className**  depending on the status
    -   Then add some CSS to differentiate between a selected and non-selected letter
    -   For instance, you could use `text-decoration: line-through;` to show a line over the letter

  

You can use the following `letterStatus` object to test your work. You should - **for testing purposes only** - hard-code this into your `App`'s `state`, then make sure the results are as you expect:

  
```
{
        A: false,
        B: false,
        C: false,
        D: false,
        E: true,
        F: false,
        G: false,
        H: false,
        I: false,
        J: false,
        K: false,
        L: false,
        M: false,
        N: false,
        O: false,
        P: false,
        Q: false,
        R: false,
        S: true,
        T: false,
        U: false,
        V: false,
        W: false,
        X: false,
        Y: true,
        Z: false
      }
```
  

If you **change your secret** **word** **to BYTES**, you should see only the letters `Y`, `E`, and `S` in the solution, and the same letters crossed out from your Available Letters:

  

![](.guides/img/lesson-4.png)

  

Now the only thing left to do is to allow the user to click on each letter and change each status on click. That's not a task for right now - but we're almost done!