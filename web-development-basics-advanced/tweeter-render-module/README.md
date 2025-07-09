# Intro

After Completing the Module part of the **M**VC ,It's time to **(partly)** bring our **Tweeter app** to life!

  

If you've got your whole **Tweeter logic module working well** - great. Keep that.

if you did not **complete** it, thats okay! 😄 you can use the following instead for now, since we're only going to deal with rendering and nothing dynamic yet:
<details>
<summary>Tweeter Logic</summary> 

```
const Tweeter = function () {
    const _posts = [
        {
            text: "First post!",
            id: "p1",
            comments: [
                { id: "c1", text: "First comment on first post!" },
                { id: "c2", text: "Second comment on first post!!" },
                { id: "c3", text: "Third comment on first post!!!" }
            ]
        },
        {
            text: "Aw man, I wanted to be first",
            id: "p2",
            comments: [
                { id: "c4", text: "Don't wory second poster, you'll be first one day." },
                { id: "c5", text: "Yeah, believe in yourself!" },
                { id: "c6", text: "Haha second place what a joke." }
            ]
        }
    ]

    const getPosts = () => _posts

    return {
        getPosts: getPosts
    }
}
```

</details>
<br>

Having the getPosts function is enough for this part, because that's all our rendering module will **require**. (we Do **NOT** need anything more than that)

---

Also, here is some HTML (add it to your **tweeter** folder) you should use - it's nothing exciting, and we won't be changing it throughout this project:
```
<!DOCTYPE html>
<html>
  <head>
    <title>Tweeter</title>
    <link href="https://fonts.googleapis.com/css?family=Balthazar" rel="stylesheet">
    <link rel="stylesheet" type="text/css" media="screen" href="style.css" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  </head>
  
  <body>
    <div id="container"><h1 id="title">Tweeter</h1><input type="text" placeholder="What's on your mind?" id="input"><div id="post" onclick="post()">Twit</div><div id="posts"></div></div>
    <script src="render.js"></script> <!-- You'll create this soon --><script src="logic.js"></script> <!-- You've got this --><script src="main.js"></script> <!-- You'll create this soon -->
  </body>
</html>
```