# Intro

Up to now, whenever we've dealt with the DOM - specifically, whenever we've added/removed things dynamically from the DOM - we just kinda.. _did_ it directly. No sense of order, no single source of responsibility.

Any rogue button or hover could just change things.

  

And while that is fun, it's certainly not a good practice. In fact, it's quite a bad practice.

  

Today we'll see a good way to deal with data, and it all has to do with the flow of data ~

  

----------

  

#### **DATA FLOW**

  

You can think of every application as a machine that takes user input, holds some data (and perhaps modifies it), then gives back some sort of output that's useful to the user.

When the user does something, the data changes, and a new or updated output is given.

  

We'll call this concept "data flow", but it's also known by several other names, including [reactive programming](https://en.wikipedia.org/wiki/Reactive_programming).

  

In most applications we have some data stored in some global variables (arrays or objects).

  

The application usually displays this data in a **view** - in web development, the view is generally the DOM.

This action is called **rendering** - the application **renders** the data on the view:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dataflow1.PNG)

  

**Render** means _cause to be or become; make_.

A **view** is something you can see with your eyes.

  

For example, Facebook takes the data about who you are and what your friends are posting and **renders** it into a **view** of your timeline!

  

Here is a simple example:

  
```
const posts = [
    {
        name: "Uncle Jerome",
        text: "Happy birthday kido!"
    },
    {
        name: "BFF Charlene",
        text: "HEARTS LOVE YOU FOREVER BFF4LYFE HBD"
    },
    {
        name: "Old High School Teacher",
        text: "Hey ace, have a good one."
    }
]
```
  

Assume the above data represents the people who have posted on your wall for your birthday.

  

In order to render this data in your view (your timeline), we would do something like this:

  
```
const render = function () {
    for (let post of posts) {
        let postBox = $("<div class='post-box'><p class=name>" + post.name + "</p><p class=text>" + post.text + "</p></div>")
        $("#timeline").append(postBox)
    }
}
render()
```
  

This is great because our view now reflects our data exactly.

  

But what happens when someone else posts on our timeline?

  

----------

  

From the view the user can trigger some **events** - like a button that posts another birthday wish.

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dataflow2.PNG)

  

So far, in situations like this - where there is an event that should change the DOM, we have been doing something like this:

  
```
$("post").on("click", function () {
    const name = $("input-name").val()
    const text = $("input-text").val()
    $("#timeline").append(newPost(name, text))
    //where newPost is a funciton that creates a post html element with the given name and text
})
```
  

This is bad because there are other events that trigger DOM changes.

  

-   Someone sending you a direct message
-   An invite to Crush-a-Candy
-   Another post on the timeline

  

So many things can change the DOM that if we had loose on.("click")s everywhere it would eventually become very hard to keep track.

  

Instead, when an event happens, **the only thing that should change is data itself!**

  

The idea behind the data flow concept is that **we don't want to change the view directly**. The event should only affect the data.

  

So back to our code, it would look like this:

  
```
$("post").on("click", function () {
    posts.push({
        name: $("input-name").val(),
        text: $("input-text").val()
    })
})
```

The event is still the same - the post has been clicked - but now all we're doing is pushing to our posts array.

  

And now, since our data is updated, we can just call our render function again.

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dataflow3.PNG)

And that's our circle ~