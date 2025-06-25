
Go to this [GitHub repo](https://github.com/Elevationacademy/mobx-1-lesson-exercises-updated) **fork** it, and then **clone** it.

  

Don't forget to run `npm install` and then `npm start`

  

----------

  

Now, in your repo's `src` folder go to the folder called `stores`. Inside stores, check out the file `Item.js`. It should look like this:


```
import { observable, makeObservable } from 'mobx'

export class Item {
    constructor(name) {
        this.name = name
        this.completed = false

        makeObservable(this, {
            name: observable,
            completed: observable
        })
    }
}
``` 

Let's unpack this code a bit:

  
-   We start by importing `observable` & `makeObservable` from our MobX package.
    -   Signifying that a property is `observable` means we want to watch this property for changes.
    -   `makeObservable` is a function that, when invoked, allows us to tell MobX which properties are `observable`.
-   We then create a new class `Item` and in its `constructor`, we:
    -   Create two properties, `name` and `completed`
        -   `name` - is initialized to the parameter that is passed to the `constructor`
        -   `completed` - is initialized to a default value of `false`
    -   Invoke the `makeObservable` function and pass it two arguments, a class instance (in this case `this`) and an object that signifies which properties are `observable` (and will need to tracked by React as the state).
        -   Note, we can tag certain properties differently (not just `observable`) but we'll see that later on.
-   Then, we export our class to use later.