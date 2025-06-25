
To that end, go ahead add the following to your **server**:
```
const data = {
    8112: {
        title: "Name of the Wind",
        author: "Patrick Rothfuss"
    },
    9121: {
        title: "The Catcher in the Rye",
        author: "J.D. Salinger"
    },
    1081: {
        title: "The Giver",
        author: "Lois Lowry"
    }
}
```
  

Add a route called ``/books`` that takes a `booksID` parameter, and returns the correct book data given the above object.

  

See [solution](https://codepen.io/ElevationPen/pen/XLRNXN?editors=0010).