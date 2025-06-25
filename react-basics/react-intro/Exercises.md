
 ## Exercise 1

That's it for our briefest of React intros, for now we're going to practice JSX.
    
      
    
For these exercises (as with the previous spot checks), you should write all your code as indicated in your `App.js` file, inside the `App` class.
    
      
    
   Remember, the App can **only return JSX***.
    
   <sup> Other methods can _also_ return JSX, but don't have to
    
      
    
   ***
    
      
    
   Inside `App`
   
```js
function App() {
  const showCompany = (name, revenue) => { }

  return (
    <div className="ex-space">
      <h4 className='ex-title'>Exercise 1</h4>
      <div className="exercise" id="ex-1">
        {/* your code here */}
      </div>
    </div>
  )
}
```

you'll find a method called `showCompany` that receives two parameters: a string `name`, and a number `revenue`. This method should return a `div` with an `id` of the `CompanyName` with the text `CompanyName` makes Revenue every year inside the `div`.
    
      
    
Then, use the following data to display every company's info. Notice that this data should be outside of the `return`:
    
      

  ```js
    let companies = [
      { name: "Tesla", revenue: 140 },
      { name: "Microsoft", revenue: 300 },
      { name: "Google", revenue: 600 }
    ]
```  
      
    
   Ultimately, in this exercise you are creating the following by invoking `showCompany` on each of the above companies.
    
      
    
  ```html
   <div id="Tesla">Tesla makes 140 every year</div>
   <div id="Microsoft... 
 ```   
      
    
 **Hint:** there is a way to do this with a normal for loop, but it will be easier to use one of the [array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) - remember, the return method _must_ `return` some JSX.
    

 
   
   ## Exercise 2

```js
function App() {
  const getClassName = (temperature) => { }

  return (
    <div className="ex-space">
      <h4 className='ex-title'>Exercise 2</h4>
      <div className="exercise" id="ex-2">
        {/* your code here */}
      </div>
    </div>
  )
}
```

    
   For this exercise, write your code in the `getClassName` method. This method receives a single number parameter `temperature`, and should return **one** of the following strings:
    
   -   "freezing" - if the temperature is below 15
    -   "fair" - if the temperature is between 15 and 30
    -   "hell-scape" - otherwise
    
      
    
   Your `App` should return a single `div` that has an `id` of `weatherBox` and a `className`. The `className` depends the `getClassName` invocation.
    
      
    
Your browser will ultimately render **one** of the following as a result:
    
      
    
   ```html 
    <div id="weatherBox" class="freezing"></div>
    <div id="weatherBox" class="fair"></div>
    <div id="weatherBox" class="hell-scape"></div>
  ```  
      
    
   To help check that you've done everything right, add some CSS to your `App.css` file. You should:
    
      
    
   -   Give the `#weatherBox` a height and width of `300px`
    -   Give the `freezing` class a background-color of aqua
    -   Give the `fair` class a background-color of orange
    -   Give the `hell-scape` class a background-color of red
    
      
    
 You should be able to test your  `getClassName`  method with different values and see different colored boxes appear on the page.
