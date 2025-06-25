
We've already required the wonders array from `wonders.js` and stored it in the variable `wonders` so its easily accessible within the `server.js` file.

  

But you'll notice that every other object in the array has another key: `visited` - when you add new objects to this array, by default this key should be `false`.

  

Use the post route you created earlier to add the object you received in your route to the `wonders` array - make sure to add `visited: false` to the object first.

  

See [solution](https://codepen.io/ElevationPen/pen/ewWgKP?editors=0010).

  

Finally, of course, we must **end the request-response cycle!** You can use either `res.send` with some message, or simply ``res.end()``

  

Once you do that, you'll see the console log in the browser from the callback of your `addWonder` method in your `main.js`

  

Not only that, but if you **refresh your page (without resetting the server)**, you should see your new Wonder added to the page! _That's_ some nice **MVC** for you.

  

**Spot check:** how can you see the updated results _without_ refreshing the page?

<details><summary>
  Click here to reveal the answer.
</summary>

Invoke `fetch()` inside the POST's callback in your `main.js`!


</details>

</br>

