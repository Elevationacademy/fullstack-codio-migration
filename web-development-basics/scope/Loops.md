# Loops

The rules of scope apply to loop blocks as well, for example:

```js
const names = ["Allison", "Beatrice", "Charles"]

for(let n of names){
  let coolName = "cool " + n
  console.log(coolName)
}

console.log(coolName) // throws an error
```
  

The above is what we expect - `coolName` only exists in the scope of the loop.

  

Note also that trying to access `n` outside of the for loop also throws an error! Yes, by saying `let n` we are defining it within the scope of the loop.