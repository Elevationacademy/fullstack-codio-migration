## Exercise 1

```
:root {
	    --glow-color: #F39C12;
	}
	

	

	@keyframes halo-glowing {
	    from {
	        box-shadow: -1px -1px 5px 5px var(--glow-color);
	    }
	    to {
	        box-shadow: -10px -10px 30px 30px var(--glow-color);
	    }
	} 
	

	

	body {
	    display: grid;
	    background-color: #000000;
	    margin: 0;
	    height: 100vh;
	}
	

	#ball {
	    display: grid;
	    justify-self: center;
	    align-self: center;
	    background-color: var(--glow-color);
	    width: 200px;
	    height: 200px;
	    border-radius: 50%;
      animation-name: halo-glowing;
	    animation-duration: 2s;
	    animation-iteration-count: infinite;
	    animation-direction: alternate;
	    animation-timing-function: linear; 
	}


```


## Exercise 2

```
#ball:hover {
	    box-shadow: -10px -10px 30px 30px var(--glow-color);
}

#ball {
      box-shadow: -1px -1px 5px 5px var(--glow-color);
	

	    transition: box-shadow 2s;
	    transition-timing-function: linear;
}
```


## Exercise 3

HTML:
```
<div id="nav-bar">
	        <div id="button-container">
	            <div id="hamburger" onclick="addMenu()">
	                <div id="line-1" class="line"></div>
	                <div id="line-2" class="line"></div>
	                <div id="line-3" class="line"></div>
	            </div>
	        </div>
</div>

```

JS:
```
const addMenu = function() {
	    
	    $("#button-container").empty().append(
	        `
	        <div id="x-container" onclick="deleteMenu()"
	        <div id="x">
	            <div id="line-x-1" class="line-x"></div>
	            <div id="line-x-2" class="line-x"></div>
	        </div>
	        </div>
	        `
	    )
	    
	    
	    let newHTML = 
	    `<div id="menu-container">
	        <p class="menu-item">Home</p>
	        <p class="menu-item">About</p>
	        <p class="menu-item">Shop</p>
	    </div>`
	    
	    $("body").append(newHTML)
	

	}
	

	const deleteMenu = function() {
	    $("#menu-container").remove()
	}
```


CSS:

```
@keyframes fade-menu {
	    from {
	        width: 0
	    }
	    to {
	        width: 200px;
	    }
	}
	

	

	@keyframes make-x-1 {
	    from{
	        transform: rotate(0deg);
	        margin-left: 0;
	    }
	    to {
	        transform: rotate(-45deg);
	        margin-left: 4px;
	    }
	}
	

	@keyframes make-x-2 {
	    from{
	        transform: rotate(0deg);
	        margin-left: 0;
	        margin-top: 0;
	    }
	    to {
	        transform: rotate(45deg);
	        margin-left: 3px;
	        margin-top: -6px;
	    }
	}
	

	

	

	:root {
	    --secondary-color: #F7D794;
	}
	

	#nav-bar {
	    display: grid;
	    height: 75px;
	    width: 100%;
	    background-color: #CF6A87;
	}
	

	.line {
	    background-color: var(--secondary-color);
	    height: 4px;
	    width:30px;
	    margin: 2px;
	}
	

	#hamburger {
	    display: grid;
	    align-self: center;
	    
	}
	

	#button-container {
	    margin-left: 30px;
	    display: grid;
	    align-self: center;
	}
	

	#menu-container {
	    background-color: var(--secondary-color);
	    height: 500px;
	    width: 200px;
	

	    animation-name: fade-menu;
	    animation-duration: 2s;
	    animation-direction: alternate;
	

	    display: grid;
	    grid-template-rows: repeat(3, 1fr);
	    grid-gap: 20px;
	    overflow: hidden;
	}
	

	/* #menu {
	    display: grid;
	    grid-template-rows: repeat(3, 1fr);
	    grid-gap: 50px;
	} */
	

	.menu-item{
	    margin-left: 10px;
	}
	

	.line-x {
	    background-color: var(--secondary-color);
	    height: 4px;
	    width:30px;
	    margin: 2px;
	}
	

	#line-x-1 {
	    transform: rotate(-45deg);
	    margin-left: 4px;
	

	    animation-name: make-x-1;
	    animation-duration: 1s;
	}
	

	#line-x-2 {
	    transform: rotate(45deg);
	    margin-left: 3px;
	    margin-top: -6px;
	

	    animation-name: make-x-2;
	    animation-duration: 1s;
	}
```
