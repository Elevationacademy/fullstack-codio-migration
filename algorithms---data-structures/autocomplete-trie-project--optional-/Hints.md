<details><summary>
  Click here to reveal some hints:
</summary>
  
You should make two helper functions in your class to help with your `predictWords` method:

```

-   _getRemainingTree()
  -   This method will receive a input and a node
  -   This method will go through your tree by the first letter of the string, going down the input until you are at the last letter of the input
  -   This method should return the final node of the **provided** string (e.g. if the string was "hu", the method will return the node with the value "U"

-   _allWordsHelper()
  -   This method should receive the string prefix (the input), a node, and an array of `allWords` as a parameter
  -   This function will need to loop through each of the current nodes children **and**recursively run on each child
  -   Each letter should be added to the string prefix being passed to the next recursive function
  -   When you hit a node that has `endOfWord = true`, add it to your `allWords` array
  -   The function should return the `allWords` array
  ```
</details>