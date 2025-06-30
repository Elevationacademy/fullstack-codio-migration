# Exercises: Conditional Statements


Exercise 
-
Tesla (the electric car company) is building a prototype for an AI salesperson. To do this, it needs _you_ to code part of the flow of the initial conversation with the customer. The rules of the flow are as follow:

  

-   If the customer has previously bought a Tesla, and the customer is a US citizen, the AI should check how long ago the customer bought their Tesla
-   If the Tesla was bought four or more years ago, the AI should ask (console log) whether the customer would like an upgrade
-   Otherwise, it should ask whether the customer is satisfied with the car
-   If the customer is not as US citizen but has bought a Tesla, the AI should ask whether the customer would like to move to the US
-   If the customer has not bought a Tesla, the AI should ask whether they are interested in buying one

  

For the following task you are given these inputs from each customer:

  
```js
let boughtTesla = true
const yearOfTeslaPurchase = 2014
let isUSCitizen = true
let currentYear = 2018
```
  

For your tests, change the values to make sure all the cases are working. For the above inputs, your AI prototype should output "Would you like an upgrade?"

