
There are a few simple rules about JSON that makes writing it slightly more "strict" than writing raw JavaScript objects.

  

1.  Single quotes ( i.e. ' ) cannot be used to surround strings or keys; only double quotes ( i.e. " ) are allowed.

  

**Good**
```
{ "hello": "world" }
```
  

**Bad**
```
{
 "uh": 'oh',
 'super': "bad"
}
```
  

2. Keys _must_ be surrounded by double quotes, even if they don't contain any "special" characters.

  

**Good**
```
{ "yeah": "baby" }
```
  

**Bad**
```
{ not: "allowed" }
```
  

3. The final item in an array, or the final key-value pair in an object, **cannot** be followed by a "trailing", or "dangling" comma ( i.e. , ).

  

**Good**
```
{
 "stuff": [
   "foo",
   "bar"
 ],

 "other_stuff": {
   "baz": true
 }
}
```
  

**Bad**
```
{
 "all_sorts_of": [
   {
     "bad stuff": "going down over here",
   }
 ],
}
```
  

4. Comments are not allowed.
```javascript
{
 // Sad day, this is wrong :("_comment": "This is dumb, but it works!"
}
```
  

Another thing to keep in mind is that outside of strings, whitespace (i.e. spaces and new lines) isn't significant. Practically, this means that:

  
```
{"hello":"world"}
```
  

and

  
```
{
 "hello": "world"
}
```
  

are two valid, if different, ways to express the _same_ underlying JSON document.

Keep those few rules in mind, and you'll be writing serious JSON in no time!

  

----------

  

#### **ORDER**

  

One thing to keep in mind is how "order" is handled in JSON - it is similar to how we treat order in JS objects.

  

Ordering can be thought of as how you would iterate over the members of an object or array.

  

The key-value pairs in objects are explicitly defined as _having no order_! This means that:

  
```
{
  "a": 1,
  "b": 2
}
```
  

must be treated as exactly the same object as:

  
```
{
  "b": 2,
  "a": 1
}
```
 

This means that objects have "undefined", or "insignificant" ordering, and that you should never assume that the key-value pairs in an object will come to you in any particular order!

  

Arrays, however, are different beasts. Within arrays, order is guaranteed. This means that:

  
```
["a", "b"]
```
  

and...

  
```
["b", "a"]
``` 

are _two different_ arrays! When you iterate over them, you'll get the elements in two different orders. This means that within arrays, order is "defined", or "significant".