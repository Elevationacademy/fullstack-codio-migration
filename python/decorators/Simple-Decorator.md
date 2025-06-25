How do we solve the problem?


Of course we don't want to duplicate code in each function.

We need some kind of function solution.

We will use a nested function, but before we solve our problem, let's show the solution for a simpler problem:

instead of printing the arguments before the function execution and the result at the end, we will simply print "before" and "after".


This is how the solution looks like:
```python
def my_decorator(some_func):
  def wrapper():
    print("1. before executing some_func()")
    some_func() # here we execute the function
    print("2. after executing some_func()")
    return wrapper   
  
def just_print():
  print("** some function that uses the decorator")
  
my_func = my_decorator(just_print)
my_func() 
```


In fact what we are doing here is wrapping our just_print function with the `my_decorator` function.​

When we run this code the output will be:

1. Before executing `some_func()` ** some function that uses the decorator
2. After executing `some_func()` 


But as you probably expected, this is just the beginning.

Python has a great syntactic shortcut for us.


Meet the decorator:

Instead of doing: `my_func = my_decorator(just_print)`

we can use the `@`:
```python
# same as just_print = my_decorator(just_print)
@my_decorator
def just_print():
  print("** some function that uses the decorator")


just_print() 
```

The result is the same.

The most wonderful thing about it, it's **short and generic**.

We can even store the decorator in another module, say utils and use it like that:
```python
from utils import my_decorator


@my_decorator
def just_print():
  print("** some function that uses the decorator")


just_print() 
```

So that the decorator function is encapsulated and doesn't get in the way.

---

Now, there is another tiny problem.

What is the name of the function?


Like a good programer, we will check:
```python
@my_decorator
def just_print():
  print("** some function that uses the decorator")


print(just_print.__name__) 
```
:(


The name is wrapper, the name of the inner function of the decorator.

This is not what we wanted...

Luckily, there is a simple solution:

```python
from functools import wraps


def my_decorator(some_func):
  @wraps(some_func)
  def wrapper():
    print("1. before executing some_func()")
    some_func() # here we execute the function
    print("2. after executing some_func()")
  return wrapper  
```

The functools wrap decorator the original function name, docstring, arguments list, etc.

So now if we print the name:
```python
print(just_print.__name__) 
```

We will get:
```output
just_print
```