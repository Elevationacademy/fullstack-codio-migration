# Intro

Welcome to the wonderful world of MobX! This lesson will cover:

  

-   What is MobX
-   Why do we need a state manager?
-   The basics of MobX
    -   MobX data-flow
    -   Creating a Store and Observable
    -   Observer
    -   Actions

  

Let's get MobXing!

  

----------

  

#### **WHAT IS MOBX?**

  

Simply put, MobX is a library for state management.

  

React renders an application state. MobX brings in a new mechanism for storing and updating the state that React renders.

  

As the [MobX documentation](https://mobx.js.org/) says, "MobX provides mechanisms to optimally synchronize application state with your React components by using a reactive virtual dependency state graph that is only updated when strictly needed and is never stale."

  

We'll understand this quote more in depth later, but the important thing to take away from it is that MobX manages passing the necessary information to each react component, and updating the data **only when necessary**.