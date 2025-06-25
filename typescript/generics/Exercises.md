## Exercise 1

Create a function called *sum()* which accepts Generics. The function should only accept the following types: string, string[], number, number[]. You need to type-check them in the function. The function returns a ‘number’ representing the sum of all numbers.

**Function logic:**
- If the function’s parameter is a single number, return it
- If the function’s parameter is a single string, check if it’s a number, if so, return it
- If the function’s parameter is an array of numbers, calculate the sum and return it
- If the function’s parameter is an array of strings, iterate over each element, check if it’s a number, if so, aggregate it and return the sum at the end

**Notes:**
- If an array element is not a number, ignore it and skip to the next element
- You can check if a string can be converted to a number by using the *parseInt(x)* function. Then you can check if the result is a number by using the *!isNaN(x)* function (which checks if the value is NOT a *number*), *true* means it’s a number, and *false* means it’s not.

Create at least 5 examples, covering: a single string, a single number, an array of numbers, and an array of strings (which include multiple types of values). Make sure you output the results of the function using *console.log()*.

<details>
<summary>Solution</summary>
<div> 

```
function sum<Type>(val: Type): number {
    if (Array.isArray(val)) {
        let sum: number = 0;
        val.forEach(elem => sum += getNumValue(elem));
        return sum;
    } else if (typeof val === 'string' || typeof val === 'number') {
        return getNumValue(val);
    } else {
        return 0;
    }
}

function getNumValue(val: string | number): number {
    if (typeof val === 'string') {
        const num: number = parseInt(val);
        return !isNaN(num) ? num : 0;
    } else {
        return val;
    }
}

console.log(sum("23"));
console.log(sum("Tomer"));
console.log(sum(44));
console.log(sum(["test", 22, 55, "block", "9"]));
console.log(sum([23, 433, 11]));

```

</div>
</details>

## Exercise 2

Create a class that will hold an array of Generic types. Add a method called *addNumber()* to the class, which adds a Generic value to the array.

Place the *sum()* and *getNumValue()* functions from exercise 1 into the class, and modify it accordingly. Make sure to use the *this* statement when necessary and remove unnecessary code.

Create 2 examples, where you initialize the new class with some values. For each example, add a few *addNumber()* function calls, and lastly, make sure you print the output of the object’s *sum()* function to the console.


<details>
<summary>Solution</summary>
<div> 

```
class Numbers<Type> {
    numbers: Type[];

    constructor(numbers: Type[]) {
        this.numbers = numbers;
    }

    addNumber(number: Type): void {
        this.numbers.push(number);
    }
    
    sum(): number {
        let total: number = 0;
        this.numbers.forEach(elem => {
            if (typeof elem === 'string' || typeof elem === 'number') {
                total += this.getNumValue(elem)
            }
        });
        return total;
    }
    
    getNumValue(val: string | number): number {
        if (typeof val === 'string') {
            const num: number = parseInt(val);
            return !isNaN(num) ? num : 0;
        } else {
            return val;
        }
    }
}

const numbers1: Numbers<string> = new Numbers<string>(["test", "22"]);
numbers1.addNumber("55");
numbers1.addNumber("block");
numbers1.addNumber("9");

const numbers2: Numbers<number> = new Numbers<number>([23]);
numbers2.addNumber(433);
numbers2.addNumber(11);

console.log(`1: ${numbers1.sum()}`);
console.log(`2: ${numbers2.sum()}`);
```

</div>
</details>