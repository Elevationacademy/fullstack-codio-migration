This will be the most basic of fullstack projects ever.

  

All you will have on your page is **one input box**, alongside a **single button**.

  

When the user presses the button, it should:

-   Take the text from the input
-   Display it
-   Persist it

  

Naturally, **the persisted data should be displayed on page load**.

  

Things to make your life easier:

-   You are **not required** to use any particular library to display the data, such as Handlebars
-   You are **not required** to use OOP, MVC
-   You are **not required** to split your server files - you can have all your server code in one `server.js` file

You **are allowed** to have the following of code ready before you start: 
```
mongoose.connect("mongodb://localhost/DB_NAME", { useNewUrlParser: true, useUnifiedTopology: true })
```