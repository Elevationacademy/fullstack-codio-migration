# Spacing

When we space in between different elements in our code we need to be carefull to use the correct moderation.

maintaining a code with too many spaces can be very hard and uncomfortable to keep track off, and having a code with no spaces can make it annoying to understand (specially if a colleague is trying to understand your code)

- Place a space between operators, assigments ("=") and their operands
- Make sure to not use more than **one** space in between elements in your code


<span style="color:red">**Don't**:</span>

```js
//binary operators
a=b-c;          
a = b-c;        
a=b - c;  

//acessing array/object
arr [0];

//casts
objectInstance. get(key);  
```

<span style="color:green">**Do**:</span>

```js
//binary operators
a = b - c;          
 
//acessing array/object
arr[0];

//casts
objectInstance.get(key);  
```

---

