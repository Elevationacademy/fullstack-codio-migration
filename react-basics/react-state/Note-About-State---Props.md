
Though we often pass data from one component's `state` to its children, and the children retrieve that data using `props` - **the two are not related at all!**

  

We use `props` to retrieve _any data_ passed into a child - not just data passed from `state`!

  

Another note about `state`: **state** **does not always have to be in** **App** - in fact, it can be in _any_ component. But when we share data between components, the data should be stored **in the** **state** **of the closest common parent** - that is not always necessarily `App`