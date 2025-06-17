# Spot Check: Breakpoint Practice

In the following assignment please do not use console.log!

Here is a piece of code:
```js
function foo(){
    let sum = 0
    for (let i = 1000; i < 2000; i++){
        if (i % 203 === 0){
            sum += getSecondDigit(i)
        } else if (i % 497 === 0) {
            sum += getLastDigit(i)
        } else if (i % 293 === 0) {
            sum += getLastDigit(i*13)
        } 
    }
    return sum
}

function getSecondDigit(number){
    return parseInt(number.toString().split("")[0])
}

function getLastDigit(number){
    return parseInt(number.toString().split("")[number.length - 1])
}

foo()
```

Please run this code in Chrome.

## Answer the Following Questions:
Use break points and the devtools to answer these questions.

1. Is there a time when `getSecondDigit` is being called with the number 1623 as a parameter? 
1. How many times `getLastDigit` is being called when `i % 293 === 0`?
1. Is there a time when `getLastDigit` is being called with a number parameter that has `1` as it's last digit? what is the value of that number parameter?


<details>
  <summary>
     Solution
  </summary>
  <ol>
  <li>No. It is being called with 1624</li>
   <li>3</li>
    <li>Yes, 1491.</li>
  </ol>



</details>