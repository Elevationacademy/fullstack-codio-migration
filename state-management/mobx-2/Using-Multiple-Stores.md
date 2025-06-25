
Ideally, when building a large app, we will want to separate our data

into different sections, based on what data is relevant to which section of the app.

  

The best practice with MobX is to build multiple stores, for easy separation of data concerns.

This way, we can use multiple stores with `Provider` and `Inject` to only access the data we need, where we need it. Awesome!

  

In this project, we are doing this by enabling two-way-binding through a MobX!

  

In React, we used two way binding to ensure that we were saving the values of our inputs when working with inputs.

  

While you can still do this through running `setState`, we're going to show how you can save your values in another way, using a MobX store. Neither way is particularly better than the other, this is just a good example of working with multiple stores.

  

Let's see this in action by looking at our `stores/GeneralStore.js`

  

You'll notice this is a pretty simple store, only two `observable`s and an `action`. The action is a handler that updates the value of the `observable`s.

  

Now take a look at the inputs in `src/components/ResInput.js` and the `InputHandler` function there. In short:

-   The inputs are running the `inputHandler` `onChange`
-   The `inputHandler` is sending the name and value of the input to the `handleInput` action in the `GeneralStore` which is updating the values of our `observable`s

  

**Why is this good?**

  

Since we can `inject` multiple stores where we need them, we can now access the values of our inputs from our `GeneralStore` where we need it. **Thus, we are still binding input values to our application state, and have them available _wherever_ we need them**.