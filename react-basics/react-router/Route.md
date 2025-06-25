
#### **ROUTE**

  

Alone, `Router` doesn't do anything. But now we'll introduce a new component called `Route`.**a route renders some UI when a location matches the route's path**.

The `<Route>` is a  component that is used to define a route.
 It takes two props: `path`,`element` .
- **path** : it specifies the URL path to match.
- **element**: specifies the component to render when the path is matched. 

**For example**, 

```js
<Route path="/home" element={<Home />} />
```

matches the `/home` path and renders the `<Home>` component.


Before we implement it, take a look at `Home.js` in the `components` folder. You'll see some HTML there that represents our `Home` component - our landing page - but we don't see it in the browser. Ideally, when a user goes to our **home** route, also known as the **root** route, we want them to see this HTML.

  

To do that, add the following code in `App.js`, in between the **Router**:

  
```
<Route path="/" element={<Home categories={categories} />} />
```
####   

We will see that it will not work, that is because React Router demands you to wrap all your routes with a **Routes** Component.
  
So our code should look like this:

```js
  return (
    <Router>
      <div className="App">
        <HogwartNavbar />
      </div>
      <Routes>
        <Route path="/" element={<Home categories={categories} />} />
      </Routes>
    </Router>
  );
```

  

*You'll also want to make sure you import the `Home` component in `App.js`

  

Once you've added that, save and look at your page again - wa-bam, what a landing page.

You'll notice that nothing is click-able yet - we'll fix that in a bit.

  

Using the `component` attribute in the `Route` tag is well and fine for rendering a simple, dumb, static, basic, data-less component like `Home` - but once we want to start passing data down, we'll want to use the `element` attribute.

---

Notice, the **Route** acts like a page, it changes depending on which path we are in.
If we define a **Route** like this:

```js
<Route path="/cats" element={<Cat/>} />
```

this route will display the `<Cat/>` component when we are in :

```
http://localhost:3000/cats
```

And note that in this example code:

```js
  return (
    <Router>
      <div className="App">
        <h1>Hello!</h1>
      </div>
      <Routes>
      <Route path="/cats" element={<Cat/>} />
      <Route path="/dogs" element={<Dogs/>} />
      <Route path="/owls" element={<Owls/>} />
      </Routes>
    </Router>
  );
```

We will see a page with a header of **Hello!** and depending on the route we will see a component.

Meaning in :
```
http://localhost:3000/cats
```

We will see Hello! and the rendering of cat components.

And in :
```
http://localhost:3000/dogs
```

We will see Hello! and the rendering of Dog components.

