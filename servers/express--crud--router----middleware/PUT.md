
So now we know how to Create or POST new data. Very important.

  

The next step, of course, is to Update, i.e. PUT data. This will allow us to modify existing data.

  

Let's start by configuring a route on our server. Since we will be updating the `visited` status of a single wonder, we're going to name this route ``/wonder`` as well - yes, the same route name as we had for the `app.post` route, but this will be a `put` route - **it's ok to have the same route name for different HTTP methods**!

  

**However**, this route will be a little different: because we are updating a single wonder, we need to know _which_ wonder to update. Typically, we would do this by sending an ID along in the route (something like ``/wonder/:wonderId``) - but we can just use the wonder's `name` instead, since that should be unique.