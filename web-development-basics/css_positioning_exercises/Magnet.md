# Magnet

Create the following
    

      
![.guides/img/magnet-ex](.\img\magnet-ex.PNG)
    
      
    
For this one, the `border-radius` property will help you.
    
Also, the `border-top-left-radius` property - and other similar ones which you can guess ;)
    

<details><summary>  
Click here to reveal the answer.  
</summary>

HTML (inside the `<body>` tag):

```html
<div id="red-background"><div class="silver-edges" id="edge-1"></div><div class="silver-edges" id="edge-2"></div><div id="white-space"></div>
</div>
```
  

CSS:

  
```css
#red-background {
  background-color: red;
  width: 400px;
  height:250px;
  border-radius: 5%;
  position: relative;
  bottom: 10px;
}

.silver-edges {
  background-color: grey;
  height: 85px;
  width: 85px;
  border-top-left-radius: 7%;
  border-top-right-radius: 7%;
  border: 2px solid grey;
}

#edge-1 {
  position: absolute;
  right: 0;
}

#white-space {
  width: 230px;
  height: 190px;
  background-color: white;
  position: absolute;
  top: 0;
  left: 85px;
  border-bottom-right-radius: 5%;
  border-bottom-left-radius: 5%;
}
```
</details>
