# Exercises

That's pretty much it for explaining this - but it can be a little tricky to understand without practicing, so here's some practice!

--------
## Exercise 1
Copy/paste the following code into some `.js` file. Fix the errors to make it work:
```js
const person = {
  hungry: true,

  feed: function () {
    if (hungry) {
      hungry = false;
      alert('Im no longer hungry!')
    }
  }
}  

person.feed() //should alert "I'm no longer hungry"
```
-----------
## Exercise 2
Fix the errors to make this work. Here there are two errors in this one.
```js
const pump = function (amount) {
  liters += amount;
  console.log('You put ' + this.amount + ' liters in ' + this.name);
};

const garage = {
  car1: {
    name: 'Audi',
    liters: 3,
    fillTank: pump
  },
  car2: {
    name: 'Mercedes',
    liters: 1,
    fillTank: pump
  }
};

garage.car1.fillTank(2);
console.log('Audi should have 5 liters: ',  garage.car1.liters);

garage.car2.fillTank(30);
console.log('Mercedes should have 31 liters: ', garage.car2.liters);
```

----
## Exercise 3
There are 2 errors to fix here:
```js
const pumpFuel = function (plane) {
  plane.fuel += 1;
};

const airplane = {
  fly: function () {
    if (fuel < 2) {
      return 'on the ground!';
    }
    else {
      return 'flying!';
    }
  }
};

console.log('The plane should not be able to fly (yet): ' + airplane.fly());

pumpFuel(airplane);
console.log('The plane should STILL not be able to fly: ' + airplane.fly());

pumpFuel(airplane);
console.log('Take off! ' + airplane.fly());
```
---
## Exercise 4
Create a method called `stealCoins` that takes a number parameter and decreases the tipJar's coins by that amount:
```js
const tipJar = {
  coinCount: 20,
  tip: function () {
    this.coinCount += 1;
  }
};

tipJar.tip();
console.log('Tip jar should have 21 coins: ' + tipJar.coinCount);

tipJar.stealCoins(3);
console.log('Tip jar should have 18 coins: ' + tipJar.coinCount);

tipJar.stealCoins(10);
console.log('Tip jar should have 8 coins: ' + tipJar.coinCount);
```

-----
## Exercise 5
Aside from the usual, this code also has 3 syntax errors. Fix everything:
```js
const revealSecret = function () {
  return secret;
};

const shoutIt = function (person, func) {
  person.revealItAll = func;
  const result = person.revealItAll();
  alert(person.name + " said: " result);
};

const avi = {
  name: "Avi"
  secret: "Im scared of snakes!"
};

const narkis = {
  name: "Narkis"
  secret: "I dont have secrets because I'm zen like that."
};

shoutIt(avi, revealSecret);
shoutIt(narkis, revealSecret);
```
  

This one is slightly trickier, so take it slow. Drawing helps.

-----
## Exercise 6
Add the following code to some `main.js` file:
```js
const coffeeShop = {
  beans: 40,

  drinkRequirements: {
    latte: 10,
    americano: 5,
    doubleShot: 15,
    frenchPress: 12
  },

  makeDrink: function (drinkType) {
    // TODO: Finish this method
  }
}

coffeeShop.makeDrink("latte"); 
coffeeShop.makeDrink("americano");
coffeeShop.makeDrink("filtered"); //should alert/console "Sorry, we don't make filtered"
coffeeShop.makeDrink("doubleShot");
coffeeShop.makeDrink("frenchPress"); //should alert/console "Sorry, we're all out of beans"
```
  

Read over it, then complete the `makeDrink` method so that it:

-   Only allows you make a drink if it's a drink in the `drinkRequirements` object. Otherwise alert: "Sorry, we don't make "
-   Reduces the `beans` count according to the `drinkRequirements` object and the given `drinkType`
-   Alerts _"Sorry, we're all out of beans!"_ if there are not enough beans to make that drink

  

## EXERCISE 6.1

  

Don't use any _nested_ if statements!

-------

Extension 1
Now give the coffeeShop a money property and the ability to buy more `beans` with a `buyBeans` method.

  

The method should take one parameter - `numBeans`, and should reduce the amount of money depending on `numBeans`.

You decide how much the beans cost ~

---------

Extension 2
This is a business! We need more money to buy more beans!

  

-   Change the `drinkRequirements` object so that instead of `latte: 10`, it looks like this
-   `latte: {beanRequirement: 10, price: 5}` - for each drink
-   Create a `buyDrink` method that accepts 1 parameter: `drinkType`. The method should:

1.  Increase `money` depending on the price of `drinkType`
2.  Call the `makeDrink` method

  

----------

  

#### **DONE.**

Awesome! What a baller you are.
