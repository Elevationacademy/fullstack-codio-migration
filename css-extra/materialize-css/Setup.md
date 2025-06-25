
Materialize has a [great explanation](https://materializecss.com/getting-started.html) on how the setup works - **we recommend using** **`npm install`** because you're pros. Remember that you still need to link the CSS and JS files, something like this:

  
```
<!DOCTYPE html>
<html>
<head>
<!--Import Google Icon Font-->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<!--Import materialize.css-->
<link type="text/css" rel="stylesheet" href="css/materialize.min.css" media="screen,projection"/>
<!--Let browser know website is optimized for mobile-->
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>

<body>

<!--JavaScript at end of body for optimized loading-->
<script type="text/javascript" src="js/materialize.min.js"></script>

</body>
</html>
```
  

The above boilerplate is taken directly from the docs, so notice a few things:

-   You'll probably have to change the `href` and `src` for the CSS and JS links because yours will be in your `node_modules`
    -   Note that the actual files you're looking for are in the `dist` folder
-   Notice that Materialize also brings in `Material+Icons` from Google fonts - that's cool

  

If you've setup correctly, you should be able to add the button code from earlier to your HTML (before the `script`) and see the result on your page.