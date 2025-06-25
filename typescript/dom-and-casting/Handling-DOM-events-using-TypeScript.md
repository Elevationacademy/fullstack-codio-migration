When we want to handle events in TypeScript, we need to perform a similar operation, by casting the ‘event.target’ object.

If we try to run the following code, we will get the same error as above. *event.target*, which is class type EventTarget, doesn’t have a ‘value’ attribute.
```
const someElement = document.querySelector(".foo");

someElement.addEventListener("blur", (event) => {
  console.log("event", event.target.value); // ERROR. 
});
```
What we need to do is cast ‘event.target’ to HTMLInputElement, and then the code would work.
```
const someElement = document.querySelector(".foo");

someElement.addEventListener("blur", (event) => {
  const target = event.target as HTMLInputElement;
  console.log("event", target.value); // WORKS
});
```