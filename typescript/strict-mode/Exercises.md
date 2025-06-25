## Exercise 1
Will this cause an error?
```
"use strict";
x = 3.14; 
```

<details>
<summary>Solution</summary>
<div> 

`x = 3.14;` will throw an error, as ‘x’ is not declared
</div>
</details>

## Exercise 2
Will this cause an error?
```
"use strict";
myFunction();

function myFunction() {
  y = 3.14;
}
```

<details>
<summary>Solution</summary>
<div> 

`y = 3.14;` will throw an error, as ‘y’ is not declared
</div>
</details>

## Exercise 3
Will this cause an error?
```
x = 3.14;
myFunction();

function myFunction() {
  "use strict";
  y = 3.14;
}
```

<details>
<summary>Solution</summary>
<div> 

- `x = 3.14;` will not throw an error as it’s efore the `“use strict”;` directive
- `y = 3.14;` will throw an error, as ‘y’ is not declared
</div>
</details>

## Exercise 4
Will this cause an error?
```
"use strict";
function x(p1, p2) {
  alert(p1);
}; 
``` 

<details>
<summary>Solution</summary>
<div> 

No, this will work fine
</div>
</details>