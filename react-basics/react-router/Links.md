
#### **LINKS**

So far we've only been able to access our pages by physically writing out the URL each time - obviously, that's not how we want our users to navigate through our apps. That's where the `Link` tag comes in.

It's syntax is very straight forward

```js
<Link to="/cats">Cats</Link>
```

- **to** : it specifies to which route it will go to. (matches the string to the routes defined in router)


For demonstration, add this inside the ``HogwartNavbar`:

  
```
<Link to="/">Home</Link>
```
  

Pretty straightforward. When you hit this link, it will go to the `/` route. Note that _Home_ in this case is just plain text.

  

Of course, since `Link` is a new component we're using, we're going to have to import it.

**Add it to your imports** from `react-router-dom`, like so:

  
```
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
```
---
