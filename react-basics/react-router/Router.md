
#### **ROUTER**

  

We got something called a **React Router** from the `react-router-dom` package. This is what we'll use to handle all our routes.

  

So as with everything React-y, we'll need to import it. Before we do that, let's **take a look at** **App.js**:

  
```
const App = (props) => {
  const [categories, setCategories] = useState(CATEGORIES);
  const [potions, setPotions] = useState(POTIONS_DATA);
  const [charms, setCharms] = useState(CHARMS_DATA);
  const STATE_MAP = {
    potions:potions,
    charms:charms
  }

  const getCategoryData = (category) => {
    return STATE_MAP[category];
  }

  return (
    <div>
        <div className="App">
          <HogwartNavbar />
        </div>
        {/* add routes and route here */}
    </div>

  );
}

```
  

Looks like a lot - but really it's just the `state` and some minor boilerplate in the `return`

######   

###### **Quick word on our app's data**: we should be pulling it from some API/our server - but for this example hard coding will do fine.

###### As you can see, the data in there is everything that will appear on our app once everything is working (reference the gif from before)

  

For starters, we'll want to wrap our _whole_ app with that **React Router** we talked about. We can see this in top of `App.js`.
  
```
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

```
  

The React Router is called `BrowserRouter` initially, but we'll shorten it by using the alias `as`.

  

The **BrowserRouter** **uses the** [**HTML 5 History API**](https://developer.mozilla.org/en-US/docs/Web/API/History_API) **to keep our UI in sync with our URLs** (our routes). For instance, if we're on `http://localhost:3001/wiki/charms/Accio` - we should see a page with information about the charm Accio!

  

With the above import we now have access to a `Router` tag (which is a React component) and we're going to nest our whole app inside of it, like so:

  
```
  return (
    <Router> {/* Wrapping everything with Router */}
      <div className="App"><div id="home-background"></div><div id="main-links">
          {/* Main Links */}
        </div>
        {/* Routes go here v */}

        {/* Routes go here ^ */}
      </div>
  </Router>
);

```

(just an example)

Now we'll be able to use routes inside our whole app.