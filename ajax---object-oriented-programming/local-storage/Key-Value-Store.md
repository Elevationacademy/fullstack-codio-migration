
Ultimately, Local Storage is merely a plain object, stored in your browser, that hold **keys** and **values** - should be familiar from your work with JS/JSON.

  

Open the Console tab in the Chrome DevTools. All three of the lines below do the _same_ thing. Pick one, type it into the console, and then hit enter.
```
// Functions
localStorage.setItem('name', 'Shoobert');

// Object
localStorage.name = 'Shoobert';

// Object
localStorage['name'] = 'Shoobert';
```

Now if you type localStorage into your dev console, you should see it as an object with course.cohortStudentId as one of the keys. Likely you'll see other stuff that's been utilizing your local storage as well (that's ElevationLearn storing some information about you!)

  

**Refresh the browser**. Still see the name key? Yep! That's because local storage persists data in the browser itself.

  

Aside from the ways we'll teach you to remove things from Local Storage (as developers), the only way a user can accidentally (or on purpose) clear their local storage is via [these conditions](https://stackoverflow.com/questions/8537112/when-is-localstorage-cleared) - it depends on the browser.

  

Also important to note, there is no (reasonable) limit to how much we can store in Local Storage. But if you use the same key twice, the second time will overwrite the first - as we know.

  

We'll see soon how we can store things aside from strings.