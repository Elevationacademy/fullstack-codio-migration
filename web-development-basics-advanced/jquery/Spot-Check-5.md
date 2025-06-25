
Create an element with two data attributes: barcode and expirationDate

Then, use jQuery to grab both and print out _The item with barcode 311192 will expire on 18-02-2030_

  

**Hint:** there's a small issue here, but with enough console logging you'll figure it out ;)

  

If not, you can see check [here](https://codepen.io/ElevationPen/pen/PvgVXd?editors=1010).

  
<details><summary>
  Click here to reveal the answer.
</summary>

Read [here](https://stackoverflow.com/questions/20985204/does-jquery-internally-convert-html5-data-attribute-keys-to-lowercase) to go in depth about the issue, but the gist of it is that when we use data() the way we do, it will lowercase the data attribute for us.

</details>
