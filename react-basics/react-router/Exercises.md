## Exercise 1

Now that we learnt basic React routing, its time to put it to the test!

Now to truly test it, let's go to the `CategoryList.js`.

We want to add `Link`s to potions and charms.

first, add this `Route` in `App.js` (add in Routes tag) 

```js
<Route path="/wiki/:category" element={<Entities getCategoryData={getCategoryData} />} />
```

The link should send render `Entites` component.


## Exercise 2


The last thing that's really missing is getting from our app, is the desciprition of each item.

Which we saw in the URL if you recall:

```js
http://localhost:3001/wiki/charms/Accio
```

- create a `Route` that shows description
- create a `Link` that sends you there

Check out these hints if you are stuck on one of those:

<details>
  <summary>
     Route
  </summary>

you need to create a route that accepts a parameter that you can extract later on (check useParams)
</details>


<details>
  <summary>
     Link
  </summary>
when you are mapping the Entity, make sure to wrap it with a dynamic Link (meaning a link in which the url depends on the array)
</details>

## Extension:

Go through out the project and look  to add routes and links where it makes sense.
