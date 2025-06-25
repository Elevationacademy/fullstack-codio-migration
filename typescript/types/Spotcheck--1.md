
Given the following statements, what would be the expected output?

  
```
let id: number = 7;
let lastName = 'Smith';
let isEmpty: boolean = true;

id = '8';
lastName = 'Jordan';
isEmpty = 1;
```
  
<details>
<summary>Solution</summary>
<div> 

```
id = '8'; // ERROR, 'id' is a number and not a string
lastName = 'Jordan'; // OK
isEmpty = 1; // ERROR, 'isEmpty' is boolean and not a number
```
</div>
</details>

