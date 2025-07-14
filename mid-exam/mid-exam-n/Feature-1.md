The Feature that we will be adding to the Project is **Sharing Recipe by Email ⭐**

![alt text](.guides/img/f1-3.jpeg)

Now that you can filter and find recipes you like, you want to be able to email the recipe and the recipe video to who you think would like it!

We will be using the `mailto` hyperlink.

so you will need to implement the following:
- Add a "Share via Email" Button for each recipe.

- This button should invoke a `mailto` link which will open a new email with the following needed data


The structure of the email should be:

- Subject : Check out this recipe! [insert recipe name]

- Body : You can see the recipe in this video : [insert link]

Check out this video and picture.

Picture: 
![alt text](.guides/img/f1-1.png)

Video:
<video width="640" height="360" controls>
  <source src=".guides/img/f1-2.mov" type="video/mp4">
</video>

<hr/>
<br/>

You can use this link to generate such link : [Generator](https://www.sender.net/mailto-link-generator/)

|||topic
## Progress

We recommend that you will hard code an example with fixed data, then dynamically generate the link with the proper data
|||