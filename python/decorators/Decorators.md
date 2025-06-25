Now, let's go back to the original problem. We wanted to type the parameters of the function.

We will need a new decorator.

Something like:
```python
def print_args(func):
  def inner():
    print("args: ", end=" ")
    for x in args:
      print(x, end=" ")
    print()
    return func() # we also need to pass the parameters
  return inner 
```
but where do we get the parameters from?

First we will remember that the function that is eventually executed is the inner function.
and when we call the decorated add2 function we actually executing inner that execute add2:
```python
def print_args(func):
  def inner():
    print("args: ", end=" ")
    for x in args:
      print(x, end=" ")
    print()
    return func()
  return inner
    
@print_args
def add2(x, y):
  return x+y

add2(1,2) 
```

How do we express general arguments?

Remember `*args` and `**kwargs`?

Great! Let's use them (of course you can go back to functions intermediate lesson and be reminded)

```python
def print_args(func):
  def inner(*args, **kwargs):
    print("args: ", end=" ")
    for x in args:
      print(x, end=" ")
    print()
    res = func(*args, **kwargs)
    print(res)
  return inner
  
@print_args
def add2(x, y):
  return x+y
  
@print_args
def add3(x, y, z):
  return x+y+z

@print_args
def add4(w, x, y, z):
  return w+x+y+z

add2(1,2)
add3(1, 2, 3)
add4(1,2, 2, 4) 
```

Run it and make sure it works.

Note that we also added the the print of the function result, after the function execution.

---

Before we can finally conclude, we will add the last touch.

What happens when we do:
```python
print(add2(1,2)) 
```

We get `None`?? **Yep.**

Can you explain what happened?

<details>
<summary>Click to see the result</summary>
We forgot to return the function result!
</details>

<br>
Let's fix it:
```python
def print_args(func):
  @wraps(some_func)
  def inner(*args, **kwargs):
    print("args: ", end=" ")
    for x in args:
      print(x, end=" ")
    print()
    res = func(*args, **kwargs)
    print(res)
    return res
  return inner 
```

That's it.

The final version of our decorator.



