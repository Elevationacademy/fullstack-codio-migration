
Sometimes we need to send data to our routes (not through the URL, but through a POST or PUT request, for instance, where we send actual JSON).

  

To that end, we can go to the `Body` tab inside of Postman (say we're making a POST request to `/testData`), select the `raw` radio-button, and make sure you have `JSON (application/json)` selected from the dropdown to the right:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-post-with-data-setup.PNG)

  

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-post-with-data-setup.PNG) to embiggen.

  

Now you need to write the parameters in **legal JSON** - that means double quotes, no trailing commas, and no comments. Example:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-post-with-data-with-json.PNG)

  

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-post-with-data-with-json.PNG) to embiggen.

  

When you press `Send`, you should see that object in your server's logs.