## Setup

First things first, **fork** and clone this version of the RUPG project --> [https://github.com/Elevationacademy/webpack-rand](https://github.com/Elevationacademy/webpack-rand). Make sure to run `npm install`.
    
      
For this section, you can use [this part](https://webpack.js.org/guides/getting-started/) of the webpack docs.
    
          
Notice, that the `index.html` file is in the `dist` folder and the JS and CSS files are in the `src` folder. The goal of this assignment is that you will configure webpack to output a file called `main.js` to the `dist` repo and that will be the only JS file linked to the HTML. Currently, the application does not work.
    
      
    
To fix it, you will need to:
    
-   Create a `webpack.config.js` file in the root directory with the relevant setup
-   Import the Renderer and APIManager into the `index.js` file (make sure they are being exported)
    -   To import/export files you can use the new [ES6 import syntax](https://www.digitalocean.com/community/tutorials/js-modules-es6)
-   Add the `build` script to the `package.json`
    
          
Open the `index.html` file in the browser and make sure the functionality works (you should be able to click on the buttons and they should display something).
    
      
    
*Note, there should still be no style added to the page.
    

    
## Adding Style

Now, let's add some style to the page. Webpack can allow you to import the CSS files right into JS. Go ahead and add the necessary code and then refresh the page (if you've done so correctly the page should now be styled).
    
      
    
*You can use [this section](https://webpack.js.org/guides/asset-management/#loading-css) of the docs if you need help.

<details>
<summary>
  Click here to reveal a hint.
  </summary>
  You'll need something called a loader.
</details>
    

## External Packages
    
Right now, in addition to linking the `main.js` script to the `index.html`, we are also linking the jQuery and Handlebars CDN. Let's fix that.
    
          
Go ahead and use webpack to import jQuery (and remove the link to it in the HTML file) - use google ;)
    
          
*We'll worry about handlebars in the next section

<details>
<summary>
  Click here to reveal a hint.
  </summary>
  You might want to check out something called a plugin.
</details>   
    

## Extension: Handlebars
    

There are a couple of issues with Handlebars. Firstly, we are linking to it from the HTML (in order to have access to the global Handlebars object), and secondly, we need to write all of our templates inside the HTML file as well (which can make things a bit messy, especially when we have many templates).
    
          
You should:
    
-   Remove the link to Hanldebars in the HTML
-   Move the template scripts from the HTML to the `.handlebars` files - each template should have its own file (you can put all these files inside a folder called `templates` inside the `src` folder)
-   Modify your code in the `Renderer.js` file to use the new templates
    
          
*If you've gotten this far, we'll let you find a source for instructions on your own :P
    
<details>
<summary>
  Click here to reveal a hint.
  </summary>
  You can check out <a href="https://handlebarsjs.com/installation/integrations.html">this link</a> for some help.
</details>
        
    
### WOW! How much more separation of concerns ;)