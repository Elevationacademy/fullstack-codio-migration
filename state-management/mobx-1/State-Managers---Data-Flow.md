
#### **Why Do We Need a State Manager?**

  

We know that the state in React is meant to be the single source of truth in our App. But out of the box, there are a couple setbacks with using React's state:

  

-   As our app gets more complex we make more states on more components.
-   We are additionally passing down the state and mutating it, making it difficult to track which state our data is originally in, and what is happening to it over it's journey
-   We need to run `setState` every time we want to change something in our state

  

A state manager does exactly what it sounds like it does, it manages our state for one single source of truth. In MobX, any place we store data as part of our app State is generally called **a store.**

  

**Our state manager (MobX) will keep all of the data in our store, where it will track the changes, and work with react to understand which components can change the store, how they can change the store, and follow the changes being made to help React react to changes in the apps state**.

  

Sounds good right? Let's jump into it!

  

----------

  

#### **MOBX DATA FLOW**

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A1622-0.png)

MobX data flow works like this:

  

-   We have our app **state**, which is our Apps single source of truth
-   **Actions** and events are the only things that can change the state of our app. These are things like on clicks
-   Anything that can be automatically computed should be **derived** from our state when relevant data changes. MobX automatically optimizes these operations based on the changes that are made
-   Similar to **derivations**, **reactions** react to state changes and have some sort of side effect, such as updating the UI