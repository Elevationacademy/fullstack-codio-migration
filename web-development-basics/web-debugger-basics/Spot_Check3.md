# Spot Check: Watch Practice

In the following assignment please do not use console.log!

Please run this code in Chrome:
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
    let numberLength = number.toString().length
    return parseInt(number.toString().split("")[numberLength - 1])
}

foo()
```



## Answer the Following Questions:
Use the **watch** panel and the devtools to answer these questions.

1. What is the largest value of `number % 18` when calling `getSecondDigit` ? 
1. What is the value of `sum * 33` after the first time `getLastDigit` is being called?



<details>
  <summary>
     Answers
  </summary>
    1. 17
    2. 231
</details>