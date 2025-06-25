

## Exercise #1 : Timer Decorator

Write a decorator that **prints the time it takes a function to be executed**.

Example for running 2 functions that sum numbers in a range:
```python
sum1 = sum_many(10000000)
sum2 = sum_many_more(50000000) 
```

your decorator should print something like:
```console
function runtime: 0:00:01.184106
function runtime: 0:00:05.506641 
```


## Exercise #2 : Print Function Information

Write a decorator that **prints information about a function execution**.

For each function call the decorator should :

1. Print some data about the function call.
2. Name of the function.
3. All arguments (regular, *args, **kwargs).
4. Execute the original function.
5. Print all the returning data. (value and type).


Here is an example..

Calling:
```python
add(1, 2, age=3, text="hello") 
```

Should return:
```console
func name: add
args: (1, 2)
kwargs: {'age': 3, 'text': 'hello'}
return value: 3
return type: <class 'int'> 
```


## Exercise #3 : Slow Down

Write a decorator that **slows down** the function by 1 second.


## Exercise #4 : Number of calls to a func

1. Write a decorator that **keeps count for how many calls have been done to a function**.
2. Print the number of calls each time the function finishes to execute.



## Exercise #5 : Cache Decorator

Write a decorator that implements a cache mechanism.

The decorator should store results of function calls that already have been made. If a function is being called and the result was already calculated, then the function should return the result immediately, instead of calculate it again.



Test it on a Fibonacci function.


You can write in the first line of the Fibonacci function a print that will tell you which number you are calculating:
```python
def fibonacci(num):
  print("calculating: ", num) 
```

Then when you run the function, each value should be calculated only once.

So running :
```python
print(fibonacci(2))
print(fibonacci(4)) 
```

Should output:
```output
calculating:  2
calculating:  1
calculating:  0 1
calculating:  4
calculating:  3 3 
```

Running the function without the decorator would print:
```console
calculating:  2
calculating:  1
calculating:  0 1
calculating:  4
calculating:  3
calculating:  2
calculating:  1
calculating:  0
calculating:  1
calculating:  2
calculating:  1
calculating:  0 3  
```

hint: store your values in a dict and then before calling the function check if you already got an answer


Make sure your code is generic and you can use the decorator for different functions.


Bonus: support more cases.

For example:
```python
def add(x, *, addition=0, more=0):
  print("running  add")
  return x + 1 + addition + more 
```

**Note:** the * make the kwargs "mandatory kwargs", which mean we must pass them as a key value pair.

You can read more about it [here](https://www.python.org/dev/peps/pep-3102/).


Then when you run the function, each value should be calculated only once.

So running :
```python
add(1, addition=0, more=0)
add(1, more=0, addition=0)
add(1, more=0)
add(1) 
```
Should print:

    running  add 
