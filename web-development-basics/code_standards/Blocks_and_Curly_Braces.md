# Blocks and Curly Braces

**if**, **else**, **for**, **while**, and **try blocks** should always use braces ``{}``, and always go on multiple lines.
- The opening brace should be on the same line as the function definition, the conditional, or the loop.
- The closing brace should be on the line directly following the last statement of the block.


<span style="color:red">**Don't**:</span>

```js
function isPositive(num) 
{if(num>0 )
    {
     return true}
return false}

```

<span style="color:green">**Do**:</span>
```js
function isPositive(num){
    if(num>0){
     return true
    }
    return false
}

```

Now it is much more easier for us to track the **opening** and **closing** braces.

### Make sure to always use this structure for code blocks