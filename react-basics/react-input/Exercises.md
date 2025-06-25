create a new react project and solve the following:

## Exercise 1
    
Create a component called `Exercise1`, and give it the following code.
    
```
import { useState } from 'react';

const Exercise1 = () => {
    const [person, setPerson] = useState({ name: "", age: "" });

    const handleChange = (event, property) => {
        setPerson({ ...person, [property]: event.target.value });
    }
    return (
        <div>
            <input id="name-input" onChange={(e) => handleChange(e, 'name')} value={person.name} />
            <input id="age-input" onChange={(e) => handleChange(e, 'age')} value={person.age} />
            <button>Go to Bar</button>
        </div>
    );
}
export default Exercise1;
 ```   
      
Your goal is to alert a message when the user presses the `button`.
    
          
The message should include text from both `input`s. For example, if the user types "Haliax" and 40, your alert could say "Come in Haliax, you're 40 - that's good enough".
    
      
    
Make sure that in the `button`'s method you're accessing the `name` and `age` through `state`, and that generally you're working with inputs the proper React way.
    

    
## Exercise 2


Create a component called `Exercise2`, and give it the following code.

```js

import { useState } from 'react';

const Exercise2 = () => {
    const [name, setName] = useState("");
    const [fruit, setFruit] = useState("");

    return (
        <div>
            <input id="name-input" onChange={(e) => setName(e.target.value)} value={name} />
            <select id="select-input" onChange={(e) => setFruit(e.target.value)} value={fruit}>
            </select>
        </div>
    );
}
export default Exercise2;

```

      
Start by checking out the docs about dropdown lists [(select element)](https://www.w3schools.com/tags/tag_select.asp).
    
Next, add a couple of `option`s to the above dropdown, and complete the following:
    
When the user selects an item from the dropdown, it should update the `fruit`  property in state.
    
After the update (don't forget that `useState` set method is asynchronous), you should console log "`<name>` selected `<fruit>`" - make sure you're accessing `name` from `state`!