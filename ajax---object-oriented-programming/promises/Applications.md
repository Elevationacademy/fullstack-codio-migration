
Promises are useful mainly in **two situations**:

  

1.  When we have a series of async calls whose results depend on one another (as above)
2.  To detach our async calls (mostly GET requests) from callbacks (example below)

  

Consider the following code:

  
```
class APIManager {
    fetch() {
        return $.get('/data')
    }
}

class Renderer {
    render(dataPromise) {
        dataPromise.then(function (data) {
            $("#body").append(`<div>${data}</div>`)
        })
    }
}

const apiManager = new APIManager()
const renderer = new Renderer()

let initialDataPromise = apiManager.fetch()
renderer.render(initialDataPromise) //initial page load

$(".some-thing").on("click", function () {
    let newDataPromise = apiManager.fetch()
    renderer.render(newDataPromise)
})
```
  

The upside to this is that we don't have to use a callback, so we can pass our promise around like a normal object.

  

Specifically, we can make the API request wherever, then store the _promise_ of that data in a variable, and **resolve** it elsewhere.

  

In this case, we're resolving our promise inside of `render` - which is the downside.

  

The "bad" thing about this is that now our `renderer` isn't a dumb, simple, plain, stupid "renderer" anymore - it actually has to do some logic.

  

So again, there is no hard-and-fast rule that says you _must_ use promises, but they can be helpful.