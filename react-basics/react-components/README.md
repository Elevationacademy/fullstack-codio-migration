# Child Components

Now, even though we saw that we can put any JSX inside the `App`'s `return`, we're going to do something a little different.

We're going to load **child components** in there, instead.

  

React is _built_ around components. If we put all our JSX in one place, it would defeat the purpose.

  

Consider this code:

  

```js
function Nav() {
	return (
		<div id="nav"><span>Home</span><span>About</span></div>
	)
}

function App() {
	return (
		<div className="app">
			<Nav /> {/* loading a child component */}
			<div>Welcome!</div>
		</div>
	)
}
```
  

Generally, **you should create a new file for each component** - but for the sake of this example, we're keeping it all in one file.

  

Here we have two components, where the `App` component is **loading** the `Nav` component.

  

We say that `App` **is a parent of `Nav`, and `Nav` is a child of `App`** - this should come as no surprise as it is very familiar to our HTML/DOM hierarchy.

  

Also notice the syntax: **when we create a component, we can use it like an "HTML" tag** - angled brackets and all.