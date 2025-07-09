# Intro

You must have noticed by now, that there are many ways we can write an implementation for a specific task.
These different implementations will affect the code's efficiency, clarity and more.
In this lesson we are going to explore the impact of the design of our code on the maintenance, flexibility and safety of our program.

We have mentioned principles that are important for high quality code such **generic code**. 

For example this code is what we call **hard coded**, and therefor not very flexible. 
```

function initArr() {
  let numbers = []

  for (let i = 0; i < 3; i++) {
    numbers[i] = i + 1
  }
  return numbers
}
```

What if we want to initialize the array with numbers from 10 to 20?

In order to make this code more generic we would want to pass the arguments of start and end to the `initArr` function.

```js
function initArr(start, end) {
    let numbers = []

    for (let i = 0; start <= end; i++, start++) {
        numbers[i] = start
    }
    return numbers
}
```

In this case we are thinking about the future uses of this code, what other cases it might need to support, such as different numbers we might want to initialize in the array, and which code modifications will we have to do to support these changes. So principles like generic code, helps us write more flexible and easy to maintain code!

# OOD 
In this chapter we will focus on **OOD** (Object Oriented Design) principles. We are going to focus on modules (which can be Classes or built-in Objects) and their interaction with one another. 

# SOLID 
There are many approaches and principles to guide us, but now we will focus on 5 important principles called **SOLID principles**.
These principles were introduced by Robert C. Martin, aka Uncle Bob in 2000, and swiftly became very popular.