## Exercise 1

Create a function called *concat()* which takes two parameters, one is a union of string and string[], and the other is a union of a *boolean* and a *number*. The purpose of the function is to concatenate the strings (one or more) sent to the function.

The first parameter is the string or strings to concatenate, and the second parameter determines if the result should be printed out to the console. The second parameter is a *boolean* flag, either as a true/false boolean, or a ‘0’ (false) or ‘1’ (true) flag.

Create at least 4 examples of using this function covering all 4 combinations, and at least 1 exception (e.g. when the *number* flag is not ‘0’ or ‘1’).

|||info
## Hint

Pay close attention to all scenarios, both types and values, and triple-check your code before you stop.
|||

<details>
<summary>Solution</summary>

```
function concat(strArray: string | string[], isPrint: boolean | number): void {
    if (Array.isArray(strArray)) {
        strArray = strArray.join(' ');
    } else if (typeof strArray !== 'string') {
        console.log(`Function doesn't support type ${typeof strArray}`);
    }

    if ((typeof isPrint === 'boolean' && isPrint) || (typeof isPrint === 'number' && isPrint === 1)) {
        console.log(strArray);
    } else if ((typeof isPrint !== 'boolean' && !isPrint)) {
        console.log(`Function doesn't support 'isPrinted' with value '${isPrint}'`);
    }
}

concat("Tomer", false);
concat("Tomer", 2);
concat(["Tomer", "Sagi"], 1);
concat(["Tomer", "Sagi"], 0);
concat(["Michael", "Jordan", "is", "the", "King"], true);
```

</details>

## Exercise 2

We want to create a function that can print one or phone numbers, and we want this function to be able to receive 4 different types, and by that, making it flexible to handle different types of values, e.g.:
string - a single number in a string format, e.g. “0521231122”
string[] - an array of string numbers, e.g. [“0521231122”, “0523212211”]
number - a single number in number format, e.g. 972521231122
number[] - an array of numbers, e.g. [972521231122, 972523212211]

We would need to define a new type alias that will define a union of the above types, and the new function called ‘print_numbers’ will receive this type as a parameter.

Inside the function, you will check the type, and for each one, print the type, followed by the value. Printing should be done using the *console.log()* function.

Here is an example of how to query an Array type and a *number* or *string* type:
- *Array.isArray(numbers)* → returns true/false if the variable *numbers* is an array
- *typeof numbers === 'string'* → returns true/false if the variable is of type *string*

Lastly, you need to call the function 4 times, each with a different type as defined in the above list, showing how the function works in each scenario.


<details>
<summary>Solution</summary>
<div> 

```
type PhoneNumbers = string | string[] | number | number[];

function print_numbers(numbers: PhoneNumbers): void {
    if (Array.isArray(numbers)) {
        console.log("Array: " + numbers);
    } else if (typeof numbers === 'string') { 
        console.log('string: ' + numbers);
    } else if (typeof numbers === 'number') {
        console.log('number: ' + numbers);
    }
}

print_numbers(972528684411);
print_numbers([972528684411, 9725242223]);
print_numbers("052863423243");
print_numbers(["052343434286", "0547734343"]);
```

</div>
</details>