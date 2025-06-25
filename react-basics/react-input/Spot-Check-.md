
Here is the input we created:
```
const InputTest = () => {
    const [text, setText] = useState("")

    const updateText = (event) => {
        setText(event.target)
    }

    return (
        <div>
            <input type="text" value={text} onChange={updateText} />
        </div>
    )
}

export default InputTest
```
add an `input type="checkbox"` and capture its value the React way. 
Make sure you do a 2 way binding.

Remember that we don't use the `value` attribute but rather the `checked` attribute for checkboxes.

  

[This resource](https://www.w3schools.com/jsref/prop_checkbox_checked.asp) might help.

  

Console log the boolean to make sure you got it.

  
<details>
  <summary>
     Solution
  </summary>

```js

import React, { useState } from 'react';

const InputTest = () => {
  const [inputValue, setInputValue] = useState('');
  const [checkboxValue, setCheckboxValue] = useState(false);

    const updateText = (event) => {
        setInputValue(event.target)
    }
  
  const handleCheckboxChange = (event) => {
    setCheckboxValue(event.target.checked);
  }

  return (
    <div>
      <input type="text" value={text} onChange={updateText} />
      <input type="checkbox" checked={checkboxValue} onChange={handleCheckboxChange}/>
    </div>
  )
}

export default InputTest

```

</details>