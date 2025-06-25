## Exercises


There are other methods we can use to traverse the DOM, such as [siblings](https://api.jquery.com/siblings/), [children](https://api.jquery.com/children/), and [many others](https://api.jquery.com/category/traversing/).

  

Each has their own use, though generally we tend to get by with closest and find.

  

You'll get to practice this all soon, but for now check out the following exercise.

  

----------

  

You have become the lead hardware engineer for a computer lab at an incredibly prestigious facility. It's in Britain.

  

In your lab you have 3 supercomputers, each with its own specifications.

Each computer, among other things, has two buttons: a validator and a generator

  

These buttons are your only way to interact with the other parts of each computer.

  

Here is your lab (instructions below):

  
```
<div id="lab"><div class="computer" data-id="F00T-W411"><p class="BUS">CX9-3312</p><p class="MB">#000000111</p><div class="processor" id="J0Y-FU11"><span class="QR">Wizz-Knob</span><span class="QR">Nooq</span><button class="generator">Cromp</button></div><div class="ram"><div class="DDR"><button class="validator">Womp</button></div></div></div>

  <div class="computer" data-id="G11U-X522"><p class="BUS">DY0-4423</p><p class="MB">#111111222</p><div class="processor" id="K1Z-GV22"><span class="QR">Quimbor</span><span class="QR">Kroon</span><button class="generator">Dimp</button></div><div class="ram"><div class="DDR"><button class="validator">Ballimp</button></div></div></div>

  <div class="computer" data-id="H22V-Y633"><p class="BUS">EZ1-5534</p><p class="MB">#222222333</p><div class="processor" id="L2A-HW33"><span class="QR">Shelk</span><span class="QR">Mutix</span><button class="generator">Phomer</button></div><div class="ram"><div class="DDR"><button class="validator">Mayth</button></div></div></div>
</div>
```
  

As lead hardware engineer, your task is to write some code that reacts to clicks on both buttons.

  

**When the** **generator** **button is clicked**, you should console log the following values for its computer:

  

-   The processor ID
-   The computer's data-id - also, push this to an array in an object like this: {cmp_id: id}
-   The BUS number

  

**When the** **validator** **button is clicked**, you should console log the following values for its computer:

  

-   The generator's text
-   The MB
-   Both QRs

  

For example, when you click on the Phomer generator, you should log the following:

  

Processor ID: L2A-HW33

Computer's data-id: H22V-Y633

BUS: EZ1-5534

  

----------

  

### **DONE**

Traversing the DOM is pretty cool. We are now like skaters, gently gliding through the elements at our beckoning.