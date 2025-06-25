
#### **FONT AWESOME**

  

Whether you've thought about it explicitly or not, the web is riddled with icons. For a user, an icon is a clear indicator of an action, state, or location.

  

For instance:

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A226-0.png) is a common icon indicating something that can be deleted/removed

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A226-1.png) means something is complete or correct

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A226-2.png) will generally bring us to a "Settings" page

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A226-3.png) allows us to "like" something

  

And so on, and so forth.

  

There are a few ways to implement these icons, but maybe on of the simpler ways is by using [Font Awesome](https://fontawesome.com/) - a mostly free service with tons of icons.

  

To set up, add this line at the top of your root (usually index) HTML file, inside your `head` tag:

  
```html
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
```
  

The above will effectively give us access to all of Font Awesome's icons, so that when we use them (below) they actually appear on our page.

  

Next, check out Font Awesome's [icon gallery](https://fontawesome.com/icons?d=gallery) to find the icons you need. An icon will usually look something like this:

  
```html
<i class="fab fa-android"></i>
```
  

And then just drop an icon wherever you want in your HTML, like a normal element- because it _is_ a normal element, an i tag, plus the power of Font Awesome.

  

By the way, since these icons are just a normal HTML, **we can also color them like normal text! Just use the** **color** **property in CSS** ![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A226-4.png)
