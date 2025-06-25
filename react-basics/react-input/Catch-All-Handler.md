
You now understand the basics of handling input in React. And honestly, there's not much more to it.

  

The only "issue" might arise when you have multiple inputs, and you need multiple methods to manage the state changes.

  

There's nothing inherently wrong with having a method for each input element - you may very well want to do different things for each input.

However, When we are dealing with states in general we want to combine states that have a common ground into one state.
This allows us to have generalization in our code.

**That said**, it is silly to have several methods that do exactly the same thing: update one property of `state`.

To that end, **take a look at** [**Handling Multiple Inputs**](https://medium.com/nerd-for-tech/how-to-build-forms-with-multiple-input-fields-using-react-hooks-677da2b851aa).

  

They show a clever use of **ES6**'s [computed property names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#Computed_property_names) syntax in conjunction with the name attribute.

  
