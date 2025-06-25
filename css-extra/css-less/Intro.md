
For all the power of CSS3, sometimes we need more. And, ironically, [CSS Less](http://lesscss.org/)gives us more. It stands for **Le**aner **S**tyle **S**heets.

  

CSS Less is one of the number of **CSS pre-processors** out there which allow us to write "plain" CSS with more convenience, then gets **compiled** back directly into CSS.

  

Note that **the browser always reads normal CSS**, but when working with CSS Less we will write in a `.less` file.

  

CSS Less gives us quite a few tools, but in this lesson we will focus on:

-   Nesting
-   Extend
-   Mixins

  

----------

  

#### **SETUP**

  

Since CSS Less is not a browser-native technology, we have to first install it, and do a bit of setup in our IDE.

  

Conveniently, **you can** **`npm install less`** directly into your project - and there is **no need to require it** anywhere.

  

The next part of the setup is to **install the** [**Easy Less**](https://github.com/mrcrowl/vscode-easy-less) **extension in VS Code**. This will automatically compile (i.e. "translate") your `.less` files into `.css` files whenever you save.

  

That's all! Now **create a folder called** `artisan`**, and in it an** **`index.html`** **and** **`style.less`** **file**, and let's begin.

  

**Note:** you do **not** have to create a `.css` file - the extension will create it for you (once you refresh your VS Code), but you do **have to connect your HTML and CSS** files regularly, <ins>to your `.css` file which doesn't exist yet.</ins> And henceforth in this lesson, **only write CSS code in your** **`.less`** **file**.