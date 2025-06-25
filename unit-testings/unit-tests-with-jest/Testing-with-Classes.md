
We've been testing loose functions so far, but of course we could do the same with classes. It's just a matter of creating an instance for the test:

  

<ins>**Code to be tested**:</ins>

```
class PictureManager {
    constructor() {
        this.pictureURLs = []
    }

    addPicture(picURL) {
        this.pictureURLs.push(picURL)
    }

    removePicture(picURL) {
        this.pictureURLs.splice(this.pictureURLs.indexOf(picURL), 1)
    }
}

module.exports = PictureManager
```
  

<ins>**Test**:</ins>

```
const PM = require('./code')

test("addPicture should add a picture URL to the pictureURLs array", function () {
  //sanity 
  const picManager = new PM()
  expect(picManager.pictureURLs.length).toBe(0)
  
  picManager.addPicture("some_url")
  expect(picManager.pictureURLs.length).toBe(1)           //test
  expect(picManager.pictureURLs).toContain("some_url")    //double check 
})
```
  

Notice that **we prefer to instantiate a class _inside of a test_** to make sure we're starting fresh.

  

**Write a test for the** **`removePicture`** **method.**

  

**Note**: you don't have to comment out your old test anymore - this is still the same class!

Check [here](https://codepen.io/ElevationPen/pen/MdEMOx?editors=0010) for the solution.