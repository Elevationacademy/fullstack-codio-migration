
In the same JS/HTML files from before, use the data below to:

  

-   Save userStorage to LS
-   Check that it's all good in the browser - access the count of the last item in cart and make sure you get 16

  
```
let userStorage = {
    darkMode: true,
    showSideNav: false,
    defaultResultCount: 9,
    latestMarks: {
        sectionA: 92,
        sectionB: 11
    },
    cart: [
        { id: 3112, count: 2 },
        { id: 812, count: 16 }
    ]
}
```

After trying by yourself, you can see other solutions [here](https://codepen.io/ElevationPen/pen/BgBJav?editors=0010).