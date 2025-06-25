## Exercise 1

Create a simple HTML file that imports a generated .js file (it will be generated from the .ts file you will create).

The HTML file will have an *input* element with class *foo*, and a *button* element which calls a TypeScript function called *doX()*.

The function *doX()* will be inside the .ts file and will include the following logic:
- Use *querySelector* to locate the *input* element from the DOM
- Cast the element to the correct TypeScript class
- Display the input field’s value in the console

<details>
<summary>Solution</summary>
<div> 

#### HTML file
```
<html>
    <head>
        <script src="dom_exercise_1.js"></script>
    </head>
    <body>
        <form>
            <input type="text" class="foo"/>
            <button onClick="doX(); return false;">Submit</button>
        </form>
    </body>
</html>
```

#### TypeScript file
```
function doX() {
    const domElement = document.querySelector('.foo');
    const inputElement = domElement as HTMLInputElement;

    console.log(inputElement.value);
}
```


</div>
</details>

## Exercise 2

Following on from Exercise 1.

Remove the *button* element from the HTML page, and add an event listener for changes to the *input* element (hint: you can use the event *input* in the event listener definition to catch *input* changes).

In the event listener function, make sure you cast the *event* object properly and display the *input* field’s value in the console.

|||info
## Hint

Don’t forget to attach the event listener after the *body* tag has loaded, otherwise your DOM element won’t exist when you try to add the listener.
|||

<details>
<summary>Solution</summary>
<div> 

#### HTML file
```
<html>
    <head>
        <script src="dom_exercise_2.js"></script>
    </head>
    <body onLoad="initPage();">
        <form>
            <input type="text" class="foo"/>
        </form>
    </body>
</html>
```

#### TypeScript file
```
function initPage() {
    const domElement = document.querySelector('.foo') as HTMLInputElement;

    domElement.addEventListener('input', function(event) {
        const e = event.target as HTMLInputElement;
        console.log(e.value);
    });
}
```

</div>
</details>