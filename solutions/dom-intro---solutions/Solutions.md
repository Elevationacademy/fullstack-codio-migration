
Completing the Game
-
index.html:
```html
<div id="container"><div id="playing-field" class="centered"><div id="block" class="centered"></div></div><div id="arrows" class="centered"><div id="up" class="arrow" onclick="moveUp()">&uarr;</div><div id="left" class="arrow" onclick="moveLeft()">&larr;</div><div id="right" class="arrow" onclick="moveRight()">&rarr;</div><div id="down" class="arrow" onclick="moveDown()">&darr;</div></div>
</div>
```
  

main.js:
```js
const playingField = document.getElementById("playing-field")
const down = document.getElementById("down")
const ball = document.getElementById("block")
ball.style.backgroundColor = "yellow"
	
const header = document.createElement("h1")
header.innerHTML = "The Best Game Ever"
header.style.color = "#c0392b"
header.style.fontFamily = "Helvetica"
document.body.appendChild(header)
	
const subHeader = document.createElement("h2")
subHeader.innerHTML = "Game by: Danny Brudner"
subHeader.setAttribute("class", "sub-header")
document.body.appendChild(subHeader)
	
const moveUp = function () {
  const initialVal = parseInt(ball.style.top) || 0
  ball.style.top = (initialVal - 15) + "px"
}
  	
const moveLeft = function () {
  const initialVal = parseInt(ball.style.left) || 0
  ball.style.left = (initialVal - 15) + "px"
}
      	
const moveRight = function () {
  const initialVal = parseInt(ball.style.left) || 0
  ball.style.left = (initialVal + 15) + "px"
}
          	
const moveDown = function () {
  const initialVal = parseInt(ball.style.top) || 0
  ball.style.top = (initialVal + 15) + "px"
}
```
Reservations
-
index.html:
```html
 <input id="name" type="text" placeholder="Who are you?" value="">
<button onclick="checkReservation()"> Check Reservation</button>
```
  

main.js
```js
const reservations = {
  Bob: { claimed: false },
  Ted: { claimed: true }
}

const checkReservation = function () {
  const name = document.getElementById("name").value
  const lowerCaseName = name.toLowerCase()
  const editedName = lowerCaseName.charAt(0).toUpperCase() + lowerCaseName.slice(1)
  if (reservations[editedName] && !reservations[editedName].claimed) {
    alert("Welcome in, " + editedName)
    reservations[editedName].claimed = true
  } else if (reservations[editedName] && reservations[editedName].claimed) {
    alert("Hmm, someone already claimed this reservation")
  } else if (!reservations[editedName]) {
    alert("You have no reservation")
    reservations[editedName] = { claimed: true } 
  }
}
```
Visual Overload
-
HTML (inside <body> element)::

<div id="container"></div>

  

CSS:
```css
#container {
  display: flex;
}

.box {
  width: 100px;
  height: 100px;
  border: 1px solid black;
  margin: 1px;
}
```
  

JS:
```js
const getRandomColor = function () {
  const niceColors = ['#8e44ad', '#3498db', '#c0392b', '#f1c40f', '#d35400', '#2ecc71', '#1abc9c', '#2c3e50', '#7f8c8d'];
  const randomPosition = Math.floor(Math.random() * niceColors.length);
  return niceColors[randomPosition];
};

for (let i = 1; i < 8; i++) {
  const newBox = document.createElement('div');
  newBox.setAttribute('class', 'box');
  newBox.style.backgroundColor = getRandomColor();
  newBox.onmouseenter = function () {
    const randomColor = getRandomColor();
    newBox.style.backgroundColor = randomColor;
  };
  document.getElementById('container').appendChild(newBox);
}
```
Form
-
HTML:

  
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>

    <link rel="stylesheet" type="text/css" media="screen" href="style.css">

</head>

<body>

    <div id="container">
        <div id="form">
            <div class="main">
                <div>Name</div>
                <input type="text" placeholder="Enter your name" id="name">
            </div>
            <div class="main">
                <div class="second-line">
                    <div>Desired Salary</div>
                    <input type="number" placeholder="Salary" id="desired-salary" class="input">
                </div>
                <div class="second-line">
                    <div>Birthday</div>
                    <input type="date" id="birthday" class="input">
                </div>
            </div>
            <div class="main">
                <div>Phone</div>
                <input type="number" placeholder="Enter phone number" id="phone" class="input">
            </div>
            <button id="button" onclick="validate()">Submit</button>
        </div>
    </div>

    <script src="main.js"></script>
</body>

</html>
```
  

CSS:

  
```css
body {
  font-family: helvetica;
}

#container {
  position: relative;
  background-color: #1abc9c;
  display: inline-block;
  padding-top: 40px;
  padding-bottom: 40px;
  padding-right: 20px;
  padding-left: 20px;
  border: #16a085 solid 4px;
}

#form {
  position: relative;
  width: 350px;
  height: 300px;
}

.main {
  margin: 12px;
}

.second-line {
  display: inline-block;
}

#error-message {
  color: red;
  position: absolute;
}

#name{
  width: 100%;
}

#desired-salary {
  width: 150px;
}

#birthday {
  width: 100%;
}

#phone {
  width: 100%;
}

#button {
  position: absolute;
  right: 20px;
  bottom: 20px;
  background-color: #34495e;
  color: #95a5a6;
  border: #2c3e50 solid 3px;

  width: 75px;
  height:35px;
  border-radius: 5%
}
```
  

JS:

  
```js
const isMissing = function(input) {
  if(input.length === 0) {
      return true
  } else {
      return false
  }
}

const message = document.createElement("div")
message.setAttribute("id", "error-message")

const validate = function() {

  const form = document.getElementById("form")
  const name = document.getElementById("name").value
  const salary = parseInt(document.getElementById("desired-salary").value)
  console.log(salary)
  const birthday = document.getElementById("birthday").value
  const phone = document.getElementById("phone").value



  if(isMissing(name)){
      message.innerHTML = "Name is missing"
  } else if(name.length <= 2) {
          message.innerHTML = "Name is too short, please enter name with more than 2 characters"
  } else if (isMissing(salary)) {
      message.innerHTML = "Desired salary is missing"
  } else if((salary < 10000)) {
      message.innerHTML = "Salary must be greater than 10000"
  } else if((salary > 16000)) {
      message.innerHTML = "Salary must be less than 16000"
  } else if (isMissing(birthday) || birthday === null) {
      message.innerHTML = "Please enter your birthday"
  } else if(isMissing(phone)) {
      message.innerHTML = "Phone is missing"
  } else if(phone.length < 10) {
      message.innerHTML = "Phone number too short, must be 10 digits"
  } else if(phone.length > 10) {
      message.innerHTML = "Phone number too long, must be 10 digits"
  } else {
      form.style.display = "none"const welcome = document.createElement("h1")
      welcome.innerHTML = "Welcome in, " + name
      welcome.style.color = "green"document.body.appendChild(welcome)
  }




  document.getElementById("form").appendChild(message)

}
```
