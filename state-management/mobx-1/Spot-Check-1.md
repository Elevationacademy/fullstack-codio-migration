
Now, **go to the class called** **`ShoppingList.js`**. It should have a class ShoppingList with two properties:

-   `list`, an empty array by default
-   `length`

  

Go ahead and make those properties `observable`.

Check out the solution:

<details>
<summary>Solution</summary>


```js
import { observable, makeObservable } from 'mobx'


export class ShoppingList {
    constructor() {
        this.list = [];
        this.length=0;
      
        makeObservable(this, {
          list: observable,
          length: observable
        })
    }
    //other methods
}
```

</details>


