Lets Look at this Example of **Quote Liker**.

```js
import React, { useState } from 'react'
import Quote from './Quote';

export default function Quotes() {
    const [quotes, setQuotes] = useState([
        {id:0 ,text:"Live your life", likes:0},
        {id:1 ,text:"Time is of the essence", likes:0}
      ])

    return (
      <div>
          {quotes.map((quote)=> 
            <Quote quote={quote} onClickEvent={}/>
          )}
      </div>
    );
}
```


|||info
## onClickEvent
Note that this is not an event handler.
This is just a prop that is sent to Quote component. In the Quote components it will be used for onClick event.
|||

---

Lets say we want to implement a handleClick that can increment the likes of each quote.

Initially you might think this is the way to go 

```js
  return (
      <div>
          {quotes.map((quote)=> 
            <Quote quote={quote} onClickEvent={handleClick(quote.id)}/>
          )}
      </div>
    );
}
```

The issue with this is that we need to pass a `callBack` and not an invocation, so when we add the `()` the `handleClick` function actually runs when the component is rendered (when we reach the return part) and not when the event happens.

a Solution to this is the using good design and hierarchy.

We will create a handler inside of `Quotes` which will receive an id and then increase the likes for the relevant `quote`.

this is how we will implement it.


---

### A `Quotes` Component:

```js
import React, { useState } from 'react'
import Quote from './Quote';

export default function Quotes() {
    const [quotes, setQuotes] = useState([
        {id:0 ,text:"Live your life", likes:0},
        {id:1 ,text:"Time is of the essence", likes:0}
      ])
  
      const handleClick = (id) => {
          const newQuotes = quotes.map((quote) => {
            if (quote.id === id) {
              return { ...quote, likes: quote.likes + 1 };
            }
            return quote;
          });
          setQuotes(newQuotes);
        };
  
    return (
      <div>
          {quotes.map((quote)=> 
            <Quote quote={quote} onClickEvent={handleClick}/>
          )}
      </div>
    );
}

```


A `Quote` Component:

```js
import React from 'react'

export default function Quote(props) {
  console.log(props)
  const handleClick = () => {
    props.onClickEvent(props.quote.id)
  }
  return (
    <div>
      <div>{props.quote.text} : {props.quote.likes}</div>
      <button onClick={handleClick}> Like!</button >
    </div>
  )
}
```

What we did here is that we allowedto `handleClick` function to tell us which `quote` needs to be updated.


