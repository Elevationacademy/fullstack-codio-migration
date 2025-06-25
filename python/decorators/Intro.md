In this lesson we will learn about **decorators**.

**Decorators** are functions that allows you run some code before and after a function.


Let's say that we have written some functions, and for each one of them whenever we execute it, there will be a print of the function variables, before the function starts and the result of the function after the execution.


So if we have:
```python
def add2(x, y):
  return x+y
  
def add3(x, y, z):
  return x+y+z

def add4(w, x, y, z):
  return w+x+y+z 
```
We want to execute:
```python
add2(1,2)
add3(1, 2, 3)
add4(1,2, 2, 4) 
```

And we want our code to print:
```console
args:  1 2
args:  1 2 3
args:  1 2 2 4  
```

What are our options of implementation?

Think about it for a minute, and move on to see what python has to offer.
