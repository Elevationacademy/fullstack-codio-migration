Convert the following union types to a type alias.

  
```ts
const val: string | number | boolean = true;

function doX(val: string | number | boolean): string | number | boolean {
    return val == 8;
}

doX(val);
```
  
<details>
<summary>Solution</summary>
<div> 

```ts
type Type = string | number | boolean;
const val: Type = true;

function doX(val: Type): Type {
    return val == 8;
}

doX(val);
```
</div>
</details>
