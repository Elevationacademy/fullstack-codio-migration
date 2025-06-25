Create your own React project using 
```console
$ npx create-react-app
```
or use an existing one to practice the spot checks in this lesson.

----------

  

In  **App.js** add a `Sum` component. 
```js
export function Sum() {
	// your code here...
}
```
Inside of this component, please follow these instructions:

  

-   Define two variables, `num1` and `num2` 
-   You should render the sum of the two numbers in a simple `div`
-   Change (for this practice only) the **index.js**'s `ReactDOM.render(...)` to render your component instead of `App`
-   Take note of the `export`/`import` ;)

  

<details>
  <summary>
     See our solution if you're stuck
  </summary>

```js
// App.js
export function Sum() {
	const num1 = 9
	const num2 = 3
	return (
		<div>
			The sum is {num1 + num2}
		</div>
	)
}

// index.js
import {Sum} from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Sum />
  </React.StrictMode>
);
```
</details>
  
<br/>
Using components, **we allow React to handle all the _put-this-data-on-the-DOM_ part** - we just have to create a component that describes _what_ to put on the DOM, and how it should be displayed.
