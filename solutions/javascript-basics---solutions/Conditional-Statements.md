Exercise 1
-
```
if (boughtTesla && isUSCitizen) {
  if(currentYear - yearOfTeslaPurchase >= 4) {
    console.log("Would you like an upgrade")
  }
  else {
    console.log("Are you satisfied with your purchase")
  }
}
else if (boughtTesla) {
  console.log("Would you like to move to the US?")
}
else if (!boughtTesla) {
  console.log("Are you interested in purchasing a Tesla")
} //this last else-if is redundant, understand why?
```
You can see all of the exercise solutions on [this codepen](https://codepen.io/ElevationPen/pen/ZNZqjY?editors=0010) - view at your own risk!