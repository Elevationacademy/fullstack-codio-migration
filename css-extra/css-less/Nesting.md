
In normal CSS, if we have this HTML setup:

```
<div class="data"><input type="text" placeholder="Tell Us"><button>Send</button>
</div>
```
  

Then we can target the `input` and `button` like so, in our `.css` files:

```
.data input {
  color: orange;
}

.data button {
  font-weight: bold;
}
```
  

The above uses **a space** to target **any** nested children (i.e. the `input` children of the `.data` element.)

  

In CSS Less (in our `.less` file), we can instead target the `input` and `button` like so:

```
.data {
    input {
        color: orange;
    }
}

.data {
    button {
        font-weight bold;
    }
}
```
  

When you **save this file**, you'll notice that a `style.css` file is **created for you**(that's thanks to the extension) - and in that file, you'll see the old CSS with spaces.

  

The main benefit to nesting with CSS Less is that visually it **helps us understand our code better**.

Ultimately, the browser will read the exact same CSS.