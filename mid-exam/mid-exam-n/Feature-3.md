The Feature that we will be adding to the Project is **Pagination ⭐**

While we progress in developing our App, we notice that sometimes we have too many recipes displayed and it was overwhelming to read all of them.

![](https://i.pinimg.com/originals/d0/75/f8/d075f82b2f1ae5d67f7b8600513e1654.jpg)

We want to add the ability to display our recipes partly, meaning we want to send the recipes in patches (pages).

so you will need to implement the following:

- a `pagination` functionality to get a fixed amount of `recipes` in a request and display them in the client.
- a `navigation` functionality to navigate between the patches of the `recipes`

This means we will be in control of how many recipes we will display in a page and keep track of which recipes are displayed.


|||important
## Pagination

it means sending the data in patches, for the first result your limit would be for example 5 results.
so if you have 19 results of recipes. 
you will need to send 4 batches each one of them has 5 results.
|||


Watch this video for reference:
<video width="640" height="360" controls>
  <source src=".guides/img/f3-1.mov" type="video/mp4">
</video>

### Bonus (complete this feature if you have the time)
Take care of edge case!
Make sure we can not navigate more or less than the results we got. 

|||important
## Notice

Please notice that you will need to edit both `Client` and `Server`.
|||

|||topic
## Progress

We recommend that you will work in patches and make sure everything works step by step.
|||