It should come as no surprise that that we can modify values in a matrix similar to how we modify array items.



For instance, say we wanted to change the legendary `7` to a `42`. Hard-coded, it's trivial:

```
matrix[1][2] = 42
print()
//prints:
1       2       3       4
5       6       42      8
9       10      11      12
```


With that knowledge, it should be straightforward to write an `alter` function that receives three parameters: the row number, column number, an updated value, and updates the value accordingly - check out the next spot check ;) .

