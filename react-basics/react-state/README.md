# Common Fitfalls

## State updates are async operation

Look at this code, and try to find what is wrong

```
function Counter() {
  const [count,setCount] = useState(0)

  const updateCounter = () => {
      setCount(count + 1)
      console.log(count)
  }

  return (
    <div>
      <button onClick={updateCounter}>+</button> 
      <div>{count}</div> 
    </div>
  );
}
```
If you open the console and click the button you will see that the count is "not updating".
The reason is that the state update is an asynchronous operation, so the count state hasn't been updated yet.  

We will see later how to solve it.
For the mean time, just be aware of it.


## State Objects
When we define a state, some times it will be an object.

For instance, if we have a `classroom` object which has a `students` property in it, and we want to add a student to it, we need to access `classroom.students` first.

  

We need to do the following

  
```
import { useState } from 'react';

const ClassRoom = () => {
    const [classRoom, setClassRoom] = useState({ students: [] });

    const addStudent = (student) => {
      let newClassroom = {...classRoom}
      newClassroom.students = [...classRoom.students, student]
      setClassRoom(newClassroom);
    }
    return <div></div>
}

export default ClassRoom;
```
  
What we are doing here is that we take the old state and clone it first. Then we mutate it to fit our needs and then replace it fully with the new mutated object.

  
Be careful of situations like this.
```
import { useState } from 'react';

const ClassRoom = () => {
    const [classRoom, setClassRoom] = useState({ students: [] });

    const removeStudent = (student) => {
      students = classRoom.students
      students.pop()
    }
    return <div></div>
}

export default useClassRoom;
```
  

This is bad because `classRoom.students` is an array, which is a [reference type](https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0) - that means that even though we've created a new variable, `students`, any modifications we make to that (the `.pop()` on the second line) will still affect the original array in `classRoom`.

  

**Check out** how to use the [ES6 spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) to avoid this problem.