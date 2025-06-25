When we enable TypeScript in web development frameworks such as React and Angular, we need to take into account that writing TypeScript code that interacts with DOM elements and events, is based on a concept called ‘casting’.

As interacting with HTML elements is dynamic and occurs at run-time, we need to place special attention to types, and we need to ‘cast’, i.e. ‘adjust’ the types we receive via DOM elements and via event handling, to the equivalent TypeScript types.

In this chapter we will cover:
1. Interacting with DOM elements using TypeScript
1. Handling DOM events using TypeScript