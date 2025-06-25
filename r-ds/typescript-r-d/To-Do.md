Create a file called `Person.interface.ts` and add an interface called `IPerson`. The interface should set the types for the following properties:

-   `name` - string
-   `age` - number
-   `height` - number
-   `hobbies` - array of `hobby` objects (see below)
-   `weight` - number

  

The interface should also have the following methods (see below in the class description how they should be implemented):

-   `grow` -> should not return anything
-   `loseWeight` -> receives a number and does not return anything
-   `addHobby` -> receives a `hobby` object and does not return anything
-   `getHobbiesNames` -> receives nothing and returns an array of strings

  

Now, create a `Person.ts` file and add a class representing a person that will implement the `IPerson` interface.

_* Don't forget to export/import the interface._

  

The class should have the following properties:

-   `name`
-   `age`
-   `height`
-   `hobbies` (array of `hobby` objects. See below)
-   `weight`

_* Note it will receive all as parameters in the `constructor` and should initialize them there._

  

The class should have the following methods:

-   `grow` -> increases the age by one
-   `loseWeight` -> receives a number value as a parameter and decreases the weight by that amount
-   `addHobby` -> receives a `hobby` and adds it to the hobbies array
-   `getHobbiesNames` -> returns an array of just the names of the `hobbies` in the hobbies array

  

  

In a `Hobby.ts` file, create another class called `Hobby`. The class should have two properties (both initialized in the `constructor`):

1.  `hobbyName`
2.  `yearsInHobby`

_* Make an interface for this class as well_

  

----

_In order to test yourself, create a `main.ts` file and add the following code. Then run it and make sure you get the correct results._

  
```
import { Hobby } from './Hobby'
import { Person } from './Person'

const p1 = new Person('Shoobert', 29, 175, 70, [])


p1.grow()
console.log(p1.age) // should print 30

p1.loseWeight(10)
console.log(p1.weight) // should print 60

const h1 = new Hobby('Skating', 20)
console.log(h1.hobbyName) // should print 'Skating'
console.log(h1.years) // should print 20

p1.addHobby(h1)
p1.addHobby(new Hobby('Surfing', 3))

console.log(p1.hobbies)
/* should print
 [
   Hobby { hobbyName: 'Skating', years: 20 },
   Hobby { hobbyName: 'Surfing', years: 3 }
 ]
*/

console.log(p1.getHobbiesNames()) // should print [ 'Skating', 'Surfing' ]
```