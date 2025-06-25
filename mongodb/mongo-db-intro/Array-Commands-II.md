
We can use `pull` to remove all instances from an array that match some filter:

  

```js
db.firstCollection.update(  
    {name: "Soren"}, 
    {$pull: {
        dreams: "Being like Razu"
    }}
)
```
  

Or just remove the last item from the array using `pop`:

  

```js
db.firstCollection.update(  
    {name: "Soren"}, 
    {$pop: {
        dreams: 1
    }}
)
```
  

We would use `-1` in the above to remove the _first_ item in the array instead of the last.
