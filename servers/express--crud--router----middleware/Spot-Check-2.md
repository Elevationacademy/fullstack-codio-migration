
Go ahead and create a `put` route that accepts a `name` parameter on your own. For now, just have a console log in the callback so you can see that it works.

  

See [solution](https://codepen.io/ElevationPen/pen/OemWop?editors=0010).

  

As for making an actual PUT request - unfortunately, jQuery doesn't have a built-in ``$.put`` like it does for GET and POST, so we'll have to use ``$.ajax``, where our `method` parameter will be ``"PUT"``. And of course, we'll do this in a function that will get invoked when we press any of the `visit` buttons. It should look like this:
```
const updateVisited = function (wonder) {
    $.ajax({
        url: `wonder/${wonder}`,
        method: "PUT",
        success: function (response) {
            console.log("PUT complete")
        }
    })
}
```
  

Towards the end of `main.js` you should see a click handler that's listening for clicks on elements with a class of `visit` - this is where you should be invoking the `updateVisited` function. **However, notice that when we extract the wonder, we get it with the location, like this:** `Grand Canyon - Arizona` - but we're only interested in `Grand Canyon`.

Use [split](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split) and [trim](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim) to get what you want.

(This is a fun JS challenge not related to express)

  

See [solution.](https://codepen.io/ElevationPen/pen/jjmyeZ?editors=0010)

  

Now if you save & refresh your server and page, then click on a `visit` button, you should see the console log in your server, alerting you that someone has accessed your `put` route. Go ahead and **console log** **req.params.name** in your PUT route in `server.js` as well to make sure it got to the server as expected.

  

**Spot check:** of course, all that's left now is to actually change the `status` value of the `wonder` you received in the route to `true` - so go ahead and do that in your ``app.put(wonder/:name...`` route.

  

**Note:** Don't forget to ``response.send()``

  

See [solution](https://codepen.io/ElevationPen/pen/ewWvpo?editors=0010).

  

And of course, add another ``fetch()`` call in your PUT's callback to see all the updates instantly ;)