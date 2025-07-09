# Present

# Present

Create the following:

![.guides/img/ex1](.\img\ex1.PNG)
<details><summary>  
Click here to reveal the answer.  
</summary>

HTML (inside the `<body>` tag)

```html
<div id="parent"><div class="child" id="child-1"></div><div class="child" id="child-2"></div>
</div>﻿﻿
```
  

  

CSS:

```css
#parent {
  display: inline-block;
  background-color: blue;
  width: 300px;
  height: 300px;
}

.child {
  background-color: red;
}

#child-1 {
  position: absolute;
  width: 300px;
  height: 20px;
  top: 50px;
}

#child-2 {
  position: absolute;
  height: 300px;
  width: 20px;
  left: 50px;
}
```
</details>