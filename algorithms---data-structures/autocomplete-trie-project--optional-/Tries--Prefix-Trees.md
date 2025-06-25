
The main difference between tries and binary search trees is that tries can have many children. Whereas binary search trees only have a right child and left child, a trie will have a children property which links to each of it's child nodes.

  

Here's an example of a trie:

  

![](https://cdn-images-1.medium.com/max/1600/1*jL2Rc-EpEmNZII552xX7Ig.jpeg)

  

As you can see, our root is a blank node - from it will link the first letters of every word of our dictionary. Any path followed down should consist of a word when the values are added together.

  

One of the most common applications for Tries are auto complete or predictive text programs, which is why we'll be using it to build our auto complete.

  

This is because the search for a word is quite quick - in a worst case scenario searching for a word has an **O (m)**time complexity - where is m is the length of the word.