# Solutions

Exercise 1
-
```js
const person = {
	    hungry: true,
	  
	    feed: function () {
	      if (this.hungry) {
	        this.hungry = false;
	        alert('Im no longer hungry!')
	      }
	    }
	  }
	  
	  person.feed() //should alert "I'm no longer hungry"
```
Exercise 2
-
```js
  const pump = function (amount) {
	    this.liters += amount;
	    console.log('You put ' + amount + ' liters in ' + this.name);
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
Exercise 3
-
```js
 const pumpFuel = function (plane) {
	    plane.fuel += 1;
	  };
	  
	  const airplane = {
	    fly: function () {
	      if (this.fuel < 2) { // #1 - add "this" to "fuel"
	        return 'on the ground!';
	      }
	      else {
	        return 'flying!';
	      }
	    },
	    fuel: 0 // #2 - add a "fuel" property with value of 0
	  };
	  
	  console.log('The plane should not be able to fly (yet): ' + airplane.fly());
	  
	  pumpFuel(airplane);
	  console.log('The plane should STILL not be able to fly: ' + airplane.fly());
	  
	  pumpFuel(airplane);
	  console.log('Take off! ' + airplane.fly());
```
Exercise 4
-
```js
  const tipJar = {
	    coinCount: 20,
	    tip: function () {
	      this.coinCount += 1;
	    },
	    stealCoins: function (amount) {
	        this.coinCount -= amount
	    }
	  };
	  
	  tipJar.tip();
	  console.log('Tip jar should have 21 coins: ' + tipJar.coinCount);
	  
	  tipJar.stealCoins(3);
	  console.log('Tip jar should have 18 coins: ' + tipJar.coinCount);
	  
	  tipJar.stealCoins(10);
	  console.log('Tip jar should have 8 coins: ' + tipJar.coinCount);
```
Exercise 5
-
```js
  const revealSecret = function () {
	    return this.secret;
	  };
	  
	  const shoutIt = function (person, func) {
	    person.revealItAll = func;
	    const result = person.revealItAll();
	    alert(person.name + " said: " + result);
	  };
	  
	  const avi = {
	    name: "Avi",
	    secret: "Im scared of snakes!"
	  };
	  
	  const narkis = {
	    name: "Narkis",
	    secret: "I dont have secrets because I'm zen like that."
	  };
	  
	  shoutIt(avi, revealSecret);
	  shoutIt(narkis, revealSecret);
```
Exercise 6
-
```js
const coffeeShop = {
	    beans: 40,
	

	    money: 15,
	  
	    drinkRequirements: {
	      latte: {beanRequirement: 10, price: 10},
	      americano: {beanRequirement: 5, price: 5},
	      doubleShot: {beanRequirement: 15, price: 15},
	      frenchPress: {beanRequirement: 12, price: 12}
	    },
	

	    buyBeans: function(numBeans) {
	

	        this.beans += numBeans
	        this.money -= numBeans * 0.5
	        
	    },
	

	    hasDrink: function(drinkType) {
	        let drinks = Object.keys(this.drinkRequirements)
	        
	        for(let drink of drinks) {
	            if(drink === drinkType){
	                return true
	            }
	        }
	

	        return false
	    },
	

	    hasEnoughBeans: function(drinkType) {
	        if(this.beans > this.drinkRequirements[drinkType].beanRequirement) {
	            return true
	        } else {
	            return false
	        }
	    },
	

	    useBeans: function(drinkType) {
	        this.beans -= this.drinkRequirements[drinkType].beanRequirement
	    },
	  
	    makeDrink: function (drinkType) {
	        
	        /* Because of the exercise extension we already don't need the first if here because we need
	        to check if the drink exists as to not get an error
	        if(!this.hasDrink(drinkType)) {
	            alert("Sorry, we don't make " + drinkType)
	        } else */ if(!this.hasEnoughBeans(drinkType)) {
	            //can also use the buy beans function
	            /*
	            this.buyBeans(this.drinkRequirements[drinkType].beanRequirement)
	            */
	            alert("Sorry we're all out of beans!")
	        } else {
	            this.useBeans(drinkType)
	        }
	

	    },
	

	    buyDrink: function(drinkType) {
	        if(this.hasDrink(drinkType)){
	            this.money += this.drinkRequirements[drinkType].price
	            this.makeDrink(drinkType)
	        } else {
	            alert("Sorry, we don't make " + drinkType)
	        }
	    }
	  }
```